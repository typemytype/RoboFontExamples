from AppKit import NSDragOperationMove
from vanilla import *

from fontTools.pens.cocoaPen import CocoaPen

from defconAppKit.windows.baseWindow import BaseWindowController

from lib.tools.misc import randomColor
from lib.cells.colorCell import ColorCell

from mojo.drawingTools import *
from mojo.events import addObserver, removeObserver
from mojo.UI import UpdateCurrentGlyphView

contourReoderPboardType = "contourReoderPboardType"

class ContourReorder(BaseWindowController):
    
    def __init__(self, glyph):
        self.w = FloatingWindow((230, 300), "Contour Reorder", minSize=(200, 250))
        
        columnDescriptions = [
                    dict(title="contour", width=170), 
                    dict(title="", key="color", cell=ColorCell.alloc().init(), width=60)
                    ]
                
        self.w.contours = List((0, 0, -0, -0), [], columnDescriptions=columnDescriptions,
                            allowsEmptySelection=False, 
                            allowsMultipleSelection=False,
                            enableDelete=True,
                            dragSettings=dict(type=contourReoderPboardType, 
                                              callback=self.dragCallback),
                            selfDropSettings=dict(type=contourReoderPboardType, 
                                                  operation=NSDragOperationMove, 
                                                  callback=self.dropListSelfCallback)
                            )
        
        addObserver(self, "drawBackground", "drawBackground")
        addObserver(self, "currentGlyphChanged", "currentGlyphChanged")
        
        self.setUpBaseWindowBehavior()
        self.setGlyph(glyph)
        UpdateCurrentGlyphView()
        self.w.open()
    
    def setGlyph(self, glyph):
        self._glyph = glyph
        items = [dict(contour=contour, color=randomColor(asNSColor=True, dept=len(glyph), order=i)) 
                        for i, contour in enumerate(glyph)]
        self.w.contours.set(items)
    
    def reorderGlyph(self):
        contours = [item["contour"] for item in self.w.contours.get()]
        
        self._glyph.prepareUndo("Reoder Contours")
        self._glyph.clearContours()
        for contour in contours:
            self._glyph.appendContour(contour)
        
        self._glyph.performUndo()
                    
    def dropListSelfCallback(self, sender, dropInfo):
        isProposal = dropInfo["isProposal"]
        
        if not isProposal:
            indexes = [int(i) for i in sorted(dropInfo["data"])]
            indexes.sort()
            source = dropInfo["source"]
            rowIndex = dropInfo["rowIndex"]

            items = sender.get()

            toMove = [items[index] for index in indexes]

            for index in reversed(indexes):
                del items[index]

            rowIndex -= len([index for index in indexes if index < rowIndex])
            for font in toMove:
                items.insert(rowIndex, font)
                rowIndex += 1

            sender.set(items)
            self.reorderGlyph()
        return True    
        
    def dragCallback(self, sender, indexes):
        return indexes
    
    def drawBackground(self, info):
        scale = info["scale"]
        for item in self.w.contours:
            contour = item["contour"]
            pen = CocoaPen(None)
            contour.draw(pen)
            item["color"].set()
            pen.path.setLineWidth_(10*scale)
            pen.path.stroke()
    
    def currentGlyphChanged(self, info):
        self.setGlyph(CurrentGlyph())
    
    def windowCloseCallback(self, sender):
        removeObserver(self, "drawBackground")
        removeObserver(self, "currentGlyphChanged")
        UpdateCurrentGlyphView()
        super(ContourReorder, self).windowCloseCallback(sender)
        
ContourReorder(CurrentGlyph())
        
        
        