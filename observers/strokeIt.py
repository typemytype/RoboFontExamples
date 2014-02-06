from AppKit import *
from vanilla import *

from fontTools.pens.cocoaPen import CocoaPen

from defconAppKit.windows.baseWindow import BaseWindowController

from lib.UI.stepper import SliderEditIntStepper

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
        self.w = FloatingWindow((250, 130), "Stroke It")
        y = 10
        self.w.colorText = TextBox((10, y, 88, 22), "Stroke Color:", alignment="right")
        self.w.color = ColorWell((100, y-5, -10, 30), color=self.defaultColor, callback=self.changedCallback)
        
        y += 30
        self.w.widthText = TextBox((10, y, 88, 22), "Stoke Width:", alignment="right")
        self.w.width = SliderEditIntStepper((100, y, -10, 22), 10, callback=self.changedCallback, minValue=0, maxValue=100)
        
        y += 30
        self.w.lineCapText = TextBox((10, y, 88, 22), "Line Cap:", alignment="right")
        self.w.lineCap = PopUpButton((100, y, -10, 22), self._lineCapStylesMap.keys(), callback=self.changedCallback)
        
        y += 30
        self.w.lineJoinText = TextBox((10, y, 88, 22), "Line Join:", alignment="right")
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
        
        #path = glyph.naked().getRepresentation("defconAppKit.NSBezierPath")       
        pen = CocoaPen(glyph.getParent())
        glyph.draw(pen)
        path = pen.path
        
        path.setLineWidth_(width)
        path.setLineCapStyle_(lineCap)
        path.setLineJoinStyle_(lineJoin)
        
        color.set()
        path.stroke()
        
     
StrokeObserer()