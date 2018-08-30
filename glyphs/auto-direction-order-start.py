# auto contour direction + order + starting point

f = CurrentFont()

for glyph_name in f.selection:
    glyph = f[glyph_name]
    glyph.correctDirection()
    glyph.autoContourOrder()
    for contour in glyph:
        contour.autoStartSegment()
