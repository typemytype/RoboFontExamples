from AppKit import *
from lib.tools.misc import randomColor

# get the application icon image
icon = NSApp().applicationIconImage()
# get the size
w, h = icon.size()
# make a rect with the size of the image
imageRect = NSMakeRect(0, 0, w, h)
# create a new image with the same size
new = NSImage.alloc().initWithSize_((w, h))
# lock focus on the image to draw in 
new.lockFocus()
# draw the original iamge
icon.drawInRect_(imageRect)
# get a bright random color
randomColor(asNSColor=True).set()
# draw the color over the source 
NSRectFillUsingOperation(imageRect, NSCompositeSourceAtop)
# draw the image again
icon.drawInRect_fromRect_operation_fraction_(imageRect, imageRect, NSCompositePlusLighter, 1)
# un lock the image, drawing is done
new.unlockFocus()
# set the image as the application icon
NSApp().setApplicationIconImage_(new)