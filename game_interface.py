from abc import ABC, abstractmethod
from game import Game, Commands
import pyglet

class GameInterface(ABC):
    def __init__(self, game: Game=None):
        self.game = game
        self.setup()
    
    '''
    setup(): takes the necessary steps to initialize the game; is always called automatically
    in __init__(); must be implemented by subclasses
    '''
    @abstractmethod
    def setup(self):
        pass
    
    @abstractmethod
    def update_display(self):
        pass
    
    @abstractmethod
    def handle_input(self):
        pass

class CommandInterface(GameInterface):
    def __init__(self, game: Game=None):
        super().__init__(game)
    
    def setup(self):
        if self.game == None:
            self.game = Game()
        self.game.run()
        self.game.process_input(Commands.INIT_GRID, int(input("Enter number of rows: ")), int(input("Enter number of cols: ")))
    
    def update_display(self):
        print(self.game.grid)
    
    def handle_input(self):
        s = input("Enter command (X: run, Z: pause, F: add fish, S: add shark, T: tick, R: reset, P: populate, Q: quit): ").lower()
        if s == "q":
            self.game.process_input(Commands.QUIT)
        elif s == "z":
            self.game.process_input(Commands.PAUSE)
        elif s == "x":
            self.game.process_input(Commands.RUN)
        elif s == "f":
            self.game.process_input(Commands.SET_CELL, int(input("row: ")), int(input("col: ")), "fish")
        elif s == "s":
            self.game.process_input(Commands.SET_CELL, int(input("row: ")), int(input("col: ")), "shark")
        elif s == "r":
            self.game.process_input(Commands.RESET_GRID)
        elif s == "t":
            self.game.process_input(Commands.TICK)
        elif s == "p":
            self.game.process_input(Commands.POPULATE, int(input("number of fish: ")), int(input("number of sharks: ")))

class GraphicalInterface(GameInterface):
    def __init__(self, game: Game):
        super().__init__(game)
        self.window = pyglet.window.Window()
    
    def update_display(self):
        self.window.clear()
        # TODO...
    
    def handle_input(self):
        pass
