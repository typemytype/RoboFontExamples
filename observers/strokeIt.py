from AppKit import *
from vanilla import *

from defconAppKit.windows.baseWindow import BaseWindowController

from mojo.events import addObserver, removeObserver
from mojo.UI import UpdateCurrentGlyphView, CurrentSpaceCenter

class StrokeObserer(BaseWindowController):
    
    defaultColor = NSColor.colorWithCalibratedHue_saturation_brightness_alpha_(.5, .5, .5, .5)
    
    _lineCapStylesMap = dict(
        butt=NSButtLineCapStyle,
        square=NSSquareLineCapStyle,
        round=NSRoundLineCapStyle,
        )
    
    _lineJoinStylesMap = dict(   
        miter=NSMiterLineJoinStyle,
        round=NSRoundLineJoinStyle,
        bevel=NSBevelLineJoinStyle
        )
        
    def __init__(self):
        self.w = FloatingWindow((200, 130), "Stroke It")
        y = 10
        self.w.colorText = TextBox((10, y, 100, 22), "Stroke Color:")
        self.w.color = ColorWell((100, y-5, -10, 30), color=self.defaultColor, callback=self.changedCallback)
        
        y += 30
        self.w.widthText = TextBox((10, y, 100, 22), "Stoke Width:")
        self.w.width = Slider((100, y, -10, 22), callback=self.changedCallback)
        
        y += 30
        self.w.lineCapText = TextBox((10, y, 100, 22), "Line Cap:")
        self.w.lineCap = PopUpButton((100, y, -10, 22), self._lineCapStylesMap.keys(), callback=self.changedCallback)
        
        y += 30
        self.w.lineJoinText = TextBox((10, y, 100, 22), "Line Join:")
        self.w.lineJoin = PopUpButton((100, y, -10, 22), self._lineJoinStylesMap.keys(), callback=self.changedCallback)
        
        self.setUpBaseWindowBehavior()
        self.w.open()
        addObserver(self, "draw", "draw")
        addObserver(self, "draw", "drawInactive")
        addObserver(self, "draw", "spaceCenterDraw")
    
    def changedCallback(self, sender):
        UpdateCurrentGlyphView()
        sc = CurrentSpaceCenter()
        if sc:
            sc.refreshAllExept()
    
    def windowCloseCallback(self, sender):
        super(StrokeObserer, self).windowCloseCallback(sender)
        removeObserver(self, "draw")
        removeObserver(self, "drawInactive")
        removeObserver(self, "spaceCenterDraw")

    
    def draw(self, notification):
        glyph = notification["glyph"]
        scale = notification["scale"]
        color = self.w.color.get()
        width = self.w.width.get()
        lineCap = self._lineCapStylesMap[self.w.lineCap.getTitle()]
        lineJoin = self._lineJoinStylesMap[self.w.lineJoin.getTitle()]
                
        path = glyph.getRepresentation("defconAppKit.NSBezierPath")       
        path.setLineWidth_(width)
        path.setLineCapStyle_(lineCap)
        path.setLineJoinStyle_(lineJoin)
        
        color.set()
        path.stroke()
        
     
StrokeObserer()