# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
#
# Example 1:
#
# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:
#
# Input: s = "abcde", goal = "abced"
# Output: false
#
# Constraints:
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.
# Solution
# Python O(N**2) O(N) String
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s == goal:
                return True
            s = s[1:]+s[0]
        return False

# C++ O(N) O(N) String
class Solution {
public:
    bool rotateString(string s, string goal) {
        return s.size() == goal.size() && (s + s).find(goal) != std::string::npos;
    }
};
# Python O(N) O(N) String
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s