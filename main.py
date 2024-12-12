import creature, grid

g = grid.Grid(9, 9)
c = g.set_cell(6, 0, None)
print(c)
f = creature.Fish(c, 5)
g.set_cell(6, 0, f)
print(c)
c.remove_creature()
print(c)

print("\nCell::get_neighbors() and Grid::set_cell()")
print(c.get_neighbors())
print(g.get_neighbors(6, 0))
g.set_cell(5, 0, " fIsh")
g.set_cell(7, 0, creature.Shark(g.get_cell(7, 0), 8))
print(g.get_neighbors(6, 0))

print("\nCreature::die()")
s2 = creature.Shark(g.get_cell(6, 1), 5, 5)
g.set_cell(6, 1, s2)
print(g)
print(g.get_neighbors(7, 1))
s2.die()
print(g.get_neighbors(7, 1))

print("\nFish::move()")
f2 = creature.Fish(g.get_cell(3, 2), 2)
g.set_cell(3, 2, f2)
g.set_cell(3, 1, "shark")
print(g.get_neighbors(3, 2))
print(g)
f2.move()
print(g.get_neighbors(3, 2))
print(g)

print("\nShark::move()")
f3 = creature.Fish(g.get_cell(7, 1))
g.set_cell(7, 1, f3)
print(g)
g.cells[7][0].creature.move()
print(g)
print(f3.cell)
print(g.get_cell(7, 1))
g.cells[7][1].creature.move()
print(g)

print("\nGrid::tick()")
g2 = grid.Grid(10, 15)
for i, j in [[4, 2], [6, 1], [8, 1], [7, 0], [8, 0], [9, 5], [4, 13], [1, 13], [4, 12]]:
    g2.set_cell(i, j, "fish")
for i, j in [[3, 5], [6, 0], [8, 4], [5, 3], [4, 12]]:
    g2.set_cell(i, j, "shark")
print(g2)
for i in range(10):
    g2.tick()
    print(g2)
g2.reset()
print(g2)

# Testing harness
print("Enter testing harness...initializing test grid")
grd = grid.Grid(int(input("Enter number of rows: ")), int(input("Enter number of cols: ")))
print(grd)
s = ""
while s != "q":
    s = input("Enter command (F: add fish, S: add shark, T: tick, R: reset, P: populate, Q: quit): ").lower()
    if s == "f":
        grd.set_cell(int(input("row: ")), int(input("col: ")), "fish")
    if s == "s":
        grd.set_cell(int(input("row: ")), int(input("col: ")), "shark")
    if s == "r":
        grd.reset()
    if s == "t":
        grd.tick()
    if s == "p":
        grd.populate(int(input("number of fish: ")), int(input("number of sharks: ")))
    print(grd)
