# Below is a right-angled triangle:
#
#   |\
#   | \
#   |  \
#   |   \
# o |    \ h
#   |     \
#   |    θ \
#   |_______\
#      a
# Your challange is to write a function that calculates the angle θ in degrees. You will be given three arguments representing each side: o, h and a. One of the arguments equals zero. Use the length of the two other sides to calculate θ.
#
# Round the result to the nearest integer, except in C and JavaScript.
#
# AlgorithmsMathematicsGeometry
# Solution
from math import degrees, asin, acos, atan

def missing_angle(h, a, o):
    if h == 0: return round(degrees(atan(o / a)))
    if a == 0: return round(degrees(asin(o / h)))
    return round(degrees(acos(a / h)))