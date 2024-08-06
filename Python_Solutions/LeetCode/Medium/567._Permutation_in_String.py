# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
#
#
# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.
# Solution Two Pointers Sliding Window Hash Table O(N) O(N)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        storage: dict[str, int] = dict()
        for char in s1:
            storage[char] = storage.get(char, 0) + 1
        k: int = len(s1)
        left: int = 0
        for right in range(len(s2)):
            # Case when letter from s2 not exist in s1
            if s2[right] not in storage:
                while left < right:
                    storage[s2[left]] += 1
                    left += 1
                left += 1
            # Case when letter from s2 exist, but frequence of it letter is exeed
            elif storage[s2[right]] == 0:
                while storage[s2[right]] == 0:
                    storage[s2[left]] += 1
                    left += 1
                storage[s2[right]] -= 1
            # Case when letter from s2 exist in s1
            else: storage[s2[right]] -= 1
            if right - left + 1 == k: return True
        return False