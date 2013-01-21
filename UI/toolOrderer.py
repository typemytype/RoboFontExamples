from AppKit import NSDragOperationMove
from vanilla import *

from mojo.events import setToolOrder, getToolOrder

toolOrderDragType = "toolOrderDragType"

class ToolOrder:
    
    def __init__(self):
        
        self.w = Window((200, 300), "Tool Orderer")
        
        self.w.tools = List((10, 10, -10, -40), getToolOrder(),
                            dragSettings=dict(type=toolOrderDragType, callback=self.dragCallback),
                            selfDropSettings=dict(type=toolOrderDragType, operation=NSDragOperationMove, callback=self.dropListSelfCallback),
                            )
        
        self.w.apply = Button((10, -30, -10, 22), "Apply", callback=self.applyCallback)
        self.w.open()
    
    def applyCallback(self, sender):
        setToolOrder(self.w.tools.get())
        
    def dragCallback(self, sender, indexes):
        return indexes
        
    def dropListSelfCallback(self, sender, dropInfo):
        isProposal = dropInfo["isProposal"]
        
        if not isProposal:
            indexes = [int(i) for i in sorted(dropInfo["data"])]
            indexes.sort()
            source = dropInfo["source"]
            rowIndex = dropInfo["rowIndex"]

            items = sender.get()

            toMove = [items[index] for index in indexes]

            for index in reversed(indexes):
                del items[index]

            rowIndex -= len([index for index in indexes if index < rowIndex])
            for font in toMove:
                items.insert(rowIndex, font)
                rowIndex += 1

            sender.set(items)
        return True
        
        
ToolOrder()