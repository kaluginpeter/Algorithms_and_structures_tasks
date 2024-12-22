# You are given a 2D integer array grid with size m x n. You are also given an integer k.
#
# Your task is to calculate the number of paths you can take from the top-left cell (0, 0) to the bottom-right cell (m - 1, n - 1) satisfying the following constraints:
#
# You can either move to the right or down. Formally, from the cell (i, j) you may move to the cell (i, j + 1) or to the cell (i + 1, j) if the target cell exists.
# The XOR of all the numbers on the path must be equal to k.
# Return the total number of such paths.
#
# Since the answer can be very large, return the result modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11
#
# Output: 3
#
# Explanation:
#
# The 3 paths are:
#
# (0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2)
# (0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)
# (0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)
# Example 2:
#
# Input: grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2
#
# Output: 5
#
# Explanation:
#
# The 5 paths are:
#
# (0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3)
# (0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2) → (2, 3)
# (0, 0) → (1, 0) → (1, 1) → (1, 2) → (1, 3) → (2, 3)
# (0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2) → (2, 3)
# (0, 0) → (0, 1) → (0, 2) → (1, 2) → (2, 2) → (2, 3)
# Example 3:
#
# Input: grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10
#
# Output: 0
#
#
#
# Constraints:
#
# 1 <= m == grid.length <= 300
# 1 <= n == grid[r].length <= 300
# 0 <= grid[r][c] < 16
# 0 <= k < 16
# Solution
# Python O(N**3) O(N**3) Dynamic Programming
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        MOD: int = 10**9 + 7
        dp: dict[int, dict[int, dict[int, int]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        initial_xor: int = grid[0][0]
        dp[0][0][initial_xor] = 1
        for r in range(m):
            for c in range(n):
                for xor_value in list(dp[r][c].keys()):
                    count: int = dp[r][c][xor_value]
                    if c + 1 < n:
                        new_xor: int = xor_value ^ grid[r][c + 1]
                        dp[r][c + 1][new_xor] = (dp[r][c + 1][new_xor] + count) % MOD
                    if r + 1 < m:
                        new_xor: int = xor_value ^ grid[r + 1][c]
                        dp[r + 1][c][new_xor] = (dp[r + 1][c][new_xor] + count) % MOD
        return dp[m - 1][n - 1][k]

# C++ O(N**3) O(N**3) Dynamic Programming
class Solution {
public:
    int countPathsWithXorValue(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int MOD = 1000000007;
        std::unordered_map<
            int, std::unordered_map<
                int, std::unordered_map<int, int>
            >
        > dp;
        int initialXor = grid[0][0];
        dp[0][0][initialXor] = 1;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                for (auto& pair : dp[r][c]) {
                    int count = dp[r][c][pair.first]; // xorValue
                    if (c + 1 < n) {
                        int newXor = pair.first ^ grid[r][c + 1];
                        dp[r][c + 1][newXor] = (dp[r][c + 1][newXor] + count) % MOD;
                    }
                    if (r + 1 < m) {
                        int newXor = pair.first ^ grid[r + 1][c];
                        dp[r + 1][c][newXor] = (dp[r + 1][c][newXor] + count) % MOD;
                    }
                }
            }
        }
        return dp[m - 1][n - 1][k];
    }
};