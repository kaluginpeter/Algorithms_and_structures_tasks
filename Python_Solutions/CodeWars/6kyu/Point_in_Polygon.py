# The problem
# In this kata, you're going write a function called point_in_polygon to test if a point is inside a polygon.
#
# Points will be represented as tuples (x,y).
#
# The polygon will be an array of points which are the polygon's vertices. The last point in the array connects back to the first point.
#
# You can assume:
#
# The polygon will be a valid simple polygon. That is, it will have at least three points, none of its edges will cross each other, and exactly two edges will meet at each vertex.
#
# In the tests, the point will never fall exactly on an edge of the polygon.
#
# Testing
# To help you visualize your test cases, the visualize_polygon(polygon, point) function is preloaded. It draws the polygon and point.
#
# GEOMETRYMATHEMATICSALGORITHMS
# Solution
from typing import List, Tuple
from preloaded import visualize_polygon
def point_in_polygon(poly, point) -> bool:
    x,y  = point
    n = len(poly)
    inside = False
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside