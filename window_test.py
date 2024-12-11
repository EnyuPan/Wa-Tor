import pyglet
from pyglet import window, app, graphics, shapes
w = window.Window()

batch = graphics.Batch()
rectangle = shapes.Rectangle(0, 10, 100, 100, color=(0, 255, 0), batch=batch)

@w.event
def on_draw():
    w.clear()
    batch.draw()

app.run()
