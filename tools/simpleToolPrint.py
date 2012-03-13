from mojo.events import BaseEventTool, installTool
from AppKit import *

class MyEvent(BaseEventTool):

    def becomeActive(self):
        print "active"

    def becomeInactive(self):
        print "inactive"

    def mouseDown(self, point, clickCount):
        # getGLyph returns the current glyph as robofab object
        print "mouseDown", self.getGlyph(), clickCount

    def rightMouseDown(self, point, event):
        print "rightMouseDown"

    def mouseDragged(self, point, delta):
        print "mousedragged"

    def rightMouseDragged(self, point, delta):
        print "rightMouseDragged"

    def mouseUp(self, point):
        print "mouseup"

    def keyDown(self, event):
        # a dict of all modifiers, shift, command, alt, option
        print "keyDown", self.getModifiers() 

    def keyUp(self, event):
        print "keyUp"

    def modifiersChanged(self):
        print "modifiersChanged"

    def draw(self, scale):
        print "draw", self.isDragging()
        if self.isDragging():
            ## draw a red dot when dragging
            r = 50
            NSColor.redColor().set()
            x, y = self.currentPoint
            NSBezierPath.bezierPathWithOvalInRect_(((x-r, y-r), (r*2, r*2))).fill()

    def drawBackground(self, scale):
        print "drawBackground here"

    #def getDefaultCursor(self):
    #   this will be the cursor default is an arrow
    #   return aNSCursor
    #def getToolbarIcon(self):
    #   this is setting the icon in the toolbar default is an arrow
    #   return aNSImage

    def getToolbarTip(self):
        return "My Event Tool Bar Tip"

    #notifications

    def viewDidChangeGlyph(self):
        print "view changed glyph"

    def preferencesChanged(self):
        print "prefs changed"

installTool(MyEvent())