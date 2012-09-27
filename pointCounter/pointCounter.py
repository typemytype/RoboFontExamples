from mojo.events import addObserver
from mojo.drawingTools import *

class PointCount(object):
    
    def __init__(self):
        addObserver(self, "drawPointCount", "draw")
    
    def drawPointCount(self, info):
        glyph = info["glyph"]
        if glyph is None:
            return
        scale = info["scale"]
                
        pointCount = 0
        for contour in glyph:
            pointCount += len(contour)
        
        selectedCount = len(glyph.selection)
        
        fill(1, 0, 0)
        stroke(None)
        fontSize(10/scale)
        text("points: %s | selected: %s" %(pointCount, selectedCount), (glyph.width+10, 10))
    
    
PointCount()
             
        