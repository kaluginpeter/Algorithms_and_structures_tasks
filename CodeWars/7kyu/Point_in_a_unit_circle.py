# Task
# Write a function that returns true if a given point (x,y) is inside of a unit circle (that is, a "normal" circle with a radius of one) centered at the origin (0,0) and returns false if the point is outside.
#
# Input
# x: The first coordinate of the given point.
# y: The second coordinate of the given point.
# Notes
# The region bounded by the circle is considered to be an open disk, so points on the boundary of the circle should return false.
# We are using the euclidean metric.
# MATHEMATICSFUNDAMENTALS
# Solution
def point_in_circle(x, y):
    return (x*x + y*y) < 1