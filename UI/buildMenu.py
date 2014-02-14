from AppKit import *
from vanilla.vanillaBase import VanillaCallbackWrapper

class BuildMenu(object):
    
    def __init__(self):
        
        myMenuTitle = "TypeMedia Awsome scripts"
        
        # create a new menu
        myMenu = NSMenu.alloc().initWithTitle_(myMenuTitle)
        # create a new item
        item = myMenu.addItemWithTitle_action_keyEquivalent_("do it", "action:", "m")
        # create a callback
        self.callbackwrapper = VanillaCallbackWrapper(self.doIt)
        # set the callback
        item.setTarget_(self.callbackwrapper)
        # setting modifiermaks
        item.setKeyEquivalentModifierMask_(NSControlKeyMask | NSCommandKeyMask)
        
        
        # ask the main menu
        menu = NSApp().mainMenu()
        # add item
        newItem = menu.addItemWithTitle_action_keyEquivalent_(myMenuTitle, "", "")
        # set submenu
        newItem.setSubmenu_(myMenu)
    
    
    def doIt(self, sender):
        print "hello"
        
BuildMenu()