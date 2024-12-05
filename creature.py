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
            return
        neighbor = random.choice(free_neighbors)
        self.cell.remove_creature()
        neighbor.add_creature(self)
        self.cell = neighbor
    
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
    def __init__(self, cell, reproduce_threshold=5, energy=10):
        super().__init__(cell, reproduce_threshold)
        self.energy = energy
    
    def __repr__(self):
        return f"SHARK(energy:{self.energy})"
    
    def inc_energy(self):
        self.energy += 1
    
    def dec_energy(self):
        self.energy -= 1
        if self.energy == 0:
            self.die()
    
    def move(self):
        # ???
        self.dec_energy()
    
    def reproduce(self):
        pass
        # ???
    
    def act(self):
        # TODO
        pass

