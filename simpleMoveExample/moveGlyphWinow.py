from vanilla import *

class MoveGlyphWindow:
    def __init__(self, glyph):
        if glyph is None:
            print "There should be a glyph window selected!!"
            return
        self.glyph = glyph

        self.moveX = 0
        self.moveY = 0

        self.w = Window((200, 60), "Move %s" %self.glyph.name)

        self.w.hs = Slider((10, 10, -10, 22), value=0,
                                        maxValue=200,
                                        minValue=-200,
                                        callback=self.adjust)

        self.w.vs = Slider((10, 30, -10, 22), value=0,
                                        maxValue=200,
                                        minValue=-200,
                                        callback=self.adjust)

        self.w.open()

    def adjust(self, sender):
        hValue = self.w.hs.get()
        vValue = self.w.vs.get()

        x = self.moveX - hValue
        y = self.moveY - vValue

        self.moveX = hValue
        self.moveY = vValue

        self.glyph.move((x, y))

OpenWindow(MoveGlyphWindow, CurrentGlyph())