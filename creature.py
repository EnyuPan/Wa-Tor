from abc import ABC, abstractmethod
import random

class Creature(ABC):
    def __init__(self, cell, reproduce_threshold=5):
        self.cell = cell
        self.reproduce_timer = 0
        self.reproduce_threshold = reproduce_threshold
        self.alive = True
    
    def inc_reproduce_timer(self):
        self.reproduce_timer += 1
    
    def reset_reproduce_timer(self):
        self.reproduce_timer = 0

    @abstractmethod
    def move(self):
        pass
    
    def reproduce(self):
        old_cell = self.cell
        self.move()
        if self.alive and self.cell != old_cell:
            old_cell.add_creature(Fish(old_cell))
        self.reset_reproduce_timer()
        print(f"{self} at ({old_cell.i}, {old_cell.j}) reproduced!")

    def act(self):
        if not(self.alive):
            return
        if self.reproduce_timer >= self.reproduce_threshold:
            self.reproduce()
        else:
            self.move()
        self.inc_reproduce_timer()
    
    def die(self):
        self.cell.remove_creature()
        self.cell = None
        self.alive = False

class Fish(Creature):
    def __init__(self, cell, reproduce_threshold=5):
        super().__init__(cell, reproduce_threshold)

    def __repr__(self):
        return f"FISH" # TODO
    
    '''
    fish::move(): move to a random unoccupied neighboring cell
    '''
    def move(self):
        neighbors = self.cell.get_neighbors()
        free_neighbors = [ne for ne in neighbors if ne.creature == None]
        if free_neighbors == []:
            return # stays in the same cell if no neighboring cells are unoccupied
        dest = random.choice(free_neighbors)
        self.cell.remove_creature()
        dest.add_creature(self)
        self.cell = dest

class Shark(Creature):
    def __init__(self, cell, reproduce_threshold=5, energy=10, eating_energy_boost=4):
        super().__init__(cell, reproduce_threshold)
        self.energy = energy
        self.eating_energy_boost = eating_energy_boost
    
    def __repr__(self):
        return f"SHARK(energy:{self.energy})"
    
    def inc_energy(self):
        self.energy += 1
    
    def boost_energy(self): # energy gained from eating a fish
        self.energy += self.eating_energy_boost
    
    def dec_energy(self):
        self.energy -= 1
        if self.energy == 0:
            self.die()
    
    def move(self):
        neighbors = self.cell.get_neighbors()
        fish_neighbors = [ne for ne in neighbors if isinstance(ne.creature, Fish)]
        free_neighbors = [ne for ne in neighbors if ne.creature == None]
        if fish_neighbors == []:
            if free_neighbors == []:
                return
            dest = random.choice(free_neighbors)
        else:
            dest = random.choice(fish_neighbors)
            print(f"{self} at ({self.cell.i}, {self.cell.j}) ate {dest.creature} at ({dest.i}, {dest.j})!")
            dest.creature.die()
            self.boost_energy()
        self.cell.remove_creature()
        dest.add_creature(self)
        self.cell = dest
        self.dec_energy()
