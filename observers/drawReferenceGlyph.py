"""
An example script using merz and subscriber

It draws a simple unicode reference of an existing installed font.
"""
from mojo.subscriber import Subscriber, registerGlyphEditorSubscriber


class ReferenceGlyph(Subscriber):

    debug = True

    def build(self):
        glyphEditor = self.getGlyphEditor()
        self.container = glyphEditor.extensionContainer(
            identifier="com.typemytype.unicodePreview",
            location="background",
            clear=True)

        self.unicodeText = self.container.appendTextLineSublayer(
            fillColor=(0, 0, 0, .5),
            offset=(10, 0),
            font="Georgia",
            pointSize=30,
            verticalAlignment="top"
        )

    def glyphEditorDidSetGlyph(self, info):
        glyph = info["glyph"]
        text = ""
        if glyph.unicode:
            text = chr(glyph.unicode)
        self.unicodeText.setText(text)
        self.unicodeText.setPosition((glyph.width, 0))

    def glyphEditorGlyphDidChangeMetrics(self, info):
        glyph = info["glyph"]
        self.unicodeText.setPosition((glyph.width, 0))


registerGlyphEditorSubscriber(ReferenceGlyph)
