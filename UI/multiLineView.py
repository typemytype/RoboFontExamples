from mojo.UI import MultiLineView
from vanilla import *
    
class SampleMultiLineView:

    def __init__(self, font):

        self.w = Window((600, 400), minSize=(300, 300))

        self.w.lineView = MultiLineView((0, 0, -0, -0), pointSize=30, selectionCallback=self.lineViewSelectionCallback)
        self.w.lineView.setFont(font)

        glyphs = []
        for glyphName in font.glyphOrder:
            glyphs.append(font[glyphName])

        self.w.lineView.set(glyphs)

        self.w.open()
    
    def lineViewSelectionCallback(self, sender):
        print sender.getSelectedGlyph()

SampleMultiLineView(CurrentFont())