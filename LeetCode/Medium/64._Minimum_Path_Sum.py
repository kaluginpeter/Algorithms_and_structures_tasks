# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
# Solution
# Python O(NM) O(M) DynamicProgramming Matrix
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        dp: list[int] = [0] * m
        for i in range(n):
            next_dp: list[int] = [float('inf')] * m
            if not i: next_dp[0] = grid[0][0]
            for j in range(m):
                if i: next_dp[j] = min(next_dp[j], grid[i][j] + dp[j])
                if j: next_dp[j] = min(next_dp[j], next_dp[j - 1] + grid[i][j])
            dp = next_dp.copy()
        return dp[m - 1]

# C++ O(NM) O(M) DynamicProgramming Matrix
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<int> dp(m, 0);
        for (size_t i = 0; i < n; ++i) {
            std::vector<int> nextDp(m, 200 * 200 * 200 + 1);
            if (!i) nextDp[0] = grid[0][0];
            for (size_t j = 0; j < m; ++j) {
                if (j) nextDp[j] = std::min(nextDp[j], grid[i][j] + nextDp[j - 1]);
                if (i) nextDp[j] = std::min(nextDp[j], grid[i][j] + dp[j]);
            }
            dp = nextDp;
        }
        return dp[m - 1];
    }
};