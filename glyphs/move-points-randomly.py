from random import randint

f = CurrentFont()

for glyph_name in f.selection:
    for contour in f[glyph_name]:
        for point in contour.points:
            point.x += randint(-20, 20)
            point.y += randint(-20, 20)
    f[glyph_name].update()
