import AppKit
from mojo.roboFont import version


app = AppKit.NSApp()
menu = app.mainMenu()
roboFontItem = menu.itemArray()[0]

txt = "RoboFont %s" % version
attrTxt = AppKit.NSAttributedString.alloc().initWithString_attributes_(txt, {AppKit.NSFontAttributeName: AppKit.NSFont.menuBarFontOfSize_(0)})
roboFontItem.setAttributedTitle_(attrTxt)
roboFontItem.submenu().setTitle_(txt)


icon = app.applicationIconImage()
# get the size
w, h = icon.size()

# make a rect with the size of the image
imageRect = AppKit.NSMakeRect(0, 0, w, h)
# create a new image with the same size
new = AppKit.NSImage.alloc().initWithSize_((w, h))
# lock focus on the image to draw in
new.lockFocus()
# draw the original iamge
icon.drawInRect_(imageRect)
# draw the version number
txt = AppKit.NSString.stringWithString_(str(version))

shadow = AppKit.NSShadow.alloc().init()
shadow.setShadowOffset_((-50, -50))
shadow.setShadowColor_(AppKit.NSColor.magentaColor())
shadow.setShadowBlurRadius_(2)

textSize = 200 * (w / 512)

txt.drawAtPoint_withAttributes_((0, 0), {
    AppKit.NSFontAttributeName: AppKit.NSFont.boldSystemFontOfSize_(textSize),
    AppKit.NSStrokeColorAttributeName: AppKit.NSColor.magentaColor(),
    AppKit.NSStrokeWidthAttributeName: 20
})

txt.drawAtPoint_withAttributes_((0, 0), {
    AppKit.NSFontAttributeName: AppKit.NSFont.boldSystemFontOfSize_(textSize),
    AppKit.NSShadowAttributeName: shadow,
    AppKit.NSForegroundColorAttributeName: AppKit.NSColor.whiteColor()
})


# un lock the image, drawing is done
new.unlockFocus()
# set the image as the application icon
app.setApplicationIconImage_(new)