"""
An example script of adding an observers and do *something*

It draws a simple unicode reference of an existing installed font.
"""

from mojo.events import addObserver
from mojo.drawingTools import *

from lib.tools.misc import unicodeToChar


class DrawReferenceGlyph(object):

    def __init__(self):
        addObserver(self, "drawReferenceGlyph", "draw")

    def drawReferenceGlyph(self, info):
        glyph = info["glyph"]
        scaleValue = info["scale"]
        r = 0
        g = 0
        b = 0
        a = .5

        if glyph is not None and glyph.unicode is not None:
            t = unicodeToChar(glyph.unicode)
            save()
            translate(glyph.width + 10, 10)
            scale(scaleValue)
            font("Georgia", 20)
            stroke(None)
            fill(r, g, b, a)
            text(t, (0, 0))
            restore()


DrawReferenceGlyph()
