# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
# and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
# Solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        try:
            for i in s:
                t = t[t.index(i)+1:]
            return True
        except:
            return False

# Solution 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if s:
                if t[i] == s[0]:
                    s = s[1:]
        return len(s) == 0
# Solution 3 Two Pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x, y = 0, 0
        while x < len(s) and y < len(t):
            if t[y] == s[x]:
                x += 1
            y += 1
        return x == len(s)