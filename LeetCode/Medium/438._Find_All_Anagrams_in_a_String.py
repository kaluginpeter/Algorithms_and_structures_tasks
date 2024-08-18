# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
# Constraints:
#
# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.
# Solution Sliding Window HashTable O(N) O(N)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams: list[int] = []
        # Map of charackters that needed to create anagram of "p"
        needed: dict[str, int] = dict()
        for char in p:
            needed[char] = needed.get(char, 0) + 1
        # Length of valid anagram
        k: int = len(p)
        # Current length of sliding window
        length_window: int = 0
        # Start pointer of sliding window
        left: int = 0
        for right in range(len(s)):
            # If we meet charackter that doesnt exist in "p"
            if s[right] not in needed:
                while left < right:
                    needed[s[left]] += 1
                    left += 1
                    length_window -= 1
                left += 1
            # If we meet correct character, but his frequence is exceed
            elif needed[s[right]] == 0:
                while needed[s[right]] == 0:
                    needed[s[left]] += 1
                    left += 1
                    length_window -= 1
                needed[s[right]] -= 1
                length_window += 1
            # If we meet correct character and have frequence for him
            else:
                needed[s[right]] -= 1
                length_window += 1
            # Check if our length of sliding window is "k"
            if length_window == k:
                anagrams.append(left)

        return anagrams