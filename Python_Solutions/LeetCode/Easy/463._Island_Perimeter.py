# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:
#
# Input: grid = [[1]]
# Output: 4
# Example 3:
#
# Input: grid = [[1,0]]
# Output: 4
#
#
# Constraints:
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
# Solution Simulation O(NM4) O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans: int = 0
        moves: list[list[int, int]] = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        n, m = len(grid), len(grid[0])
        for rows in range(n):
            for cols in range(m):
                if grid[rows][cols] == 1:
                    for mov in moves:
                        x, y = mov
                        if (rows + x < 0 or rows + x == n) or (cols + y < 0 or cols + y == m):
                            ans += 1
                            continue
                        ans += grid[rows + x][cols + y] == 0
        return ans