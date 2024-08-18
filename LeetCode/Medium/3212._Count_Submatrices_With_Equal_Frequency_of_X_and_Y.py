# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of
# submatrices
#  that contains:
#
# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.
#
#
# Example 1:
#
# Input: grid = [["X","Y","."],["Y",".","."]]
#
# Output: 3
#
# Explanation:
#
#
#
# Example 2:
#
# Input: grid = [["X","X"],["X","Y"]]
#
# Output: 0
#
# Explanation:
#
# No submatrix has an equal frequency of 'X' and 'Y'.
#
# Example 3:
#
# Input: grid = [[".","."],[".","."]]
#
# Output: 0
#
# Explanation:
#
# No submatrix has at least one 'X'.
#
#
#
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.
# Solution O(N) O(N)
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        prefix_x: list[int] = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefix_y: list[int] = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_x[i][j] = prefix_x[i-1][j] + prefix_x[i][j-1] - prefix_x[i-1][j-1] + (grid[i-1][j-1] == 'X')
                prefix_y[i][j] = prefix_y[i-1][j] + prefix_y[i][j-1] - prefix_y[i-1][j-1] + (grid[i-1][j-1] == 'Y')
        valid_submatrices: int = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                count_x = prefix_x[i][j] - prefix_x[0][j] - prefix_x[i][0] + prefix_x[0][0]
                count_y = prefix_y[i][j] - prefix_y[0][j] - prefix_y[i][0] + prefix_y[0][0]
                if count_x == count_y and count_x > 0: valid_submatrices += 1
        return valid_submatrices