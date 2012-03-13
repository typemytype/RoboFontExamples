## use BasePen as base class
from fontTools.pens.basePen import BasePen

class RemoveOffcurvesPen(BasePen):
    """
    A simple pen drawing a contour without any offcurves.
    """
    def __init__(self, glyphSet):
        BasePen.__init__(self, glyphSet)
        
        self._contours = []
        self._components = []
        
    def _moveTo(self, pt):
        self._contours.append([])
        self._contours[-1].append(("moveTo", pt))        
    
    def _lineTo(self, pt):
        self._contours[-1].append(("lineTo", pt))
    
    def _curveToOne(self, pt1, pt2, pt3):
        self._contours[-1].append(("lineTo", pt3))        
    
    def qCurveTo(self, *points):
        pt = points[-1]
        self._contours[-1].append(("lineTo", pt))

    def _closePath(self):
        self._contours[-1].append(("closePath", None))
    
    def _endpath(self):
        self._contours[-1].append(("endPath", None))
    
    def addComponent(self, baseName, transformation):
        self._components.append((baseName, transformation))
    
    def draw(self, outPen):
        """
        Draw the stored instructions in an other pen.
        """
        for contour in self._contours:
            for penAttr, pt in contour:
                func = getattr(outPen, penAttr)
                if pt is None:
                    func()
                else:
                    func(pt)
        
        for baseGlyph, transformation in self._components:
            outPen.addComponent(baseGlyph, transformation)
                
        
## get the current glyph
g = CurrentGlyph()

## prepare the glyph for undo
g.prepareUndo("Remove All Offcurves")

## create a pen
pen = RemoveOffcurvesPen(g.getParent())

## draw the glyph in the pen
g.draw(pen)

## clear the glyph
g.clear()

## draw the stored contour from the pen into the emtpy glyph
pen.draw(g.getPen())

## tell the glyph undo watching is over
g.performUndo()