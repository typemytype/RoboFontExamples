from mojo.events import addObserver

class MetricsOnTop(object):
    
    def __init__(self):
        # add an obserer when a space center did open
        addObserver(self, "metricsOnTop", "spaceCenterDidOpen")
    
    def metricsOnTop(self, notification):
        # get the window
        window = notification["window"]
        # get the space center object
        spaceCenter = window.getSpaceCenter()
        
        # vanilla rocks!
        # get the position of each element
        l, t, r, b = spaceCenter.glyphLineView.getPosSize()
        ll, tt, rr, bb = spaceCenter.inputScrollView.getPosSize()

        tt = abs(tt)
        # and use the old positions to reorganise the views
        spaceCenter.glyphLineView.setPosSize((l, t+tt+1, r, -0))
        spaceCenter.inputScrollView.setPosSize((ll, t, rr, bb))
        spaceCenter.hl.setPosSize((l, t+tt, 0, 1))
    
    
MetricsOnTop()