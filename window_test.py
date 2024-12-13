import pyglet
from pyglet import window, app, graphics, shapes
import random
w = window.Window()

b = graphics.Batch()

rows = 10
cols = 10
cells = [None] * rows * cols
cell_width = w.width / rows
cell_height = w.height / cols
print(cell_width, cell_height)
for i in range(rows):
    for j in range(cols):
        cells[i * rows + j] = shapes.Rectangle(i * cell_width, j * cell_height, cell_width, cell_height, color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), batch=b)

@w.event
def on_draw():
    b.draw()

app.run()
