from abc import ABC, abstractmethod
from enum import Enum

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
    def reproduce(self):
        pass

    @abstractmethod
    def move(self, dir: Dir):
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
    
    def reproduce(self):
        pass
        # ???
    
    def move(self, dir: Dir):
        pass
        # ???
    
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
    def reproduce(self):
        pass
        # ???
    
    def move(self, dir: Dir):
        # ???
        self.dec_energy()
    
    def act(self):
        pass
        # ???

