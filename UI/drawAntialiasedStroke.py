from AppKit import *
from fontTools.pens.basePen import BasePen

from mojo.events import addObserver
from lib.tools.defaults import getDefaultColor


class AntialiasCocoaPen(BasePen):
    
    """
    - create a nsBezierPath for each segment.
    - Straight lines are ignored.
    """
    
    def __init__(self, glyphSet):
        BasePen.__init__(self, glyphSet)
        self.path = NSBezierPath.bezierPath()
        self.prevPoint = None
        self.firstPoint = None
        
    def _moveTo(self, pt):
        self.firstPoint = pt
        self.prevPoint = pt
    
    def _lineTo(self, pt):
        if pt[0] != self.prevPoint[0] and pt[1] != self.prevPoint[1]:
            # only draw the antialiased line if x or y is different
            self.path.moveToPoint_(self.prevPoint)
            self.path.lineToPoint_(pt)
        self.prevPoint = pt
    
    def _curveToOne(self, pt1, pt2, pt3):
        self.path.moveToPoint_(self.prevPoint)
        self.path.curveToPoint_controlPoint1_controlPoint2_(pt3, pt1, pt2)
        self.prevPoint = pt3
    
    def closePath(self):
        if self.firstPoint != self.prevPoint:
            self._lineTo(self.firstPoint)
        self.prevPoint = None


class NiceLines(object):
    
    def __init__(self):
        ## add observer when the glyph view draws the content
        addObserver(self, "myDraw", "drawBackground")
        ## get the stroke color from the defaults
        self.strokeColor = getDefaultColor("glyphViewStrokeColor")
        
    def myDraw(self,info):
        glyph = info["glyph"]
        ## initiate the pen
        pen = AntialiasCocoaPen(glyph.getParent())
        ## draw the glyph in the pen
        glyph.draw(pen)
        ## set the stroke color
        self.strokeColor.set()
        ## set the line width of the path, the same as the scale of the glyph view
        pen.path.setLineWidth_(info["scale"])
        ## stroke the path
        pen.path.stroke()
        
## install the observer
NiceLines()