# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
# Constraints:
#
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# Solution
# Python O(NM) O(M) DynamicProgramming Strings
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        prev_dp, cur_dp = list(range(m + 1)), list(range(m + 1))
        for i in range(1, n + 1):
            cur_dp[0] = i
            for j in range(1, m + 1):
                cur_dp[j] = min(
                    prev_dp[j - 1] + int(word1[i - 1] != word2[j - 1]),
                    prev_dp[j] + 1,
                    cur_dp[j - 1] + 1,
                )
            prev_dp = cur_dp[::]
        return prev_dp[m]

# C++ O(NM) O(M) DynamicProgramming Strings
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        vector<int> prevDp(m + 1, 0), curDp(m + 1, 0);
        for (int i = 0; i <= m; ++i) prevDp[i] = i;
        for (int i = 1; i <= n; ++i) {
            curDp[0] = i;
            for (int j = 1; j <= m; ++j) {
                curDp[j] = std::min({
                    prevDp[j - 1] + static_cast<int>(word1[i - 1] != word2[j - 1]),
                    prevDp[j] + 1,
                    curDp[j - 1] + 1,
                });
            }
            prevDp.assign(curDp.cbegin(), curDp.cend());
        }
        return prevDp[m];
    }
};