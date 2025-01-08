# You are given a string s and a pattern string p, where p contains exactly one '*' character.
#
# The '*' in p can be replaced with any sequence of zero or more characters.
#
# Return true if p can be made a
# substring
#  of s, and false otherwise.
#
#
#
# Example 1:
#
# Input: s = "leetcode", p = "ee*e"
#
# Output: true
#
# Explanation:
#
# By replacing the '*' with "tcod", the substring "eetcode" matches the pattern.
#
# Example 2:
#
# Input: s = "car", p = "c*v"
#
# Output: false
#
# Explanation:
#
# There is no substring matching the pattern.
#
# Example 3:
#
# Input: s = "luck", p = "u*"
#
# Output: true
#
# Explanation:
#
# The substrings "u", "uc", and "uck" match the pattern.
#
#
#
# Constraints:
#
# 1 <= s.length <= 50
# 1 <= p.length <= 50
# s contains only lowercase English letters.
# p contains only lowercase English letters and exactly one '*'
# Solution
# Python O(N) O(1) Greedy
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        first, second = p.split('*')
        return first in s and second in s[s.index(first) + len(first):]

# C++ O(1) O(1) Greedy
class Solution {
public:
    bool hasMatch(string s, string p) {
        std::string first = "";
        std::string second = "";
        bool afterStar = false;
        for (char& letter : p) {
            if (letter == '*') {
                afterStar = true;
            } else if (afterStar) {
                second += letter;
            } else {
                first += letter;
            }
        }
        int index = s.find(first);
        return index != std::string::npos && s.find(second, index + first.size()) != std::string::npos;
    }
};