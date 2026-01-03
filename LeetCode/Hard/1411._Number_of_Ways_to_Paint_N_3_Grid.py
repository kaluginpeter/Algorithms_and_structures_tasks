# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).
#
# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.
#
#
#
# Example 1:
#
#
# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown.
# Example 2:
#
# Input: n = 5000
# Output: 30228214
#
#
# Constraints:
#
# n == grid.length
# 1 <= n <= 5000
#
# Solution
# Python O(N) O(1) Greedy
mod: int = 10**9 + 7
class Solution:
    def numOfWays(self, n: int) -> int:
        x: int = 6
        y: int = 6
        for i in range(2, n + 1):
            nx: int = (3 * x + 2 * y) % mod
            ny: int = (2 * x + 2 * y) % mod
            x, y = nx, ny
        return (x + y) % mod

# C++ O(N) O(1) Greedy
const int mod = 1000000007;
class Solution {
public:
    int numOfWays(int n) {
        long long x = 6, y = 6;
        for (int i = 2; i <= n; ++i) {
            long long nx = (3 * x + 2 * y) % mod;
            long long ny = (2 * x + 2 * y) % mod;
            x = nx;
            y = ny;
        }
        return (x + y) % mod;
    }
};