from mojo.UI import OpenGlyphWindow

g = CurrentGlyph()
if g is not None:
    OpenGlyphWindow(g, newWindow=True)