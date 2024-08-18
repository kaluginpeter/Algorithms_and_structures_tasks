# You have the radius of a circle with the center in point (0,0).
#
# Write a function that calculates the number of points in the circle where (x,y)
# - the cartesian coordinates of the points - are integers.
#
# Example: for radius = 2 the result should be 13.
#
# 0 <= radius <= 1000
#
#
#
# GEOMETRYALGORITHMSLOGICMATHEMATICSFUNDAMENTALS
# Solution
def points(n):
    count = 0
    for i in range(1, n + 1):
        count += int((n**2 - i**2) ** (1/2))
    return 1 + int((count + n) * 4)