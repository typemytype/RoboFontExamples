from vanilla import Window
from mojo.glyphPreview import GlyphPreview
from mojo.events import addObserver, removeObserver
from mojo.roboFont import OpenWindow

class Preview:

    def __init__(self):
        ## create a window
        self.w = Window((400, 400), "Preview", minSize=(100, 100))

        ## add a GlyphPreview to the window
        self.w.preview = GlyphPreview((0, 0, -0, -0))

        ## set the currentGlyph
        self.setGlyph(CurrentGlyph())

        ## add an observer when the glyph changed in the glyph view
        addObserver(self, "_currentGlyphChanged", "currentGlyphChanged")

        ## bind a windows close callback to this object
        self.w.bind("close", self.windowClose)
        ## open the window
        self.w.open()

    def _currentGlyphChanged(self, info):
        ## notification callback when the glyph changed in the glyph view
        ## just set the new glyph in the glyph preview
        self.setGlyph(CurrentGlyph())

    def setGlyph(self, glyph):
        ## setting the glyph in the glyph Preview
        self.w.preview.setGlyph(glyph)

    def windowClose(self, sender):
        ## remove the observer if the window closes
        removeObserver(self, "_currentGlyphChanged")


## open the window with OpenWindow, so it can not be open twice
OpenWindow(Preview)