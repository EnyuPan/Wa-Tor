from grid import Grid
from enum import Enum

class Commands(Enum):
    INIT_GRID = 1 # requires 2 arguments, representing the numbers of rows and cols
    SET_CELL = 2 # requires 3 arguments, representing i, j, and creature type
    POPULATE = 3 # requires 2 arguments, representing the numbers of fish and sharks
    TICK = 4 # requires no arguments
    RESET_GRID = 5 # requires no arguments
    QUIT = 6 # requires no arguments

class Game:
    def __init__(self, grid: Grid=None):
        self.grid = grid
        self.running = False
    
    def run(self):
        self.running = True
    
    def quit(self):
        self.running = False

    def process_input(self, *args):
        if not(self.running):
            return
        if args[0] == Commands.INIT_GRID:
            self.grid = Grid(args[1], args[2])
        elif args[0] == Commands.SET_CELL:
            self.grid.set_cell(args[1], args[2], args[3])
        elif args[0] == Commands.POPULATE:
            self.grid.populate(args[1], args[2])
        elif args[0] == Commands.TICK:
            self.grid.tick()
        elif args[0] == Commands.RESET_GRID:
            self.grid.reset()
        elif args[0] == Commands.QUIT:
            self.quit()
