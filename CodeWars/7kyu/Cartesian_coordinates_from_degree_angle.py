# Write a simple function that takes polar coordinates (an angle in degrees and a radius) and returns the equivalent cartesian coordinates (rounded to 10 places).
#
# For example:
#
# coordinates(90,1)
# => (0.0, 1.0)
#
# coordinates(45, 1)
# => (0.7071067812, 0.7071067812)
# ALGORITHMSMATHEMATICSGEOMETRY
# Solution
import math

def coordinates(degrees, radius):
    grad = degrees * (math.pi / 180)
    return (round(radius * math.cos(grad), 10), round(radius * math.sin(grad), 10))