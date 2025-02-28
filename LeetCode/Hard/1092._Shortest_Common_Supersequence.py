# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
#
# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
#
#
#
# Example 1:
#
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.
# Example 2:
#
# Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# Output: "aaaaaaaa"
#
#
# Constraints:
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
# Solution
# Python O(NM) O(NM) Dynamic Programming
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n: int = len(str1)
        m: int = len(str2)
        dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]: dp[i][j] = dp[i - 1][j - 1] + 1
                else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs: list[str] = []
        i, j = n, m
        while dp[i][j]:
            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j]:
                lcs.append(str1[i - 1])
                i -= 1
            else:
                lcs.append(str2[j - 1])
                j -= 1
        while i:
            lcs.append(str1[i - 1])
            i -= 1
        while j:
            lcs.append(str2[j - 1])
            j -= 1
        return ''.join(reversed(lcs))

# C++ O(NM) O(NM) DynamicProgramming
class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int n = str1.size();
        int m = str2.size();
        vector<vector<int>> dp (n + 1, vector<int>(m + 1, 0));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (str1[i - 1] == str2[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        string lcs = "";
        int i = n, j = m;
        while (dp[i][j]) {
            if (str1[i - 1] == str2[j - 1]) {
                lcs.push_back(str1[i - 1]);
                --i;
                --j;
            } else if (dp[i][j] == dp[i - 1][j]) {
                lcs.push_back(str1[i - 1]);
                --i;
            } else {
                lcs.push_back(str2[j - 1]);
                --j;
            }
        }
        while (i > 0) {
            lcs.push_back(str1[i - 1]);
            --i;
        }
        while (j > 0) {
            lcs.push_back(str2[j - 1]);
            --j;
        }
        reverse(lcs.begin(), lcs.end());
        return lcs;
    }
};