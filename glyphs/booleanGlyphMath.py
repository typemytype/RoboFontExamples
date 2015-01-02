# get the current font
font = CurrentFont()

g1 = font["A"]
g2 = font["B"]

# difference
result = g1 % g2

dest = font.newGlyph("difference1")
dest.clear()
dest.appendGlyph(result)

# difference
result = g2 % g1

dest = font.newGlyph("difference2")
dest.clear()
dest.appendGlyph(result)

# union
result = g1 | g2

dest = font.newGlyph("union")
dest.clear()
dest.appendGlyph(result)

# intersection
result = g1 & g2

dest = font.newGlyph("intersection")
dest.clear()
dest.appendGlyph(result)

# xor
result = g1 ^ g2

dest = font.newGlyph("xor")
dest.clear()
dest.appendGlyph(result)