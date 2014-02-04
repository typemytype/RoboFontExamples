import vanilla
from defconAppKit.windows.baseWindow import BaseWindowController

from mojo.events import addObserver, removeObserver
from mojo.drawingTools import *

class SimpleWindowObserver(BaseWindowController):
    
    def __init__(self):
        # create a window        
        self.w = vanilla.Window((300, 45), "Simple Observer")
        # add a button with a title and a callback
        self.w.startStopButton = vanilla.Button((10, 10, -10, 22), "Start", callback=self.startStopButtonCallback)
        # setup basic windwo behavoir (this is an method from the BaseWindowController)
        self.setUpBaseWindowBehavior()
        # open the window
        self.w.open()
    
    
    def startStopButtonCallback(self, sender):
        # button callback, check the title
        if sender.getTitle() == "Start":
            # set "Stop" as title for the button
            sender.setTitle("Stop")
            # add an observer
            addObserver(self, "draw", "draw")
        else:
            # set "Start" as title for the button
            sender.setTitle("Start")
            # remove the observser
            removeObserver(self, "draw")            
    
    def draw(self, notification):
        # get the glyph
        glyph = notification["glyph"]
        # save the state of the canvas
        save()
        # translate the canvase
        translate(glyph.width * 2, 0)
        # scale (flip) the canvas
        scale(-1, 1)
        # set a fill color
        fill(0)
        # draw the glyph
        drawGlyph(glyph)
        # restore the canvas
        restore()
        
    def windowCloseCallback(self, sender):
        # this receives a notification whenever the window is closed
        # remove the observer
        removeObserver(self, "draw")
        # and send the notification to the super
        super(SimpleWindowObserver, self).windowCloseCallback(sender)
    
SimpleWindowObserver()
    


