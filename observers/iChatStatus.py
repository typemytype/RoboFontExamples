from AppKit import NSAppleScript

from mojo.events import addObserver
from mojo.roboFont import CurrentFont, CurrentGlyph

appleScript = """tell application "iChat"
   set status message to "%s"
end tell"""


class iChatStatus:
    
    def __init__(self):
        addObserver(self, "updateStatus", "currentGlyphChanged")
        addObserver(self, "updateStatus", "fontBecameCurrent")
    
    def updateStatus(self, info):  
        
        glyph = CurrentGlyph()
        
        if glyph is None:
            font = CurrentFont()
            if font is None:
                message = "Im just looking around"
            else:
                m = self.parseFontInfo(font)
                message = "Im working on my %s in RoboFont" % m
        else:
            font = glyph.getParent()
            m = self.parseFontInfo(font)
            message = "Im drawing glyph %s for %s in RoboFont" % (glyph.name, m)
        
        cmd = NSAppleScript.alloc().initWithSource_(appleScript % message)
        cmd.executeAndReturnError_(None)
        
    def parseFontInfo(self, font):
        familyName = font.info.familyName
        styleName = font.info.styleName
        if familyName is None and styleName is None:
            m = "an unnamed and secret font"
        elif styleName is None:
            m = familyName
        elif familyName is None:
            m = "an unnamed and secret font but its a %s" % styleName
        else:
            m = "%s %s" %(familyName, styleName)
        
        return m
        
        
    
iChatStatus()