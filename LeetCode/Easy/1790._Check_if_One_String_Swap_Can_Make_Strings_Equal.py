# You are given two strings s1 and s2 of equal length. A string swap is an operation
# where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
# Return true if it is possible to make both strings equal by performing at most
# one string swap on exactly one of the strings. Otherwise, return false.
#
# Example 1:
#
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
# Example 2:
#
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
# Example 3:
#
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.
#
# Constraints:
# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.
# Solution
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        for i, j in zip(s1, s2):
            if i not in s2 or s1.count(i) != s2.count(i): return False
            if j not in s1 or s2.count(j) != s1.count(j): return False
            if i != j: c += 1
        return c <= 2

# Python O(N) O(1) Two Pointers
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differ: int = 0
        left = right = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differ += 1
                if left == -1: left = i
                elif right == -1: right = i
        if not differ: return True
        elif differ != 2: return False
        return (s1[left] == s2[right]) and (s1[right] == s2[left])

# C++ O(N) O(1) Two Pointers
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int differ = 0;
        int left = -1, right = -1;
        for (int i = 0; i < s1.size(); ++i) {
            if (s1[i] != s2[i]) {
                ++differ;
                if (left == -1) left = i;
                else if (right == -1) right = i;
            }
        }
        if (!differ) return true;
        if (differ != 2) return false;
        return (s1[right] == s2[left]) && (s1[left] == s2[right]);
    }
};