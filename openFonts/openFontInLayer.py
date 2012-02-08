"""
Import a font into a layer of the CurrentFont
"""

## open a font without UI
f = OpenFont(showUI=False)

## get the current font
cf = CurrentFont()

## create a layer name based on the familyName and styleName of the opend font
layerName = "%s_%s" %(f.info.familyName, f.info.styleName)

## loop over all glyphs in the font
for g in f:
    ## if the glyph doenst exist in the current font, create a new glyph
    if g.name not in cf:
        cf.newGlyph(g.name)
    ## get the layered glyph
    layerGLyph = cf[g.name].getLayer(layerName)
    
    ## get the point pen of the layered glyph
    pen = layerGLyph.getPointPen()
    ## draw the points of the imported glyph into the layerd glyph
    g.drawPoints(pen)

## we are done :)
print "done"
    


