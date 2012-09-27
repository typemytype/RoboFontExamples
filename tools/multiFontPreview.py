import vanilla
from defconAppKit.windows.baseWindow import BaseWindowController
from defconAppKit.controls.glyphLineView import GlyphLineView
from mojo import events


class MultiFontPreview(BaseWindowController):

    def __init__(self):
        self.w = vanilla.Window((400, 400), minSize=(100, 100))
        self.w.glyphLineView = GlyphLineView((0, 0, 0, 0), pointSize=None, autohideScrollers=False, showPointSizePlacard=True)
        events.addObserver(self, "glyphChanged", "currentGlyphChanged")
        self.glyphChanged(dict(glyph=CurrentGlyph()))
        self.setUpBaseWindowBehavior()
        self.w.open()

    def windowCloseCallback(self, sender):
        events.removeObserver(self, "currentGlyphChanged")
        super(MultiFontPreview, self).windowCloseCallback(sender)

    def glyphChanged(self, info):
        glyph = CurrentGlyph()
        if glyph is None:
            glyphs = []
        else:
            glyphName = glyph.name
            glyphs = [font[glyphName].naked() for font in AllFonts() if glyphName in font]
        self.w.glyphLineView.set(glyphs)

MultiFontPreview()