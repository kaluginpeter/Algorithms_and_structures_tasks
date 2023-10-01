# Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. Return the result rounded to two decimals.
#
# Graph
#
# Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)
#
# FUNDAMENTALSMATHEMATICSGEOMETRY
# Solution
import math
def square_area(A):
    return round((A * 4 / (math.pi * 2)) ** 2, 2)