from mojo.events import EditingTool, installTool
from mojo.drawingTools import *

from fontTools.pens.cocoaPen import CocoaPen

class PolygonSelectionTool(EditingTool):
    
    def setup(self):
        self.pen = None
        self._oldPen = None
        
    def mouseDown(self, point, clickCount):
        if self.selection.hasSelection():
            return
        if not self.optionDown:
            self.pen = CocoaPen(None)
        else:
            self.pen = self._oldPen
        self.pen.moveTo((point.x, point.y))
    
    def mouseDragged(self, point, delta):
        if self.pen is None:
            return
        self.pen.lineTo((point.x, point.y))
    
    def mouseUp(self, point):
        if self.pen is None:
            return
        self.pen.closePath()
        
        glyph = self.getGlyph()
        path = self.pen.path
        for contour in glyph:
            for point in contour.points:
                result = path.containsPoint_((point.x, point.y))
                if self.controlDown:
                    point.selected = not result
                else:
                    point.selected = result
        
        self._oldPen = self.pen
        self.pen = None
        
    def draw(self, scale):
        if self.pen is None:
            return
        fill(0, .1)
        stroke(0, .6)
        strokeWidth(scale)
        drawPath(self.pen.path)
    
    def canSelectWithMarque(self):
        return False
    
    def getToolbarTip(self):
        return "Polygon Selection Tool"
        
    
installTool(PolygonSelectionTool())