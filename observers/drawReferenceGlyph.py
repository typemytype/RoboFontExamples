"""
An example script using merz and subscriber

It draws a simple unicode reference of an existing installed font.
"""
from mojo.subscriber import Subscriber, registerGlyphEditorSubscriber


class DrawReferenceGlyph(Subscriber):

    debug = True

    def build(self):
        glyphEditor = self.getGlyphEditor()
        self.container = glyphEditor.extensionContainer(
            identifier="com.roboFont.DrawReferenceGlyph.foreground",
            location="foreground",
            clear=True)

    def started(self):
        self.textLineLayer = self.container.appendTextLineSublayer(
            pointSize=30,
            font='Georgia',
            text="",
            fillColor=(0, 0, 0, 0.4),
            horizontalAlignment="left"
        )

    def destroy(self):
        self.container.clearSublayers()

    def glyphEditorDidSetGlyph(self, info):
        glyph = info["glyph"]
        if glyph is None:
            self.textLineLayer.setText("")
            return

        txt = ""
        if glyph.unicode is not None:
            # get character for glyph
            txt = chr(glyph.unicode)
        self.textLineLayer.setPosition((glyph.width, 0))
        self.textLineLayer.setText(txt)

    def glyphEditorGlyphDidChangeMetrics(self, info):
        glyph = info["glyph"]
        if glyph is None:
            self.textLineLayer.setText("")
            return
        self.textLineLayer.setPosition((glyph.width, 0))


if __name__ == '__main__':
    registerGlyphEditorSubscriber(DrawReferenceGlyph)

