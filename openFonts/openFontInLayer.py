f = OpenFont(showUI=False)

cf = CurrentFont()

layerName = "%s_%s" %(f.info.familyName, f.info.styleName)

for g in f:
    if g.name not in cf:
        cf.newGlyph(g.name)
    
    layerGLyph = cf[g.name].getLayer(layerName)
    
    pen = layerGLyph.getPointPen()
    g.drawPoints(pen)
    
print "done"
    


