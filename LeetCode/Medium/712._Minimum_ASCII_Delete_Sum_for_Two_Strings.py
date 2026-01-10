# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
#
#
#
# Example 1:
#
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:
#
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.
# Solution
# Python O(NM) O(M) DynamicProgramming
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n: int = len(s1)
        m: int = len(s2)
        dp: list[int] = [0] * (m + 1)
        next_dp: list[int] = [0] * (m + 1)
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])
        for i in range(1, n + 1):
            next_dp[0] = dp[0] + ord(s1[i - 1])
            for j in range(1, m + 1):
                next_dp[j] = min(
                    (dp[j - 1] if s1[i - 1] == s2[j - 1] else float('inf')),
                    dp[j] + ord(s1[i - 1]),
                    next_dp[j - 1] + ord(s2[j - 1])
                )
            dp = next_dp.copy()
        return dp[m]

# C++ O(NM) O(M) DynamicProgramming
class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        size_t n = s1.size(), m = s2.size();
        std::vector<int> dp(m + 1, 0), nextDp(m + 1, 0);
        for (size_t j = 1; j <= m; ++j) dp[j] = dp[j - 1] + s2[j - 1];
        for (size_t i = 1; i <= n; ++i) {
            nextDp[0] = dp[0] + s1[i - 1];
            for (size_t j = 1; j <= m; ++j) {
                nextDp[j] = std::min({
                    (s1[i - 1] == s2[j - 1] ? dp[j - 1] : INT32_MAX / 2),
                    dp[j] + s1[i - 1],
                    nextDp[j - 1] + s2[j - 1]
                });
            }
            dp = nextDp;
        }
        return dp[m];
    }
};