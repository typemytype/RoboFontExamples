from vanilla import *

from defconAppKit.windows.baseWindow import BaseWindowController

from mojo.glyphPreview import GlyphPreview
from mojo.events import addObserver, removeObserver

from mojo.roboFont import CurrentGlyph

class StencilPreview(BaseWindowController):
    
    def __init__(self):
        self.glyph = CurrentGlyph()
        # create a window        
        self.w = FloatingWindow((400, 400), "Stencil Preview", minSize=(200, 200))
        # add the preview to the window
        self.w.preview = GlyphPreview((0, 0, -0, -0))
        # add an observer to get callbacks when a glyph changes in the glyph view
        addObserver(self, "viewDidChangeGlyph", "viewDidChangeGlyph")
        # open the window
        self.updateGlyph()
        self.w.open()
    
    def viewDidChangeGlyph(self, notification):
        # notification when the glyph changes in the glyph view
        glyph = CurrentGlyph()
        self.unsubscribeGlyph()
        self.subscribeGlyph(glyph)
        self.updateGlyph()
        
    def glyphChanged(self, notification):
        self.updateGlyph()        
        
    def updateGlyph(self):
        glyph = self.glyph
        # if the glyph is None just set None to the preview
        if glyph is None:
            self.w.preview.setGlyph(None)
            return
        # get the foreground layer
        foreground = glyph.getLayer("foreground")
        # get the background layer
        background = glyph.getLayer("background")
        
        # get the substract the background from the foreground layer
        result = foreground % background
        # set the result in the preview view
        self.w.preview.setGlyph(result)
    
    def subscribeGlyph(self, glyph):
        # subscribe the glyph
        self.glyph = glyph
        # add an observer to glyph data changes 
        self.glyph.addObserver(self, "glyphChanged", "Glyph.Changed")
        
    def unsubscribeGlyph(self):
        # unsubscribe the glyph
        if self.glyph is None:
            return
        # remove this observer for the glyph
        self.glyph.removeObserver(self, "Glyph.Changed")
    
    def windowCloseCallback(self, sender):
        # notification when the window get closed
        # remove the view did change glyph in the glyph view observer
        removeObserver(self, "viewDidChangeGlyph")
        # unsubscribe the glyph
        self.unsubscribeGlyph()
        super(StencilPreview, self).windowCloseCallback(sender)

# open the window
OpenWindow(StencilPreview)
        
        
