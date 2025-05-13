from abc import ABC, abstractmethod
from game import Game, Commands
import pyglet
from enum import Enum
from typing import Union

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
    def run(self):
        pass
    
    @abstractmethod
    def update_display(self):
        pass

class CommandInterface(GameInterface):
    def __init__(self, game: Game=None):
        super().__init__(game)
    
    def setup(self):
        if self.game == None:
            self.game = Game()
        self.game.run()
        self.game.process_input(Commands.INIT_GRID, int(input("Enter number of rows: ")), int(input("Enter number of cols: ")))
    
    def run(self):
        while self.game.running:
            if self.game.active:
                self.update_display()
            self.handle_input()
    
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
    class GridDimensions:
        def __init__(self, rows: int, cols: int, window_width, window_height):
            self.margins_h = window_width // 20
            self.margins_v = window_height // 20
            self.grid_width = window_width - 2 * self.margins_h # width of the grid in pixels
            self.grid_height = window_height - 2 * self.margins_v # height of the grid in pixels
            self.cell_width = self.grid_width / rows
            self.cell_height = self.grid_height / cols
            self.cell_margin_h = self.cell_width // 15
            self.cell_margin_v = self.cell_height // 15
    
    class ColorScheme:
        def __init__(self, fish_color=(0, 0, 255), shark_color=(255, 0, 0), empty_a_color=(125, 255, 200), empty_b_color=(50, 200, 100)):
            self.cell_colors = {
                "fish": fish_color,
                "shark": shark_color,
                "empty_a": empty_a_color,
                "empty_b": empty_b_color
            }
    
    class ScreenTransition(Enum):
        START = 0 # transition from select dimensions screen to running screen
        PAUSE = 1 # transition from running screen to paused screen
        UNPAUSE = 2 # transition from paused screen to running screen
    
    class Screen(ABC): # represents a game state; owned by instances of GraphicalInterface
        def __init__(self, gi: 'GraphicalInterface'):
            # gi is a reference to the GraphicalInterface instance that owns this screen
            self.gi = gi
        
        @abstractmethod
        def transition(self, transition: 'GraphicalInterface.ScreenTransition') -> Union['GraphicalInterface.Screen', None]:
            pass
        @abstractmethod
        def handle_mouse_press(self, x, y, button, modifiers):
            pass
        @abstractmethod
        def handle_key_press(self, symbol, modifiers):
            pass
        @abstractmethod
        def handle_text(self, text):
            pass
        @abstractmethod
        def update(self):
            pass
    
    class SelectDimensionsScreen(Screen):
        def __init__(self, gi: 'GraphicalInterface'):
            super().__init__(gi)
        
        def transition(self, transition: 'GraphicalInterface.ScreenTransition') -> Union['GraphicalInterface.Screen', None]:
            if transition == GraphicalInterface.ScreenTransition.RUN:
                return GraphicalInterface.RunningScreen(self.game)
        
        def handle_mouse_press(self, x, y, button, modifiers):
            pass
        def handle_key_press(self, symbol, modifiers):
            pass
        def handle_text(self, text):
            pass
        def update(self):
            pass
    
    class RunningScreen(Screen):
        def __init__(self, gi: 'GraphicalInterface'):
            super().__init__(gi)
        
        def transition(self, transition: 'GraphicalInterface.ScreenTransition') -> Union['GraphicalInterface.Screen', None]:
            if transition == GraphicalInterface.ScreenTransition.PAUSE:
                return GraphicalInterface.PausedScreen(self.game)
        
        def handle_mouse_press(self, x, y, button, modifiers):
            # coordinates of the cell clicked, with (0, 0) at the top left corner
            cell_x = int((x - self.gi.grid_dimensions.margins_h) // (self.gi.grid_dimensions.grid_width / self.gi.game.rows))
            cell_y = self.gi.game.cols - 1 - int((y - self.gi.grid_dimensions.margins_v) // (self.gi.grid_dimensions.grid_height / self.gi.game.cols))
            if cell_x >= 0 and cell_x < self.gi.game.rows and cell_y >= 0 and cell_y < self.gi.game.cols:
                cell_contents = self.gi.game.process_input(Commands.GET_CELL, cell_x, cell_y)
                if cell_contents == "FISH":
                    self.gi.game.process_input(Commands.SET_CELL, cell_x, cell_y, "shark")
                elif cell_contents == "SHARK":
                    self.gi.game.process_input(Commands.SET_CELL, cell_x, cell_y, "empty")
                elif cell_contents == "EMPTY":
                    self.gi.game.process_input(Commands.SET_CELL, cell_x, cell_y, "fish")
        
        def handle_key_press(self, symbol, modifiers):
            if (symbol == pyglet.window.key.SPACE):
                self.gi.game.process_input(Commands.TICK)
        
        def handle_text(self, text):
            pass

        def update(self):
            rows = self.gi.game.rows
            cols = self.gi.game.cols
            b = pyglet.graphics.Batch()
            cells = [None] * rows * cols
            if rows == 0 or cols == 0:
                return
            for i in range(rows):
                for j in range(cols):
                    cell_contents = self.gi.game.process_input(Commands.GET_CELL, i, j)
                    if cell_contents == "FISH":
                        cell_col = self.gi.color_scheme.cell_colors["fish"]
                    elif cell_contents == "SHARK":
                        cell_col = self.gi.color_scheme.cell_colors["shark"]
                    elif (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                        cell_col = self.gi.color_scheme.cell_colors["empty_a"]
                    else:
                        cell_col = self.gi.color_scheme.cell_colors["empty_b"]
                    # coordinates of the top-left corner of the cell; (0, 0) is at the top left corner
                    gd = self.gi.grid_dimensions
                    x = gd.margins_h + i * gd.cell_width
                    y = gd.margins_v + (cols - 1 - j) * gd.cell_height
                    cells[i * rows + j] = pyglet.shapes.Rectangle(
                        x + gd.cell_margin_h, y + gd.cell_margin_v,
                        gd.cell_width - 2 * gd.cell_margin_h, gd.cell_height - 2 * gd.cell_margin_v,
                        color=cell_col, batch=b
                    )
            b.draw()
    
    class PausedScreen(Screen):
        def __init__(self, gi: 'GraphicalInterface'):
            super().__init__(gi)
        
        def transition(self, transition: 'GraphicalInterface.ScreenTransition') -> Union['GraphicalInterface.Screen', None]:
            if transition == GraphicalInterface.ScreenTransition.UNPAUSE:
                return GraphicalInterface.RunningScreen(self.game)
        
        def handle_mouse_press(self, x, y, button, modifiers):
            pass
        def handle_key_press(self, symbol, modifiers):
            pass
        def handle_text(self, text):
            pass
        def update(self):
            pass
    
    # GraphicalInterface methods
    def __init__(self, window_height: int=600, window_width: int=600, game: Game=None):
        super().__init__(game)
        self.window = pyglet.window.Window(window_width, window_height, "Wa-Tor", resizable=True)
        
        # set up miscellaneous data classes
        self.grid_dimensions = self.GridDimensions(self.game.rows, self.game.cols, self.window.width, self.window.height)
        self.color_scheme = self.ColorScheme()

        # set up screens
        self.select_dimensions_screen = GraphicalInterface.SelectDimensionsScreen(self)
        self.running_screen = GraphicalInterface.RunningScreen(self)
        self.paused_screen = GraphicalInterface.PausedScreen(self)

        # start on the select dimensions screen by default
        self.current_screen = self.running_screen # TEMPORARY ONLY

        @self.window.event
        def on_draw():
            self.window.clear()
            self.update_display()
        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            self.current_screen.handle_mouse_press(x, y, button, modifiers)
            self.update_display()
        @self.window.event
        def on_key_press(symbol, modifiers):
            self.current_screen.handle_key_press(symbol, modifiers)
            self.update_display()
        @self.window.event
        def on_text(text):
            self.current_screen.handle_text(text)
            self.update_display()
        @self.window.event
        def on_resize(width, height):
            # recalculate grid dimensions based on new window size
            self.grid_dimensions = self.GridDimensions(self.game.rows, self.game.cols, width, height)
            self.update_display()
    
    def setup(self):
        if self.game == None:
            self.game = Game()
        self.game.run()
        # TEMPORARY ONLY
        self.game.process_input(Commands.INIT_GRID, 3, 6)
    
    def run(self):
        self.window.push_handlers(self)
        pyglet.app.run()
    
    def update_display(self):
        self.window.clear()
        self.current_screen.update()
