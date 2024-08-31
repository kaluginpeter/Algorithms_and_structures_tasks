# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# Solution Depth-First-Search Memoization O(NM) O(NM)
class Solution:
    def dfs(self, row: int, col: int, grid: list[list[str]], seen: set[tuple[int, int]]) -> None:
        if (row, col) in seen or not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])) or grid[row][col] == '0':
            return
        seen.add((row, col))
        self.dfs(row + 1, col, grid, seen)
        self.dfs(row, col + 1, grid, seen)
        self.dfs(row - 1, col, grid, seen)
        self.dfs(row, col - 1, grid, seen)

    def numIslands(self, grid: List[List[str]]) -> int:
        seen: set[tuple[int, int]] = set()
        islands: int = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    self.dfs(row, col, grid, seen)
                    islands += 1
        return islands