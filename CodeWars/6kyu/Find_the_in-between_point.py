# For this kata, you are given three points (x1,y1,z1), (x2,y2,z2),
# and (x3,y3,z3) that lie on a straight line in 3-dimensional space.
# You have to figure out which point lies in between the other two.
#
# Your function should return 1, 2, or 3 to indicate which point is the in-between one.
#
# FUNDAMENTALSGEOMETRYMATHEMATICSALGORITHMS
# Solution
def middle_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    d = {(x1, y1, z1): 1, (x2, y2, z2): 2, (x3, y3, z3): 3}
    return d[sorted(d)[1]]