# You will be given an array of cordinates and a radius. The function should return if the coordinates describe a point within the given radius of the origin.
#
# In two dimensions the condition that any [x, y] coordinate lies in a given radius (= a circle) is:
#
# x
# 2
# +
# y
# 2
# ≤
# r
# 2
# x
# 2
#  +y
# 2
#  ≤r
# 2
#
#
# This generalises to higher dimensions as follows:
#
# x
# 2
# +
# y
# 2
# +
# z
# 2
# +
# .
# .
# .
# ≤
# r
# 2
# x
# 2
#  +y
# 2
#  +z
# 2
#  +...≤r
# 2
#
#
# Note: a point with no coordinates should return true, as in zero dimensions all points are the same point
#
# MathematicsArraysFundamentals
# Solution
def in_sphere(coords, radius):
    return sum(pow(point, 2) for point in coords) <= pow(radius, 2)