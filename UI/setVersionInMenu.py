import AppKit
from mojo.roboFont import version

 
if version < "2":
    menu = AppKit.NSApp().mainMenu()
    roboFontItem = menu.itemWithTitle_("RoboFont")
    if roboFontItem:
        txt = "RoboFont %s" % version
        attrTxt = AppKit.NSAttributedString.alloc().initWithString_attributes_(txt, {AppKit.NSFontAttributeName: AppKit.NSFont.menuBarFontOfSize_(0)})
        roboFontItem.setAttributedTitle_(attrTxt)
        roboFontItem.submenu().setTitle_(txt)