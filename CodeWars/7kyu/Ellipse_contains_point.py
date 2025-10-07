# You are given a length of string and two thumbtacks. One thumbtack goes into the focus point F₀ with coordinates x₀ and y₀, and the other goes into focus point F₁ with coordinates x₁ and y₁. The string is then tied at the ends to the thumbtacks and has length l excluding the knots at the ends. If you pull the string taught with a pencil and draw around the plane you'll have an ellipse with focuses at F₀ and F₁. Given a new point P, determine if it falls inside of the ellipse.
#
# You must write a function that takes arguments f0, f1, l, and p and returns true or false depending on whether or not p falls inside the ellipse.
#
# Each of f0, f1, and p has has properties x and y for its coordinates.
#
# You will never be given the case where the string is too short to reach between the points.
#
# GeometryMathematicsAlgorithms
# Solution
import math

def ellipse_contains_point(f0, f1, l, p):
    d0: float = math.dist((f0['x'], f0['y']), (p['x'], p['y']))
    d1: float = math.dist((f1['x'], f1['y']), (p['x'], p['y']))
    return d0 + d1 <= l