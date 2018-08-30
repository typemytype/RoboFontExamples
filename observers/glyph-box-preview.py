# observer test

from mojo.events import addObserver, removeObserver
from mojo.drawingTools import *


class GlyphBoxPreview(object):

    def __init__(self):
        addObserver(self, "drawBox", "drawPreview")

    def drawBox(self, info):
        glyph = info["glyph"]
        stroke(None)
        r, g, b, a = 0, 1, 1, .5
        fill(r, g, b, a)
        if glyph is not None:
            xmin, ymin, xmax, ymax = glyph.box
            x, y = xmin, ymin
            w, h = xmax - xmin, ymax - ymin
            rect(x, y, w, h)

P = GlyphBoxPreview()

# removeObserver("GlyphBoxPreview", "drawPreview")
# removeObserver(GlyphBoxPreview, "drawPreview")
# removeObserver(P, "drawPreview")
