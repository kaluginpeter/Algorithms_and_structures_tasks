# You are given a string s consisting of lowercase English letters.
#
# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
#
# Return the length of the longest balanced substring of s.
#
#
#
# Example 1:
#
# Input: s = "abbac"
#
# Output: 4
#
# Explanation:
#
# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.
#
# Example 2:
#
# Input: s = "zzabccy"
#
# Output: 4
#
# Explanation:
#
# The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​
#
# Example 3:
#
# Input: s = "aba"
#
# Output: 2
#
# Explanation:
#
# ​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".
#
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# Solution
# Python O(N^2) O(D) BruteForce
class Solution:
    def longestBalanced(self, s: str) -> int:
        output: int = 1
        n: int = len(s)
        for i in range(n):
            hashmap: list[int] = [0] * 26
            mx: int = 0
            for j in range(i, n):
                hashmap[ord(s[j]) - 97] += 1
                mn: int = n
                for freq in hashmap:
                    if not freq: continue
                    if freq < mn: mn = freq
                    if freq > mx: mx = freq
                if mn == mx: output = max(output, j - i + 1)
        return output

# C++ O(N^2) O(D) BruteForce
class Solution {
public:
    int longestBalanced(string s) {
        size_t output = 1, n = s.size();
        for (size_t i = 0; i < n; ++i) {
            std::array<int, 26> hashmap{};
            int mx = INT32_MIN;
            for (size_t j = i; j < n; ++j) {
                ++hashmap[s[j] - 'a'];
                int mn = INT32_MAX;
                for (auto& freq : hashmap) {
                    if (!freq) continue;
                    if (freq < mn) mn = freq;
                    if (freq > mx) mx = freq;
                }
                if (mn == mx) output = std::max(output, j - i + 1);
            }
        }
        return output;
    }
};