import creature, grid

g = grid.Grid(9, 9)
c = g.set_cell(6, 0, None)
print(c)
f = creature.Fish(c, 5)
g.set_cell(6, 0, f)
print(c)
c.remove_creature()
print(c)
print(c.get_neighbors())
print(g.get_neighbors(6, 0))
#TODO: for grid::set_cell(), make it easier to specify which creature to set the cell to,
# without having to create an object then pass it into set_cell()
g.set_cell(5, 0, creature.Fish(g.get_cell(5, 0)))
g.set_cell(7, 0, creature.Shark(g.get_cell(7, 0), 8))
print(g.get_neighbors(6, 0))