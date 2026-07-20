# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
#
# In one shift operation:
#
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]
# Example 2:
#
#
# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
# Example 3:
#
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 50
# 1 <= n <= 50
# -1000 <= grid[i][j] <= 1000
# 0 <= k <= 100
#
# Solution
# Python O(NM) O(NM) Matrix Math
from copy import deepcopy
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        output: list[list[int]] = deepcopy(grid.copy())
        n: int = len(grid)
        m: int = len(grid[0])
        mod: int = n * m
        k %= mod
        for i in range(n):
            for j in range(m):
                new_cell: int = (i * m + j + k) % mod
                output[new_cell // m][new_cell % m] = grid[i][j]
        return output

# C++ O(NM) O(NM) Math Matrix
class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        std::vector<std::vector<int>> output = grid;
        size_t n = grid.size(), m = grid[0].size(), mod = n * m;
        k %= mod;
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                size_t newCell = (i * m + j + k) % mod;
                output[newCell / m][newCell % m] = grid[i][j];
            }
        }
        return output;
    }
};