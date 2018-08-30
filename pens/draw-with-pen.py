# pen example: drawing inside a glyph!

from random import randint

f = CurrentFont()

for g in f:
    g.clear()
    pen = g.getPen()
    pen.moveTo((0, -200))
    pen.lineTo((
        randint(0, 200),
        randint(600, 700)
    ))
    pen.lineTo((800, 800))
    # draw an open path
    # pen.endPath()
    # *or* auto-close path
    pen.closePath()
