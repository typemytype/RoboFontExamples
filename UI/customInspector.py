from mojo.UI import AccordionView
from vanilla import *

class MyInspector:

    def __init__(self):

        self.w = FloatingWindow((200, 600))

        self.firstItem = TextEditor((10, 10, -10, -10))

        self.secondItem = List((0, 0, -0, -0), ["a", "b", "c"])

        self.thirdItem = Tabs((10, 10, -10, -10), ["1", "2", "3"])

        self.fourthItem = Group((0, 0, -0, -0))

        self.fourthItem.checkBox = CheckBox((10, 10, 100, 22), "CheckBox")
        self.fourthItem.editText = EditText((10, 40, -10, 22))


        descriptions = [
                       dict(label="first item", view=self.firstItem, size=200, collapsed=False, canResize=False),
                       dict(label="second item", view=self.secondItem, minSize=100, size=140, collapsed=True, canResize=True),
                       dict(label="third item", view=self.thirdItem, minSize=100, size=140, collapsed=True, canResize=False),
                       dict(label="fourth item", view=self.fourthItem, size=140, collapsed=False, canResize=False)
                       ]

        self.w.accordionView = AccordionView((0, 0, -0, -0), descriptions)

        self.w.open()

MyInspector()