# You are given a 0-indexed integer matrix grid and an integer k.
#
# Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.
#
#
#
# Example 1:
#
#
# Input: grid = [[7,6,3],[6,6,1]], k = 18
# Output: 4
# Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.
# Example 2:
#
#
# Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
# Output: 6
# Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= n, m <= 1000
# 0 <= grid[i][j] <= 1000
# 1 <= k <= 109
# Solution
# Python O(NM) O(M) Matrix PrefixSum
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        prefix: list[int] = [0] * m
        output: int = 0
        for i in range(n):
            matrix: int = 0
            for j in range(m):
                prefix[j] += grid[i][j]
                matrix += prefix[j]
                if matrix <= k: output += 1
        return output

# C++ O(NM) O(M) PrefixSum Matrix
class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<uint32_t> prefix(m, 0);
        uint32_t output = 0;
        for (size_t i = 0; i < n; ++i) {
            uint32_t matrix = 0;
            for (size_t j = 0; j < m; ++j) {
                prefix[j] += grid[i][j];
                matrix += prefix[j];
                if (matrix <= k) ++output;
            }
        }
        return output;
    }
};