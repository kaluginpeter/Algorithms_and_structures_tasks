# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
#
# Given the grid grid represented as a string array, return the number of regions.
#
# Note that backslash characters are escaped, so a '\' is represented as '\\'.
#
#
#
# Example 1:
#
#
# Input: grid = [" /","/ "]
# Output: 2
# Example 2:
#
#
# Input: grid = [" /","  "]
# Output: 1
# Example 3:
#
#
# Input: grid = ["/\\","\\/"]
# Output: 5
# Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 1 <= n <= 30
# grid[i][j] is either '/', '\', or ' '.
# Solution UnionFind Matrix O(N**2) O(N**2)
class Solution:
    def __init__(self):
        self.parent: list[int] = []
        self.rank: list[int] = []
        self.count: int = 0

    def regionsBySlashes(self, grid):
        n: int = len(grid)
        dots: int = n + 1
        self.parent: list[int] = [i for i in range(dots * dots)]
        self.rank: list[int] = [1] * (dots * dots)

        for row in range(dots):
            for col in range(dots):
                if row == 0 or col == 0 or row == n or col == n:
                    cell: int = row * dots + col
                    self.union(0, cell)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == '\\':
                    cell1: int = row * dots + col
                    cell2: int = (row + 1) * dots + (col + 1)
                    self.union(cell1, cell2)
                elif grid[row][col] == '/':
                    cell1: int = (row + 1) * dots + col
                    cell2: int = row * dots + (col + 1)
                    self.union(cell1, cell2)

        return self.count

    def union(self, a, b):
        parent_a: int = self.find(a)
        parent_b: int = self.find(b)
        if parent_a == parent_b:
            self.count += 1
        else:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.parent[parent_b] = parent_a
            elif self.rank[parent_a] < self.rank[parent_b]:
                self.parent[parent_a] = parent_b
            else:
                self.parent[parent_b] = parent_a
                self.rank[parent_a] += 1

    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]