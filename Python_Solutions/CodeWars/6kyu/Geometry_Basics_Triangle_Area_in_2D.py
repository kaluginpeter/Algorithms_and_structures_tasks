# This series of katas will introduce you to basics of doing geometry with computers.
#
# Point objects have x, y attributes. Triangle objects have attributes
# a, b, c describing their corners, each of them is a Point.
#
# Write a function calculating area of a Triangle defined this way.
#
# Tests round answers to 6 decimal places.
#
# GEOMETRYFUNDAMENTALS
# Solution
def triangle_area(triangle):
    a, b, c = triangle.a, triangle.b, triangle.c
    return round(abs(a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) / 2, 6)