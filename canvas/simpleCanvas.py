from mojo.canvas import Canvas
from mojo.drawingTools import *
from vanilla import *

class ExampleWindow:

    def __init__(self):
        self.size = 50

        self.w = Window((400, 400), minSize=(200, 200))
        self.w.slider = Slider((10, 5, -10, 22),
                          value=self.size,
                          callback=self.sliderCallback)
        self.w.canvas = Canvas((0, 30, -0, -0), delegate=self)
        self.w.open()

    def sliderCallback(self, sender):
        self.size = sender.get()
        self.w.canvas.update()

    def draw(self):
        rect(10, 10, self.size, self.size)

ExampleWindow()