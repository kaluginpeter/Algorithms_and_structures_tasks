# Write the following function:
#
# def area_of_polygon_inside_circle(circle_radius, number_of_sides):
# It should calculate the area of a regular polygon of numberOfSides, number-of-sides,
# or number_of_sides sides inside a circle of radius circleRadius, circle-radius,
# or circle_radius which passes through all the vertices of the polygon
# (such circle is called circumscribed circle or circumcircle).
# The answer should be a number rounded to 3 decimal places.
#
# Input :: Output Examples
#
# area_of_polygon_inside_circle(3, 3) # returns 11.691
#
# area_of_polygon_inside_circle(5.8, 7) # returns 92.053
#
# area_of_polygon_inside_circle(4, 5) # returns 38.042
# Note: if you need to use Pi in your code, use the native value of your language unless stated otherwise.
#
# MATHEMATICSGEOMETRYFUNDAMENTALS
# Solution
import math
def area_of_polygon_inside_circle(r, n):
    return float("{:.3f}".format((math.sin(2 * math.pi / n) * r * r * n) / 2))