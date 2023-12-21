# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
#
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
#
# Note that points on the edge of a vertical area are not considered included in the area.
#
#
#
# Example 1:
#
# ​
# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.
# Example 2:
#
# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3
#
#
# Constraints:
#
# n == points.length
# 2 <= n <= 105
# points[i].length == 2
# 0 <= xi, yi <= 109
# Solution O(N log N) O(1)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        top, strt = 0, points[0][0]
        for i in range(1, len(points)):
            if points[i][0] != strt:
                top = max(top, points[i][0] - strt)
                strt = points[i][0]
        return top
# Solution 2 O(N log N) O(N)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = sorted({x for x, y in points})
        return max([x2 - x1 for x1, x2 in zip(l, l[1:])] + [0])