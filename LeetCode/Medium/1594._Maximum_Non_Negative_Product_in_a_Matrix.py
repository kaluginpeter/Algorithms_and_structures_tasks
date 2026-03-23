# You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.
#
# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.
#
# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.
#
# Notice that the modulo is performed after getting the maximum product.
#
#
#
# Example 1:
#
#
# Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
# Output: -1
# Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
# Example 2:
#
#
# Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
# Output: 8
# Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
# Example 3:
#
#
# Input: grid = [[1,3],[0,-4]]
# Output: 0
# Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 15
# -4 <= grid[i][j] <= 4
#
# Solution
# Python O(NM) O(M) DynamicProgramming Matrix
mod: int = 10**9 + 7
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        prev_dp: list[list[int]] = [[float('inf'), float('-inf')] for _ in range(m)]
        prev_dp[0][0] = 1
        prev_dp[0][1] = 1
        for i in range(n):
            dp: list[list[int]] = [[float('inf'), float('-inf')] for _ in range(m)]
            for j in range(m):
                if grid[i][j] < 0:
                    if prev_dp[j][0] != float('inf'): dp[j][1] = max(dp[j][1], prev_dp[j][0] * grid[i][j])
                    if prev_dp[j][1] != float('-inf'): dp[j][0] = min(dp[j][0], prev_dp[j][1] * grid[i][j])
                    if j:
                        dp[j][0] = min(dp[j][0], dp[j - 1][1] * grid[i][j])
                        dp[j][1] = max(dp[j][1], dp[j - 1][0] * grid[i][j])
                else:
                    if prev_dp[j][0] != float('inf'): dp[j][0] = min(dp[j][0], prev_dp[j][0] * grid[i][j])
                    if prev_dp[j][1] != float('-inf'): dp[j][1] = max(dp[j][1], prev_dp[j][1] * grid[i][j])
                    if j:
                        dp[j][0] = min(dp[j][0], dp[j - 1][0] * grid[i][j])
                        dp[j][1] = max(dp[j][1], dp[j - 1][1] * grid[i][j])
            prev_dp = dp
        output: int = prev_dp[m - 1][1]
        if output < 0: return -1
        return output % mod

# C++ O(NM) O(M) Matrix DynamicProgramming
constexpr int mod = 1000000007;
class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<std::vector<long long>> prevDp(m, std::vector<long long>{INT64_MAX, INT64_MIN}); // <negative, positive>
        prevDp[0][0] = 1;
        prevDp[0][1] = 1;
        for (size_t i = 0; i < n; ++i) {
            std::vector<std::vector<long long>> dp(m, std::vector<long long>{INT64_MAX, INT64_MIN});
            for (size_t j = 0; j < m; ++j) {
                if (grid[i][j] < 0) {
                    if (prevDp[j][0] != INT64_MAX) dp[j][1] = std::max(dp[j][1], prevDp[j][0] * grid[i][j]);
                    if (prevDp[j][1] != INT64_MIN) dp[j][0] = std::min(dp[j][0], prevDp[j][1] * grid[i][j]);
                    if (j) {
                        dp[j][0] = std::min(dp[j][0], dp[j - 1][1] * grid[i][j]);
                        dp[j][1] = std::max(dp[j][1], dp[j - 1][0] * grid[i][j]);
                    }
                } else {
                    if (prevDp[j][0] != INT64_MAX) dp[j][0] = std::min(dp[j][0], prevDp[j][0] * grid[i][j]);
                    if (prevDp[j][1] != INT64_MIN) dp[j][1] = std::max(dp[j][1], prevDp[j][1] * grid[i][j]);
                    if (j) {
                        dp[j][0] = std::min(dp[j][0], dp[j - 1][0] * grid[i][j]);
                        dp[j][1] = std::max(dp[j][1], dp[j - 1][1] * grid[i][j]);
                    }
                }
            }
            prevDp = dp;
        }
        long long output = prevDp[m - 1][1];
        if (output < 0) return -1;
        return output % mod;
    }
};