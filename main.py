import grid

grd = grid.Grid(int(input("Enter number of rows: ")), int(input("Enter number of cols: ")))
print(grd)
s = ""
while s != "q":
    s = input("Enter command (F: add fish, S: add shark, T: tick, R: reset, P: populate, Q: quit): ").lower()
    if s == "f":
        grd.set_cell(int(input("row: ")), int(input("col: ")), "fish")
    elif s == "s":
        grd.set_cell(int(input("row: ")), int(input("col: ")), "shark")
    elif s == "r":
        grd.reset()
    elif s == "t":
        grd.tick()
    elif s == "p":
        grd.populate(int(input("number of fish: ")), int(input("number of sharks: ")))
    print(grd)
