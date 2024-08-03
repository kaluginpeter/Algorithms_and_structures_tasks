# You are given an m x n binary matrix grid.
#
# A row or column is considered palindromic if its values read the same forward and backward.
#
# You can flip any number of cells in grid from 0 to 1, or from 1 to 0.
#
# Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.
#
#
#
# Example 1:
#
# Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
#
# Output: 2
#
# Explanation:
#
#
#
# Flipping the highlighted cells makes all the rows palindromic.
#
# Example 2:
#
# Input: grid = [[0,1],[0,1],[0,0]]
#
# Output: 1
#
# Explanation:
#
#
#
# Flipping the highlighted cell makes all the columns palindromic.
#
# Example 3:
#
# Input: grid = [[1],[0]]
#
# Output: 0
#
# Explanation:
#
# All rows are already palindromic.
#
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m * n <= 2 * 105
# 0 <= grid[i][j] <= 1
# Solution Two Pointers Matrix Greedy O(NM) O(N)
class Solution:
    def how_many(self, arr: list[int]) -> int:
        left: int = 0
        right: int = len(arr) - 1
        needed: int = 0
        while left < right:
            if arr[left] != arr[right]:
                needed += 1
            left += 1
            right -= 1
        return needed

    def minFlips(self, grid: List[List[int]]) -> int:
        needed_for_row: int = 0
        needed_for_col: int = 0
        for row in grid:
            needed_for_row += self.how_many(row)
        for col in range(len(grid[0])):
            cols: list[int] = [grid[row][col] for row in range(len(grid))]
            needed_for_col += self.how_many(cols)
        return min(needed_for_row, needed_for_col)