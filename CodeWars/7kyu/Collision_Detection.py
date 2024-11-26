# Create a function to determine whether or not two circles are colliding. You will be given the position of both circles in addition to their radii:
#
# def collision(x1, y1, radius1, x2, y2, radius2):
#   # collision?
# If a collision is detected, return true. If not, return false.
#
# Here's a geometric diagram of what the circles passed in represent:
#
# alt text
#
# Fundamentals
# Solution
import math
def collision(x1, y1, radius1, x2, y2, radius2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    radius_sum = radius1 + radius2
    return distance <= radius_sum