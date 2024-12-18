from grid import Grid
from enum import Enum

class Commands(Enum):
    INIT_GRID = 1 # requires 2 arguments, representing the numbers of rows and cols; requires self is active
    SET_CELL = 2 # requires 3 arguments, representing i, j, and creature type; requires self is active
    POPULATE = 3 # requires 2 arguments, representing the numbers of fish and sharks; requires self is active
    TICK = 4 # requires self is active
    RESET_GRID = 5 # requires self is active
    RUN = 6
    PAUSE = 7
    QUIT = 8

class Game:
    def __init__(self, grid: Grid=None):
        self.grid = grid
        self.running = True
        self.active = False # True if the game is accepting commands; False if the game is paused
    
    def run(self):
        self.running = True
        self.active = True
    
    def pause(self):
        self.active = False
    
    def quit(self):
        self.running = False
        self.active = False

    def process_input(self, *args):
        if args[0] == Commands.INIT_GRID:
            self.grid = Grid(args[1], args[2])
        elif args[0] == Commands.RUN:
            self.run()
        elif args[0] == Commands.PAUSE:
            self.pause()
        elif args[0] == Commands.QUIT:
            self.quit()
        elif self.active:
            if args[0] == Commands.SET_CELL:
                self.grid.set_cell(args[1], args[2], args[3])
            elif args[0] == Commands.POPULATE:
                self.grid.populate(args[1], args[2])
            elif args[0] == Commands.TICK:
                self.grid.tick()
            elif args[0] == Commands.RESET_GRID:
                self.grid.reset()
        else:
            print("Game paused - enter X to resume")
