from robofab.interface.all.dialogs import Message
 
#  settings 

interpolationSteps = 5
extrapolateSteps = 2

startColor = 40
endColor = 60


# get the currentFont
f = CurrentFont()

if f is None:
    # no font open
    Message("Oeps", informativeText="There is not font open.")
else:
    # get the selection
    selection = f.selection
    # check if the selection has only two glyphs selected
    if len(selection) != 2:
        Message("Incompatible selection", informativeText="Two compatible glyphs are required.")
    else:	
        # get the first master glyphs
        source1 = f[selection[0]]
        source2 = f[selection[1]]
        
        # check if they are compatible
        if not source1.isCompatible(source2, False):
            # the glyphs are not compatible
            Message("Incompatible masters", informativeText="Glyph %s and %s are not compatible." %(source1.name, source2.name))
        else:
            # loop over the amount of required interplations
            nameSteps = 0
            for i in range(-extrapolateSteps, interpolationSteps+extrapolateSteps + 1, 1):
                # create a new name 
                name = "interpolation.%03i" % nameSteps
                nameSteps += 1
                # create the glyph if its not existing
                dest = f.newGlyph(name)
                # get the factor which will be value between 0 and 1
                factor = i / float(interpolationSteps)                
                # interpolate between the two master with the facto
                dest.interpolate(factor, source1, source2)
                # color the glyph based on the factor
                dest.mark = startColor + (endColor - startColor) * factor        
            f.update()
	
        
