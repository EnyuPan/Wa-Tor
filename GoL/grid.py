from enum import Enum

class CellState(Enum):
    DEAD = (0, '_')
    ALIVE = (1, 'X')

class Cell:
    def __init__(self, i: int, j: int, state: CellState):
        self.i = i
        self.j = j
        self.state = state
    
    def __str__(self):
        return f"(Cell at {self.i}, {self.j}): {self.state.value[1]}"
    
    def get_state(self):
        return self.state

    def set_state(self, state: CellState):
        self.state = state

class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(i, j, CellState.DEAD) for j in range(cols)] for i in range(rows)]
    
    def __str__(self):
        s = ""
        for i in range(self.rows):
            for j in range(self.cols):
                if j > 0:
                    s += " "
                s += str(self.cells[i][j].state.value[1])
            s += "\n"
        s += "rows: " + str(self.rows) + ", cols: " + str(self.cols)
        return s
    
    '''
    grid.from_list():
    Accepts lists of integers where each element is 0 (for empty), 1 (for fish), or 2 (for shark),
    or lists of characters where each element is '_' (for empty), 'f' (for fish), or 's' (for shark)
    '''
    def from_list(self, L: list[list[int]]):
        if len(L) == 0:
            raise Exception("List cannot be empty")
        self.rows = len(L)
        self.cols = len(L[0])
        self.cells = [[Cell(i, j, CellState.DEAD) for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if L[i][j] in CellState.ALIVE.value:
                    self.cells[i][j].state = CellState.ALIVE
        return self

    def get_cellstate(self, i, j):
        return self.cells[i][j].get_state()

    def set_cellstate(self, i, j, state: CellState):
        self.cells[i][j].set_state(state)


grid = Grid(5, 6)
print(grid)
print(grid.from_list([[0, 0, 1, 1, 1], [2, 0, 1, 2, 1]]))
print(grid.get_cellstate(0, 2))
grid.set_cellstate(0, 0, CellState.ALIVE)
print(grid)
