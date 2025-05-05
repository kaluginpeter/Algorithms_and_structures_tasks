# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
#
#
# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
#
# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
#
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
# Example 2:
#
# Input: n = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 1000
# Solution
# Python O(N) O(N) DynamicProgramming
class Solution:
    def numTilings(self, n: int) -> int:
        MOD: int = 1000000007
        dp: list[int] = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = (2 * dp[i - 1] % MOD + (dp[i - 3] if i - 3 >= 0 else 0)) % MOD
        return dp[n]

# C++ O(N) ON(N) DynamicProgramming
class Solution {
public:
    int numTilings(int n) {
        int MOD = 1e9 + 7;
        vector<int> dp(n + 1, 1);
        for (int i = 2; i <= n; ++i) {
            dp[i] = (2 * dp[i - 1] % MOD + (i - 3 >= 0 ? dp[i - 3] : 0)) % MOD;
        }
        return dp[n];
    }
};