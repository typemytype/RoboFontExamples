from mojo.events import addObserver
from mojo.drawingTools import *
from math import hypot

from AppKit import *

class PointDistanceController(object):
    
    def __init__(self):
        # subscribe to the draw event
        addObserver(self, "draw", "draw")
        addObserver(self, "draw", "drawBackground")
        # create a background color
        self.backgroundColor = NSColor.redColor()
        # create a background stroke color
        self.backgroundStrokeColor = NSColor.whiteColor()
        # create a stroke color
        self.strokeColor = NSColor.redColor()
        # setting text attributes
        self.attributes = attributes = {
            NSFontAttributeName : NSFont.boldSystemFontOfSize_(9),
            NSForegroundColorAttributeName : NSColor.whiteColor(),
            }
    
    def draw(self, notification):
        # get the glyph from the notification
        glyph = notification["glyph"]
        # get the selection
        selection = glyph.selection
        # check if the selection is more then 1 and less then 6
        if 2 <= len(selection) <= 5:
            # get the view
            view = notification["view"]
            # get the scale of the view
            scale = notification["scale"] 
            distances = []
            done = []
            # create a path to draw in
            path = NSBezierPath.bezierPath()
            # loop over all the points in the selection
            for p in selection:
                # loope in a the loop again over all the points in the selection
                for p2 in selection:
                    # check if the point is not the same
                    if p == p2:
                        continue
                    # check if we already handled the point
                    if (p, p2) in done:
                        continue
                    if (p2, p) in done:
                        continue
                    # add a line to the path
                    path.moveToPoint_((p.x, p.y))
                    path.lineToPoint_((p2.x, p2.y))
                    # calculate the center point
                    cx = p.x + (p2.x - p.x) * .5
                    cy = p.y + (p2.y - p.y) * .5
                    # calculate the distance
                    dist = hypot(p2.x - p.x, p2.y - p.y)
                    # store the distance and the center point
                    distances.append((cx, cy, dist))
                    # store the points 
                    done.append((p, p2))
            # set the stroke color
            self.strokeColor.set()
            # set the line width of the path
            path.setLineWidth_(scale)
            # stroke the path
            path.stroke()
            
            for x, y, dist in distances:
                # draw the distance as text at the center point
                # this will change to a public callback in the next update (RF 1.5.2)
                if dist.is_integer():
                    t = "%i"
                else:
                    t = "%.2f"
                view._drawTextAtPoint(t % dist, self.attributes, (x, y), drawBackground=True, backgroundColor=self.backgroundColor, backgroundStrokeColor=self.backgroundStrokeColor)

PointDistanceController()