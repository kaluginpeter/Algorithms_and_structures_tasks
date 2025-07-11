# Kata Task
# Given 3 points a, b, c
#
#             c
#
#                      b
#   a
#
# Find the shortest distance from point c to a straight line that passes through points a and b
#
# Notes
#
# all points are of the form [x,y] where x >= 0 and y >= 0
# if a and b are the same then just return distance between a and c
# use Euclidean distance
# GeometryAlgorithms
# Solution
from math import sqrt

def distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def distance_from_line(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x0, y0 = c
    if a == b: return distance(a, c)
    numerator = abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1))
    denominator = distance(a, b)
    if denominator == 0: return distance(a, c)
    return numerator / denominator