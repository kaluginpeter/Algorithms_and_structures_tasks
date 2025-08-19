# An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".
#
# For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
# Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.
#
#
#
# Example 1:
#
# Input: s = "abacaba"
# Output: 2
# Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
# "ab" is the longest continuous substring.
# Example 2:
#
# Input: s = "abcde"
# Output: 5
# Explanation: "abcde" is the longest continuous substring.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only English lowercase letters.
#
# Solution
# Python O(N) O(1) TwoPointers Greedy
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        output: int = 0
        left: int = 0
        for right in range(len(s)):
            if ord(s[right]) - ord(s[right - 1 if right else 0]) != 1: left = right
            output = max(output, right - left + 1)
        return output

# C++ O(N) O(1) TwoPointers Greedy
class Solution {
public:
    int longestContinuousSubstring(string s) {
        int output = 0, left = 0;
        for (int right = 0; right < s.size(); ++right) {
            if (s[right] - s[(right ? right - 1 : 0)] != 1) left = right;
            output = std::max(output, right - left + 1);
        }
        return output;
    }
};