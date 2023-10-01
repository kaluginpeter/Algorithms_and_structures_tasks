# For a given 2D vector described by cartesian coordinates of its initial point and terminal point in the following format:
#
# [[x1, y1], [x2, y2]]
# Your function must return the vector's length represented as a floating point number.
# Error must be within 1e-7.
#
# Coordinates can be integers or floating point numbers.
#
# GEOMETRYMATHEMATICSFUNDAMENTALS
# Solution
import math
def vector_length(v):
    return math.sqrt(math.pow(v[0][0] - v[1][0], 2) + math.pow(v[0][1] - v[1][1], 2))