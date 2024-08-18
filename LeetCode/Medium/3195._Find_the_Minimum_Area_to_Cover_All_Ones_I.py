# You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.
#
# Return the minimum possible area of the rectangle.
#
#
#
# Example 1:
#
# Input: grid = [[0,1,0],[1,0,1]]
#
# Output: 6
#
# Explanation:
#
#
#
# The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.
#
# Example 2:
#
# Input: grid = [[0,0],[1,0]]
#
# Output: 1
#
# Explanation:
#
#
#
# The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.
#
#
#
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 0 or 1.
# The input is generated such that there is at least one 1 in grid.
# Solution O(NM) O(1)
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        up = left = float('inf')
        down = right = float('-inf')
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    up = min(up, row)
                    down = max(down, row)
                    right = max(right, col)
                    left = min(left, col)
        area: int = (right - left + 1) * (down - up + 1)
        return area