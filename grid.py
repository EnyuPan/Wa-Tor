from creature import Dir, Creature, Fish, Shark

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

    def add_creature(self, creature: Creature):
        self.creature = creature
    
    def remove_creature(self):
        self.creature = None

    '''
    Returns list of creatures around self in von Neumann neighborhood (checks for grid boundaries);
    does not include self
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
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(i, j, self, None) for j in range(cols)] for i in range(rows)]
    
    def get_cell(self, i, j):
        return self.cells[i][j]

    def set_cell(self, i, j, creature: Creature):
        self.cells[i][j].creature = creature
        return self.cells[i][j]

    def get_neighbors(self, i, j):
        return self.cells[i][j].get_neighbors()
