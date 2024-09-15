# You are given an integer array a of size 4 and another integer array b of size at least 4.
#
# You need to choose 4 indices i0, i1, i2, and i3 from the array b such that i0 < i1 < i2 < i3. Your score will be equal to the value a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3].
#
# Return the maximum score you can achieve.
#
#
#
# Example 1:
#
# Input: a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]
#
# Output: 26
#
# Explanation:
# We can choose the indices 0, 1, 2, and 5. The score will be 3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26.
#
# Example 2:
#
# Input: a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]
#
# Output: -1
#
# Explanation:
# We can choose the indices 0, 1, 3, and 4. The score will be (-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1.
#
#
#
# Constraints:
#
# a.length == 4
# 4 <= b.length <= 105
# -105 <= a[i], b[i] <= 105
# Solution Dynamic Programming
# Python O(MN) O(MN)
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n: int = len(b)
        dp: list[list[int]] = [[-float('inf')] * 5 for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(5):
                dp[i][j] = dp[i - 1][j]
            for j in range(1, 5):
                dp[i][j] = max(
                    dp[i][j],
                    dp[i - 1][j - 1] + a[j - 1] * b[i - 1]
                )
        return dp[n][4]
# C++ O(MN) O(MN)
#include <vector>
#include <limits>
#include <algorithm>

class Solution {
public:
    long long maxScore(std::vector<int>& a, std::vector<int>& b) {
        int n = b.size();
        std::vector<std::vector<long long>> dp(n + 1, std::vector<long long>(5, std::numeric_limits<long long>::min()));
        dp[0][0] = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < 5; ++j) {
                dp[i][j] = dp[i - 1][j];
            }
            for (int j = 1; j < 5; ++j) {
                if (dp[i - 1][j - 1] != std::numeric_limits<long long>::min()){
                    dp[i][j] = std::max(
                        dp[i][j],
                        dp[i - 1][j - 1] + static_cast<long long>(a[j - 1]) * b[i - 1]
                    );
                }
            }
        }
        return dp[n][4];
    }
};