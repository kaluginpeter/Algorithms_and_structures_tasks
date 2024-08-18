# Given a non-degenerate triangle with lengths a, b, and c, return
#
# the radius of a circle inscribed in the triangle (r)
# the radius of a circle circumscribed on the triangle (R)
# Examples:
#
# radii(3, 4, 5) = (1, 2.5)                                   (r = 1, right triangle, thales theorem, so R = 5 / 2 = 2.5)
# radii(1, 1, 1) = (sqrt(3) / 6, sqrt(3) / 3)
# radii(2, 1, 2) = (0.3872983346207417, 1.032795558988644)    (maths, blah blah blah)
# No golfing limit for this one, because I felt that this kata wasn't very... golfable. But if you want to beat me, I got a 74 char solution, and I would really like to see limit being pushed further.
#
# Enjoy!
#
# Also, please check out the rest of the katas in this series! https://www.codewars.com/collections/math-challenges-1
#
# MATHEMATICS
# Solution
def radii(a, b, c):
    s: float = (a + b + c) / 2
    A: float = (s*(s - a)*(s - b)*(s - c))**.5
    return (A / s, (a * b * c) / (4 * A))