from mojo.events import addObserver
from mojo.drawingTools import *

from lib.tools.defaults import getDefault

class DrawVerticalMetricBox(object):
        
    def __init__(self):
        
        addObserver(self, "drawMetricsBox", "drawBackground")
        
        self.color = getDefault("glyphViewMarginColor")
        self.height = getDefault("glyphViewDefaultHeight") / 2
        self.useItalicAngle = getDefault("glyphViewShouldUseItalicAngleForDisplay")
        
        
    def drawMetricsBox(self, info):
        glyph = info["glyph"]
        if glyph is None:
            return
        font = glyph.getParent()
        if font is None:
            return
        
        descender = font.info.descender
        upm = font.info.unitsPerEm
        
        save()
        if self.useItalicAngle:
            angle = font.info.italicAngle
            if angle is not None:
                skew(-angle, 0)
        
        fill(*self.color)
        rect(0, descender, glyph.width, -self.height)
        rect(0, descender + upm, glyph.width, self.height)
        
        restore()
        

DrawVerticalMetricBox()