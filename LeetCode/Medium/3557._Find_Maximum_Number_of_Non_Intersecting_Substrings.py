# You are given a string word.
#
# Return the maximum number of non-intersecting substrings of word that are at least four characters long and start and end with the same letter.
#
# A substring is a contiguous non-empty sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: word = "abcdeafdef"
#
# Output: 2
#
# Explanation:
#
# The two substrings are "abcdea" and "fdef".
#
# Example 2:
#
# Input: word = "bcdaaaab"
#
# Output: 1
#
# Explanation:
#
# The only substring is "aaaa". Note that we cannot also choose "bcdaaaab" since it intersects with the other substring.
#
#
#
# Constraints:
#
# 1 <= word.length <= 2 * 105
# word consists only of lowercase English letters.
# Solution
# Python O(N) O(N) DynamicProgramming O(N) O(N)
class Solution:
    def maxSubstrings(self, word: str) -> int:
        n: int = len(word)
        dp: list[int] = [0] * n
        prev: list[list[int]] = [[] for _ in range(26)]
        for i in range(n):
            x: int = ord(word[i]) - 97
            prev[x].append(i)
            left: int = -1
            for j in range(len(prev[x]) - 1, -1, -1):
                if i - prev[x][j] + 1 >= 4:
                    left = prev[x][j]
                    break
            if left < 0:
                dp[i] = dp[i - 1] if i else 0
                continue
            take: int = (dp[left - 1] if left - 1 >= 0 else 0) + 1
            not_take: int = dp[i - 1] if i else 0
            dp[i] = max(take, not_take)

        return dp[n - 1]

# C++ O(N) O(N) DynamicProgramming
class Solution {
public:
    int maxSubstrings(string word) {
        int n = word.size();
        vector<int> dp(n, 0);
        vector<vector<int>> prev(26, vector<int>());
        for (int i = 0; i < n; ++i) {
            int left = -1;
            for (int j = prev[word[i] - 'a'].size() - 1; j >= 0; --j) {
                if (i - prev[word[i] - 'a'][j] + 1 >= 4) {
                    left = prev[word[i] - 'a'][j];
                    break;
                }
            }
            prev[word[i] - 'a'].push_back(i);
            if (left == -1) {
                dp[i] = (i? dp[i - 1] : 0);
                continue;
            }
            int take = (left - 1 >= 0? dp[left - 1] : 0) + 1;
            int notTake = (i? dp[i - 1] : 0);
            dp[i] = max(take, notTake);
        }
        return dp[n - 1];
    }
};