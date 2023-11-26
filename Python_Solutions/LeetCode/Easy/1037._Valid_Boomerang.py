# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
#
# A boomerang is a set of three points that are all distinct and not in a straight line.
#
#
#
# Example 1:
#
# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
# Example 2:
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: false
#
#
# Constraints:
#
# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100
# Solution Geometry Triangle Area Speed O(1), Memory O(1)
class Solution(object):
    def isBoomerang(self, p):
        x1, y1, x2, y2, x3, y3 = p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1]
        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0