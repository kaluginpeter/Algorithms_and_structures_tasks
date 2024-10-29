# You are given a 0-indexed m x n matrix grid consisting of positive integers.
#
# You can start at any cell in the first column of the matrix, and traverse the grid in the following way:
#
# From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
# Return the maximum number of moves that you can perform.
#
#
#
# Example 1:
#
#
# Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# Output: 3
# Explanation: We can start at the cell (0, 0) and make the following moves:
# - (0, 0) -> (0, 1).
# - (0, 1) -> (1, 2).
# - (1, 2) -> (2, 3).
# It can be shown that it is the maximum number of moves that can be made.
# Example 2:
#
#
# Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
# Output: 0
# Explanation: Starting from any cell in the first column we cannot perform any moves.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# 1 <= grid[i][j] <= 106
# Solution
# Python O(NM) O(NM) Dynamic Programming Depth-First-Search
class Solution:
    dirs: list[int] = [-1, 0, 1]

    def dfs(self, row: int, col: int, grid: list[list[int]], dp: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        if dp[row][col] != -1:
            return dp[row][col]
        max_moves: int = 0
        for move in self.dirs:
            new_row, new_col = row + move, col + 1
            if (
                0 <= new_row < M
                and 0 <= new_col < N
                and grid[row][col] < grid[new_row][new_col]
            ):
                max_moves = max(
                    max_moves, 1 + self.dfs(new_row, new_col, grid, dp)
                )
        dp[row][col] = max_moves
        return max_moves

    def maxMoves(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp: list[list[int]] = [[-1] * N for _ in range(M)]
        max_moves: int = 0
        for row in range(M):
            moves_required: int = self.dfs(row, 0, grid, dp)
            max_moves = max(max_moves, moves_required)
        return max_moves

# C++ O(NM) O(NM) Dynamic Programming Depth-First-Search
class Solution:
    dirs: list[int] = [-1, 0, 1]

    def dfs(self, row: int, col: int, grid: list[list[int]], dp: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        if dp[row][col] != -1:
            return dp[row][col]
        max_moves: int = 0
        for move in self.dirs:
            new_row, new_col = row + move, col + 1
            if (
                0 <= new_row < M
                and 0 <= new_col < N
                and grid[row][col] < grid[new_row][new_col]
            ):
                max_moves = max(
                    max_moves, 1 + self.dfs(new_row, new_col, grid, dp)
                )
        dp[row][col] = max_moves
        return max_moves

    def maxMoves(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp: list[list[int]] = [[-1] * N for _ in range(M)]
        max_moves: int = 0
        for row in range(M):
            moves_required: int = self.dfs(row, 0, grid, dp)
            max_moves = max(max_moves, moves_required)
        return max_moves