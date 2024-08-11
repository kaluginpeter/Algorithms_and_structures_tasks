# You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
#
# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
#
# In one day, we are allowed to change any single land cell (1) into a water cell (0).
#
# Return the minimum number of days to disconnect the grid.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
#
# Output: 2
# Explanation: We need at least 2 days to get a disconnected grid.
# Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
# Example 2:
#
#
# Input: grid = [[1,1]]
# Output: 2
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either 0 or 1.
# Solution DFS O(NM(N + M) O(NM)
class Solution:
    def next_valid_ceil(
            self, row: int, col: int, n: int, m: int, seen: set[int], grid: list[list[int]]
    ) -> bool:
        return 0 <= row < n and 0 <= col < m and grid[row][col] == 1 and (row, col) not in seen

    def dfs(
            self, row: int, col: int, grid: list[list[int]], seen: set[int]
    ) -> None:
        stack: list[tuple[int, int]] = [(row, col)]
        directions: list[tuple[int, int]] = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        while stack:
            row, col = stack.pop()
            for path in directions:
                next_row, next_col = row + path[0], col + path[1]
                if self.next_valid_ceil(next_row, next_col, len(grid), len(grid[0]), seen, grid):
                    seen.add((next_row, next_col))
                    stack.append((next_row, next_col))

    def count_islands(self, grid: list[list[int]]) -> int:
        seen: set[int] = set()
        islands: int = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in seen:
                    islands += 1
                    seen.add((row, col))
                    self.dfs(row, col, grid, seen)
        return islands

    def minDays(self, grid: List[List[int]]) -> int:
        if self.count_islands(grid) != 1:
            return 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    if self.count_islands(grid) != 1:
                        return 1
                    grid[row][col] = 1

        return 2