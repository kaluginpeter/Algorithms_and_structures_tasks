# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s == t

# Solution 1 - One HashTable O(N) O(N)
class Solution(object):
    def isAnagram(self, s, t):
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for i in t:
            d[i] = d.get(i, 0) - 1
        for i in d:
            if d[i] != 0:
                return False
        return True
# Solution 2 - Two HashTable O(N) O(N)
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d1, d2 = {}, {}
        for i in s:
            if i  not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in t:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        return d1 == d2
# Solution 3 - Similar Sorting O(N log(N)) O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# Solution 4 - One Liner O(N**2) O(N)
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return all(s.count(i) == t.count(i) for i in t)