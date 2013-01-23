from vanilla import *
from defconAppKit.windows.baseWindow import BaseWindowController

from mojo.events import addObserver, removeObserver
from mojo.UI import UpdateCurrentGlyphView
from mojo.drawingTools import *

class GlobalMaks(BaseWindowController):
    
    def __init__(self, font):
        # create a window
        self.w = Window((170, 300), "The Mask", minSize=(170, 100))
        # add a UI list
        self.w.list = List((0, 0, -0, -0), [], selectionCallback=self.listSelectionCallback)
        
        # set the font 
        self.setFont(font)
        
        # add observers needed
        addObserver(self, "drawBackground", "drawBackground")
        addObserver(self, "drawBackground", "drawInactive")
        addObserver(self, "fontBecameCurrent", "fontBecameCurrent")
        addObserver(self, "fontResignCurrent", "fontResignCurrent")
        
        self.setUpBaseWindowBehavior()
        self.w.open()
    
    def setFont(self, font):
        # set all the possible glyph of the font in the UI list
        self._font = font
        self._glyphs = []
        glyphs = []
        if font is not None:
            glyphs = font.glyphOrder
        
        self.w.list.set(glyphs)
            
    # ui callbacks
    
    def listSelectionCallback(self, sender):
        # called when an item is selected in the UI list
        sel = sender.getSelection()
        self._glyphs = []
        for i in sel:
            glyphName = sender[i]
            self._glyphs.append(self._font[glyphName])
        self.updateGlyphView()
        
    def updateGlyphView(self):
        # update the current glyph view
        UpdateCurrentGlyphView()
            
    
    # notifications
    
    def fontBecameCurrent(self, notification):
        # called when a font became the current font
        font = notification["font"]
        # set the font
        self.setFont(font)
        # update the glyph view
        self.updateGlyphView()
        
    def fontResignCurrent(self, notification):
        # called when a font resigns being the current font
        self.setFont(None)
        self.updateGlyphView()
    
    def drawBackground(self, notification):
        # draw the glyph in the background of the glyph view
        if not self._glyphs:
            return
        
        stroke(1, 0, 0)
        strokeWidth(notification["scale"])
        fill(None)
        for glyph in self._glyphs:
            drawGlyph(glyph)
    
    def windowCloseCallback(self, sender):
        # when the windows closes remove all the added observers
        removeObserver(self, "drawBackground")
        removeObserver(self,"drawInactive")
        removeObserver(self, "fontBecameCurrent")
        removeObserver(self, "fontResignCurrent")

        super(GlobalMaks, self).windowCloseCallback(sender)


# go
GlobalMaks(CurrentFont())
