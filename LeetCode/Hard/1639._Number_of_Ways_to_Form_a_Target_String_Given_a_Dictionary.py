# You are given a list of strings of the same length words and a string target.
#
# Your task is to form target using the given words under the following rules:
#
# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.
#
# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
# Example 2:
#
# Input: words = ["abba","baab"], target = "bab"
# Output: 4
# Explanation: There are 4 ways to form target.
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
# "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
# "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
#
#
# Constraints:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# All strings in words have the same length.
# 1 <= target.length <= 1000
# words[i] and target contain only lowercase English letters.
# Solution
# Python O(TL) O(TL) Dynamic Programming
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD: int = 10**9 + 7
        T, L = len(target), len(words[0])
        freq: list[list[int]] = [[0] * 26 for _ in range(L)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1

        dp: list[list[int]] = [[0] * (L + 1) for _ in range(T + 1)]
        dp[0][0] = 1
        for tindex in range(T + 1):
            for windex in range(L):
                dp[tindex][windex + 1] = (dp[tindex][windex + 1] + dp[tindex][windex]) % MOD
                if tindex < T:
                    char_idx: int = ord(target[tindex]) - ord('a')
                    dp[tindex + 1][windex + 1] = (dp[tindex + 1][windex + 1] + dp[tindex][windex] * freq[windex][char_idx]) % MOD
        return dp[T][L]

# C++ O(TL) O(TL) Dynamic Programming
class Solution {
public:
    int numWays(vector<string>& words, string target) {
        int MOD = 1000000007;
        int T = target.size();
        int L = words[0].size();
        std::vector<std::vector<int>> freq(L, std::vector<int>(26, 0));
        for (std::string word : words) {
            for (int idx = 0; idx < L; ++idx) {
                ++freq[idx][word[idx] - 'a'];
            }
        }
        std::vector<std::vector<long long>> dp(T + 1, std::vector<long long>(L + 1, 0));
        dp[0][0] = 1;
        for (int tindex = 0; tindex < T + 1; ++tindex) {
            for (int windex = 0; windex < L; ++windex) {
                dp[tindex][windex + 1] = (dp[tindex][windex + 1] + dp[tindex][windex]) % MOD;
                if (tindex < T) {
                    int charIdx = target[tindex] - 'a';
                    dp[tindex + 1][windex + 1] = (
                        dp[tindex + 1][windex + 1] + dp[tindex][windex] % MOD * freq[windex][charIdx] % MOD
                    ) % MOD;
                }
            }
        }
        return static_cast<int>(dp[T][L]);
    }
};