# Problem statement
# Packing multiple rectangles of varying widths and heights in an enclosing rectangle of minimum area. Given 3 rectangular boxes, find minimal area that they can be placed. Boxes can not overlap, these can only be placed on the floor.
#
# Input
# 3 pairs of numbers come to the input - the lengths(a1, b1, a2, b2, a3, b3) of the sides of the boxes. (1 ⩽ ai, bi ⩽ 10^4)
#
# Output
# Return a number equal to the minimum occupied area.
#
# Example
# Input example:
#
# packing_rectangles(4,10,5,11,12,3)
# Output example:
#
# 144
# ALGORITHMS
# Solution
def packing_rectangles(a1, b1, a2, b2, a3, b3):
    def area(w, h):
        return w * h
    orientations = [
        (a1, b1, a2, b2, a3, b3),
        (a1, b1, b2, a2, a3, b3),
        (b1, a1, a2, b2, a3, b3),
        (b1, a1, b2, a2, a3, b3),
        (a1, b1, a2, b2, b3, a3),
        (a1, b1, b2, a2, b3, a3),
        (b1, a1, a2, b2, b3, a3),
        (b1, a1, b2, a2, b3, a3)
    ]
    min_area = float('inf')
    for orientation in orientations:
        w1, h1, w2, h2, w3, h3 = orientation
        min_area = min(min_area, area(w1 + w2 + w3, max(h1, h2, h3)))
        min_area = min(min_area, area(max(w1 + w2, w3), h1 + h2 + h3))
        min_area = min(min_area, area(max(w1 + w3, w2), h1 + h3 + h2))
        min_area = min(min_area, area(max(w2 + w3, w1), h2 + h3 + h1))
        min_area = min(min_area, area(w1 + max(w2, w3), max(h1, h2 + h3)))
        min_area = min(min_area, area(w2 + max(w1, w3), max(h2, h1 + h3)))
        min_area = min(min_area, area(w3 + max(w1, w2), max(h3, h1 + h2)))
        min_area = min(min_area, area(max(w1, w2, w3), h1 + h2 + h3))
    return min_area