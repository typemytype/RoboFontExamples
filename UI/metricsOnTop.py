from mojo.events import addObserver

class MetricsOnTop(object):
    
    def __init__(self):    
        addObserver(self, "metricsOnTop", "spaceCenterDidOpen")
    
    def metricsOnTop(self, notification):
        window = notification["window"]
        spaceCenter = window.getSpaceCenter()

        l, t, r, b = spaceCenter.glyphLineView.getPosSize()
        ll, tt, rr, bb = spaceCenter.inputScrollView.getPosSize()

        tt = abs(tt)

        spaceCenter.glyphLineView.setPosSize((l, t+tt+1, r, -0))
        spaceCenter.inputScrollView.setPosSize((ll, t, rr, bb))
        spaceCenter.hl.setPosSize((l, t+tt, 0, 1))
    
    
MetricsOnTop()