from AppKit import NSDragOperationMove
from vanilla import *

from fontTools.pens.cocoaPen import CocoaPen

from defconAppKit.windows.baseWindow import BaseWindowController

from lib.tools.misc import randomColor
from lib.cells.colorCell import RFColorCell

from mojo.drawingTools import *
from mojo.events import addObserver, removeObserver
from mojo.UI import UpdateCurrentGlyphView

contourReoderPboardType = "contourReoderPboardType"

class ContourReorder(BaseWindowController):

    def __init__(self, glyph):
        self.w = FloatingWindow((230, 300), "Contour Reorder", minSize=(200, 250))

        columnDescriptions = [
                    # dict(title="contour", width=170),
                    dict(title="index"),
                    dict(title="", key="color", cell=RFColorCell.alloc().init(), width=60)
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
        items = []
        if glyph is not None:
            self._glyph = glyph.naked()
        
            if self._glyph:
                items = [dict(contour=contour, index=i, color=randomColor(asNSColor=True, dept=len(glyph), order=i))
                        for i, contour in enumerate(self._glyph)]
        self.w.contours.set(items)

        
    def dropListSelfCallback(self, sender, dropInfo):
        isProposal = dropInfo["isProposal"]

        if not isProposal:
            indexes = [int(i) for i in sorted(dropInfo["data"])]
            indexes.sort()
            source = dropInfo["source"]
            rowIndex = dropInfo["rowIndex"]

            items = sender.get()
            changeLists = [items]
            changedGlyphs = dict()
            
            for layerName in self._glyph.font.layers.layerOrder:
                glyphs = list(self._glyph.getLayerGlyph(layerName)) 
                changeLists.append(glyphs)
                changedGlyphs[layerName] = glyphs
            
            for changeList in changeLists:
                toMove = [changeList[index] for index in indexes]
            
                for index in reversed(indexes):
                    del changeList[index]
                        
                rowIndex -= len([index for index in indexes if index < rowIndex])
                for font in toMove:
                    changeList.insert(rowIndex, font)
                    rowIndex += 1
                                    
            for layerName, contours in changedGlyphs.items():
                g = self._glyph.getLayerGlyph(layerName)
                print(contours)
                g.prepareUndo("Reorder Contours")
                g.clearContours()
                for contour in contours:
                    g.appendContour(contour)

                g.performUndo()
            
                        
            for item in items:
                c = item["contour"]
                item["index"] =  self._glyph.contourIndex(c)
            sender.set(items)
            
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