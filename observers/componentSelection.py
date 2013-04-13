from mojo.events import addObserver, removeObserver

from mojo.events import EditingTool
from fontTools.misc.arrayTools import sectRect, normRect, pointInRect

# Adds components selection to the editingTool...
# Selection of components only works when:
# - option is down
# - there is no point selection.


class ComponentSelection(object):

    def __init__(self):
        # observe the mouse up
        addObserver(self, "mouseUp", "mouseUp")

    def mouseUp(self, info):
        # get the glyph
        glyph = info["glyph"]
        # get the current tool
        tool = info["tool"]
        # only work when the curren tools is the editingTool
        if not isinstance(tool, EditingTool):
            return
        # go on when the option is down and there is no point selection in the glyph
        if tool.optionDown and not glyph.selection:
            # get the marque rect from the tool
            (x, y), (w, h) = tool.getMarqueRect()
            # normalize the rect to a minx, miny, maxx, maxy rectangle
            marqueRect = normRect((x, y, x + w, y +h))
            # loop over all components
            for component in glyph.components:
                # get the component bounding box
                comonentBounds = component.box
                # empty components are possible
                if comonentBounds:
                    # check if there an intersection between the marque rect and the component bounding box
                    interesect, intersectionRect = sectRect(marqueRect, component.box)
                    # if so...
                    if interesect:
                        # check if shift is down
                        if tool.shiftDown:
                            # on shift down, just toggle the current selection
                            component.selected = not component.selected    
                        else:
                            # othewise set the component as selected
                            component.selected = True
                else:
                    # empty component
                    # check if the off set point of the component is inside the marque rect
                    if pointInRect(component.offset, marqueRect):
                        # check if shift is down
                        if tool.shiftDown:
                            # on shift down, just toggle the current selection
                            component.selected = not component.selected
                        else:
                            # othewise set the component as selected
                            component.selected = True
            # update the glyph
            glyph.update()

# start the observer
ComponentSelection()