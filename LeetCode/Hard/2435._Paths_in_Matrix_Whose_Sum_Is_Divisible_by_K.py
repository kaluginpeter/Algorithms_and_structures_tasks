# You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.
#
# Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
#
# Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
# Output: 2
# Explanation: There are two paths where the sum of the elements on the path is divisible by k.
# The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
# The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.
# Example 2:
#
#
# Input: grid = [[0,0]], k = 5
# Output: 1
# Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.
# Example 3:
#
#
# Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
# Output: 10
# Explanation: Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 5 * 104
# 1 <= m * n <= 5 * 104
# 0 <= grid[i][j] <= 100
# 1 <= k <= 50
# Solution
# Python O(NMK) O(MK) DynamicProgramming
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        dp: list[list[int]] = [[0] * k for _ in range(m + 1)]
        mod: int = 1000000007
        for i in range(1, n + 1):
            next_dp: list[list[int]] = [[0] * k for _ in range(m + 1)]
            if i == 1: next_dp[1][grid[0][0] % k] = 1
            for j in range(1, m + 1):
                for grid_sum in range(k):
                    rem: int = (grid_sum + grid[i - 1][j - 1]) % k
                    next_dp[j][rem] = (next_dp[j][rem] + next_dp[j - 1][grid_sum]) % mod
                    next_dp[j][rem] = (next_dp[j][rem] + dp[j][grid_sum]) % mod
            dp = next_dp
        return dp[m][0]

# C++ O(NMK) O(MK) DynamicProgramming
constexpr int mod = 1e9 + 7;
class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<std::array<int, 50>> dp(m + 1, std::array<int, 50>{});
        for (size_t i = 1; i <= n; ++i) {
            std::vector<std::array<int, 50>> nextDp(m + 1, std::array<int, 50>{});
            if (i == 1) nextDp[1][grid[0][0] % k] = 1;
            for (size_t j = 1; j <= m; ++j) {
                for (size_t gridSum = 0; gridSum < k; ++gridSum) {
                    size_t rem = (gridSum + grid[i - 1][j - 1]) % k;
                    // check move right
                    nextDp[j][rem] = (nextDp[j][rem] + nextDp[j - 1][gridSum]) % mod;
                    // check move down
                    nextDp[j][rem] = (nextDp[j][rem] + dp[j][gridSum]) % mod;
                }
            }
            dp = nextDp;
        }
        return dp[m][0];
    }
};