# You are given a n x n 2D array grid containing distinct elements in the range [0, n2 - 1].
#
# Implement the neighborSum class:
#
# neighborSum(int [][]grid) initializes the object.
# int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, that is either to the top, left, right, or bottom of value in grid.
# int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, that is either to the top-left, top-right, bottom-left, or bottom-right of value in grid.
#
#
#
#
# Example 1:
#
# Input:
#
# ["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]
#
# [[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]
#
# Output: [null, 6, 16, 16, 4]
#
# Explanation:
#
#
#
# The adjacent neighbors of 1 are 0, 2, and 4.
# The adjacent neighbors of 4 are 1, 3, 5, and 7.
# The diagonal neighbors of 4 are 0, 2, 6, and 8.
# The diagonal neighbor of 8 is 4.
# Example 2:
#
# Input:
#
# ["neighborSum", "adjacentSum", "diagonalSum"]
#
# [[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]
#
# Output: [null, 23, 45]
#
# Explanation:
#
#
#
# The adjacent neighbors of 15 are 0, 10, 7, and 6.
# The diagonal neighbors of 9 are 4, 12, 14, and 15.
#
#
# Constraints:
#
# 3 <= n == grid.length == grid[0].length <= 10
# 0 <= grid[i][j] <= n2 - 1
# All grid[i][j] are distinct.
# value in adjacentSum and diagonalSum will be in the range [0, n2 - 1].
# At most 2 * n2 calls will be made to adjacentSum and diagonalSum.
# Solution
# Complexity
# Time complexity: O(N^2) - because our initialization will cost O(N^2), but other operations like search, adjacentSum or diagonalSum will be always(almost if we know about hashmap complexities) cost O(1)
# Space complexity: O(N^2)
# Code
class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.mtrx: list[list[int]] = grid
        self.positions: dict[int, tuple[int]] = dict()
        for row in range(len(self.mtrx)):
            for col in range(len(self.mtrx)):
                self.positions[self.mtrx[row][col]] = (row, col)

    def search(self, value: int) -> tuple[int, int]:
        return self.positions[value]

    def adjacentSum(self, value: int) -> int:
        row, col = self.search(value)
        sm: int = 0
        # upper element
        if row - 1 >= 0: sm += self.mtrx[row - 1][col]
        # left side element
        if col - 1 >= 0: sm += self.mtrx[row][col - 1]
        # right side element
        if col + 1 < len(self.mtrx): sm += self.mtrx[row][col + 1]
        # bottom element
        if row + 1 < len(self.mtrx): sm += self.mtrx[row + 1][col]
        return sm

    def diagonalSum(self, value: int) -> int:
        row, col = self.search(value)
        sm: int = 0
        # upper left element
        if row - 1 >= 0 and col - 1 >= 0: sm += self.mtrx[row - 1][col - 1]
        # lower left element
        if row + 1 < len(self.mtrx) and col - 1 >= 0: sm += self.mtrx[row + 1][col - 1]
        # lower right element
        if row + 1 < len(self.mtrx) and col + 1 < len(self.mtrx): sm += self.mtrx[row + 1][col + 1]
        # upper right element
        if row - 1 >= 0 and col + 1 < len(self.mtrx): sm += self.mtrx[row - 1][col + 1]
        return sm



# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)