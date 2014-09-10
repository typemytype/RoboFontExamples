# convert to monospace font
from robofab.interface.all.dialogs import AskString

value = AskString("Monospace width:")

try:
    value = int(value)
except ValueError:
    value = None

if value:
    font = CurrentFont()
    for glyph in font:
        glyph.width = value