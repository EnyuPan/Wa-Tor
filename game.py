from typing import Literal
from grid import Grid
import creature
from enum import Enum

class Commands(Enum):
    INIT_GRID = 1 # requires 2 arguments, representing the numbers of rows and cols; requires self is active
    GET_CELL = 2 # requires 2 arguments, representing i and j; returns a string representing the creature type at the cell
    SET_CELL = 3 # requires 3 arguments, representing i, j, and creature type; requires self is active
    POPULATE = 4 # requires 2 arguments, representing the numbers of fish and sharks; requires self is active
    TICK = 5 # requires self is active
    RESET_GRID = 6 # requires self is active
    RUN = 7
    PAUSE = 8
    QUIT = 9

class Game:
    def __init__(self, grid: Grid=None):
        self.grid = grid
        if (self.grid == None):
            self.rows = 0
            self.cols = 0
        else:
            self.rows = self.grid.rows
            self.cols = self.grid.cols
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

    def process_input(self, *args) -> None | Literal['N/A'] | Literal['EMPTY'] | Literal['FISH'] | Literal['SHARK']:
        if args[0] == Commands.INIT_GRID:
            self.grid = Grid(args[1], args[2])
            self.rows = args[1]
            self.cols = args[2]
        elif args[0] == Commands.RUN:
            self.run()
        elif args[0] == Commands.PAUSE:
            self.pause()
        elif args[0] == Commands.QUIT:
            self.quit()
        elif args[0] == Commands.GET_CELL:
            if self.grid == None:
                return "N/A"
            cell = self.grid.get_cell(args[1], args[2])
            if cell.creature == None:
                return "EMPTY"
            elif isinstance(cell.creature, creature.Fish):
                return "FISH"
            elif isinstance(cell.creature, creature.Shark):
                return "SHARK"            
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
