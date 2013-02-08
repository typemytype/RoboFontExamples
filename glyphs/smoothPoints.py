# get the current glyph
g = CurrentGlyph()

# start an undo recorder
g.prepareUndo("Smooth points")

# loop over all contours
for c in g:
    # loop over all points
    for p in c.points:
        # if the point is in oncurve
        if p.type:
            # set the smooth to False and selecte the point
            p.smooth = False
            p.selected = True

# toggle smoothness
g.naked().selection.toggleSmoothness()
# update the glyph
g.update()
# set an undo
g.performUndo()