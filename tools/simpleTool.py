"""
Example of a simple tool.

Doesn't do more then drawing an oval on the mouse down position.

"""
from mojo.events import BaseEventTool, installTool
from mojo.drawingTools import *

class MyTool(BaseEventTool):
    
    def setup(self):
        self.position = None
    
    def mouseDown(self, point, clickCount):
        self.position = point
    
    def mouseDragged(self, point, delta):
        self.position = point
    
    def mouseUp(self, point):
        self.position = None
    
    def draw(self, scale):
        if self.position is not None:
            size = 10
            x = self.position.x - size
            y = self.position.y - size
            fill(None)
            stroke(1, 0, 0)
            oval(x, y, size*2, size*2)
    
    def getToolbarTip(self):
        return "My Tool Tip"
    
    

installTool(MyTool())