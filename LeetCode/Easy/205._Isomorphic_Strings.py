# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
#
# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.
# Solution
from collections import Counter
# Solution One Liner O(N**2) O(N)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(x) for x in s] == [t.index(y) for y in t]

# Solution HashTable O(N) O(N)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ht1, ht2 = dict(), dict()
        for i in range(len(s)):
            if ht1.get(s[i], 0) != ht2.get(t[i], 0):
                return False
            if (s[i] == s[max(i - 1, 0)] and t[i] != t[max(i - 1, 0)]) or (s[i] != s[max(i - 1, 0)] and t[i] == t[max(i - 1, 0)]):
                return False
            ht1[s[i]] = i
            ht2[t[i]] = i
        return ht1.get(s[-1], 0) == ht2.get(t[-1], 0)