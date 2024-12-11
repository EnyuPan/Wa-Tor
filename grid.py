from creature import Creature, Fish, Shark
from typing import Union
import random

class Cell:
    def __init__(self, i: int, j: int, grid, creature: Creature=None):
        self.i = i
        self.j = j
        self.grid = grid
        self.creature = creature
    
    def __repr__(self):
        return f"Cell({self.i}, {self.j}, {self.creature})"
    
    def __str__(self):
        s = f"Cell at ({self.i}, {self.j}): "
        if self.creature == None:
            s += "EMPTY"
        elif isinstance(self.creature, Fish):
            s += "FISH"
        elif isinstance(self.creature, Shark):
            s += "SHARK"
        return s

    '''
    add_creature(): accepts either an instance of Creature or a string (one of "Empty", "Fish", or "Shark")
    '''
    def add_creature(self, creature: Union[Creature, str]):
        if creature == None:
            self.creature = None
            return
        if isinstance(creature, Creature):
            self.creature = creature
        elif isinstance(creature, str):
            creature_str = creature.strip().lower()
            if creature_str == "empty":
                self.creature = None
            elif creature_str == "fish":
                self.creature = Fish(self)
            elif creature_str == "shark":
                self.creature = Shark(self)
        if isinstance(self.creature, Fish):
            self.grid.fishset.add(self.creature)
        elif isinstance(self.creature, Shark):
            self.grid.sharkset.add(self.creature)
    
    def remove_creature(self):
        if isinstance(self.creature, Fish):
            self.grid.fishset.discard(self.creature)
        elif isinstance(self.creature, Shark):
            self.grid.sharkset.discard(self.creature)
        self.creature = None

    '''
    Returns list of creatures around self in von Neumann neighborhood (checks for grid boundaries),
    not including self
    '''
    def get_neighbors(self) -> list[Creature]:
        neighbors = []
        cells = self.grid.cells
        if self.i > 0:
            neighbors.append(cells[self.i - 1][self.j])
        if self.i < self.grid.rows - 1:
            neighbors.append(cells[self.i + 1][self.j])
        if self.j > 0:
            neighbors.append(cells[self.i][self.j - 1])
        if self.j < self.grid.cols - 1:
            neighbors.append(cells[self.i][self.j + 1])
        return neighbors

class Grid:
    def __init__(self, rows: int, cols: int, time: int=0):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(i, j, self, None) for j in range(cols)] for i in range(rows)]
        self.time = time
        self.fishset = set()
        self.sharkset = set()
    
    def __str__(self):
        s = ""
        for i in range(self.rows):
            for j in range(self.cols):
                if j > 0:
                    s += " "
                creature = self.cells[i][j].creature
                if creature == None:
                    s += "_"
                elif isinstance(creature, Fish):
                    s += "f"
                elif isinstance(creature, Shark):
                    s += "S"
            s += "\n"
        s += f"rows: {self.rows}, cols: {self.cols}, time: {self.time}\nfish: {self.fishset}, sharks: {self.sharkset}"
        return s
    
    def get_cell(self, i, j) -> Cell:
        return self.cells[i][j]

    def set_cell(self, i, j, creature: Union[Creature, str]) -> Cell:
        self.cells[i][j].add_creature(creature)            
        return self.cells[i][j]

    def get_fish(self) -> set[Creature]:
        return self.fishset
    
    def get_sharks(self) -> set[Creature]:
        return self.sharkset

    def get_neighbors(self, i, j) -> list[Cell]:
        return self.cells[i][j].get_neighbors()

    def tick(self):
        for s in random.sample(list(self.sharkset), len(self.sharkset)):
            s.act()
        for f in random.sample(list(self.fishset), len(self.fishset)):
            f.act()
        self.time += 1
    
    def reset(self):
        for s in random.sample(list(self.sharkset), len(self.sharkset)):
            s.die()
        for f in random.sample(list(self.fishset), len(self.fishset)):
            f.die()
        self.time = 0
