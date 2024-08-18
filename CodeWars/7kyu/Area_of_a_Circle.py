# Complete the function which will return the area of a circle with the given radius.
#
# Returned value is expected to be accurate up to tolerance of 0.01.
#
# If the radius is not positive, raise ValueError.
#
# Example:
#
# circle_area(43.2673)      # returns 5881.248  (± 0.01)
# circle_area(68)           # returns 14526.724 (± 0.01)
# circle_area(0)            # raises ValueError
# circle_area(-1)           # raises ValueError
# FUNDAMENTALSALGORITHMSGEOMETRYMATHEMATICS
# Solution
import math
def circle_area(r):
    return round(math.pi*r**2, 2) if type(r) == int and r > 0 else False