from game import Game, Commands

g = Game()
g.run()
g.process_input(Commands.INIT_GRID, int(input("Enter number of rows: ")), int(input("Enter number of cols: ")))
print(g.grid)
s = ""
while g.running:
    s = input("Enter command (F: add fish, S: add shark, T: tick, R: reset, P: populate, Q: quit): ").lower()
    if s == "q":
        g.quit()
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
    print(g.grid)
