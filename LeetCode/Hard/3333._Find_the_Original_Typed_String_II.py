# Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
#
# You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.
#
# Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.
#
# Since the answer may be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: word = "aabbccdd", k = 7
#
# Output: 5
#
# Explanation:
#
# The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".
#
# Example 2:
#
# Input: word = "aabbccdd", k = 8
#
# Output: 1
#
# Explanation:
#
# The only possible string is "aabbccdd".
#
# Example 3:
#
# Input: word = "aaabbb", k = 3
#
# Output: 8
#
#
#
# Constraints:
#
# 1 <= word.length <= 5 * 105
# word consists only of lowercase English letters.
# 1 <= k <= 2000
# Solution
# Python O(N + k^2) O(k) DynamicProgramming
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n: int = len(word)
        left: int = 0
        mod: int = 10 ** 9 + 7
        freq: list[int] = []
        for right in range(n):
            if word[right] != word[left]:
                freq.append(right - left)
                left = right
        freq.append(n - left)
        output: int = 1
        for x in freq:
            output = (output * x) % mod
        if len(freq) >= k: return output
        prev_dp: list[int] = [0] * k
        prev_prefix_sum: list[int] = [1] * k
        for i in range(len(freq)):
            new_dp: list[int] = [0] * k
            for j in range(1, k):
                new_dp[j] = prev_prefix_sum[j - 1]
                if j - freq[i] - 1 >= 0:
                    new_dp[j] = (new_dp[j] - prev_prefix_sum[j - freq[i] - 1] + mod) % mod
            new_prefix_sum: list[int] = [0] * k
            for j in range(1, k):
                new_prefix_sum[j] = (new_prefix_sum[j - 1] + new_dp[j]) % mod
            prev_dp = new_dp
            prev_prefix_sum = new_prefix_sum
        return (output - prev_prefix_sum[k - 1] + mod) % mod

# C++ O(N + k^2) O(k) DynamicProgramming
class Solution {
public:
    int possibleStringCount(string word, int k) {
        int n = word.size(), left = 0, mod = 1e9 + 7;
        vector<int> freq;
        for (int right = 0; right < n; ++right) {
            if (word[right] != word[left]) {
                freq.push_back(right - left);
                left = right;
            }
        }
        freq.push_back(n - left);
        int output = 1;
        for (int x : freq) {
            output = static_cast<long long>(output) * x % mod;
        }
        if (freq.size() >= k) return output;

        vector<int> prevDp(k), prevPrefixSum(k, 1);
        prevDp[0] = 1;
        for (int i = 0; i < freq.size(); ++i) {
            vector<int> newDP(k);
            for (int j = 1; j < k; ++j) {
                newDP[j] = prevPrefixSum[j - 1];
                if (j - freq[i] - 1 >= 0) {
                    newDP[j] = (newDP[j] - prevPrefixSum[j - freq[i] - 1] + mod) % mod;
                }
            }
            vector<int> newPrefixSum(k);
            newPrefixSum[0] = newDP[0];
            for (int j = 1; j < k; ++j) {
                newPrefixSum[j] = (newPrefixSum[j - 1] + newDP[j]) % mod;
            }
            prevDp = move(newDP);
            prevPrefixSum = move(newPrefixSum);
        }
        return (output - prevPrefixSum[k - 1] + mod) % mod;
    }
};