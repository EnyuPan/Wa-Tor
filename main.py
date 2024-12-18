from game import Game, Commands

g = Game()
g.run()
g.process_input(Commands.INIT_GRID, int(input("Enter number of rows: ")), int(input("Enter number of cols: ")))
s = ""
while g.running:
    if g.active:
        print(g.grid)
    s = input("Enter command (X: run, Z: pause, F: add fish, S: add shark, T: tick, R: reset, P: populate, Q: quit): ").lower()
    if s == "q":
        g.process_input(Commands.QUIT)
    elif s == "z":
        g.process_input(Commands.PAUSE)
    elif s == "x":
        g.process_input(Commands.RUN)
    elif s == "f":
        g.process_input(Commands.SET_CELL, int(input("row: ")), int(input("col: ")), "fish")
    elif s == "s":
        g.process_input(Commands.SET_CELL, int(input("row: ")), int(input("col: ")), "shark")
    elif s == "r":
        g.process_input(Commands.RESET_GRID)
    elif s == "t":
        g.process_input(Commands.TICK)
    elif s == "p":
        g.process_input(Commands.POPULATE, int(input("number of fish: ")), int(input("number of sharks: ")))
