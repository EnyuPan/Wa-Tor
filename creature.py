from abc import ABC, abstractmethod
from enum import Enum
import random

class Dir(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

class Creature(ABC):
    def __init__(self, cell, reproduce_threshold=5):
        self.cell = cell
        self.reproduce_timer = 0
        self.reproduce_threshold = reproduce_threshold
    
    def inc_reproduce_timer(self):
        self.reproduce_timer += 1
    
    def reset_reproduce_timer(self):
        self.reproduce_timer = 0

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def act(self):
        pass
    
    def die(self):
        self.cell.remove_creature()
        self.cell = None

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
    
    def reproduce(self):
        old_cell = self.cell
        self.move()
        if self.cell != old_cell:
            old_cell.add_creature(Fish(old_cell))
        self.reset_reproduce_timer()
    
    def act(self):
        pass
        # ???

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
            dest.creature.die()
            self.boost_energy()
        self.cell.remove_creature()
        dest.add_creature(self)
        self.cell = dest
        self.dec_energy()
    
    def reproduce(self):
        pass
        # ???
    
    def act(self):
        # TODO
        pass

