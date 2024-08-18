# You are given a 2D boolean matrix grid.
#
# Return an integer that is the number of right triangles that can be made with the 3 elements of grid such that all of them have a value of 1.
#
# Note:
#
# A collection of 3 elements of grid is a right triangle if one of its elements is in the same row with another element and in the same column with the third element. The 3 elements do not have to be next to each other.
#
#
# Example 1:
#
# 0	1	0
# 0	1	1
# 0	1	0
# 0	1	0
# 0	1	1
# 0	1	0
# Input: grid = [[0,1,0],[0,1,1],[0,1,0]]
#
# Output: 2
#
# Explanation:
#
# There are two right triangles.
#
# Example 2:
#
# 1	0	0	0
# 0	1	0	1
# 1	0	0	0
# Input: grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
#
# Output: 0
#
# Explanation:
#
# There are no right triangles.
#
# Example 3:
#
# 1	0	1
# 1	0	0
# 1	0	0
# 1	0	1
# 1	0	0
# 1	0	0
# Input: grid = [[1,0,1],[1,0,0],[1,0,0]]
#
# Output: 2
#
# Explanation:
#
# There are two right triangles.
#
#
#
# Constraints:
#
# 1 <= grid.length <= 1000
# 1 <= grid[i].length <= 1000
# 0 <= grid[i][j] <= 1
# Solution Pre Counting O(N**3) O(N)
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        ans: int = 0
        rows: list[list[int]] = [sum(grid[rows][cols] for rows in range(len(grid))) for cols in range(len(grid[0]))]
        for row in range(len(grid)):
            n: int = grid[row].count(1)
            if n > 1:
                for col in range(len(grid[0])):
                    if grid[row][col]:
                        ans += (n - 1) * (max(rows[col] - 1, 0))
        return ans