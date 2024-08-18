# Given a string s, find the length of the longest
# substring
#  without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
# Solution Initial solution O(N**2) O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count: int = 0
        ht: dict = dict()
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in ht:
                    ht[s[j]] = 1
                else:
                    count = max(count, len(ht))
                    ht.clear()
                    break
        return count if not ht else max(len(ht), count)
# Solution HashTable and Sliding Window O(N) O(M)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht: dict = dict()
        ans: int = 0
        left: int = 0
        for right in range(len(s)):
            if s[right] not in ht or ht[s[right]] < left:
                ans = max(ans, right - left + 1)
            else:
                left = ht[s[right]] + 1
            ht[s[right]] = right
        return ans


# Solution HashSet Sliding Window O(N) O(M) where is length of unique characters, that in the worst case equals to N
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length: int = 0
        hashset: set[str] = set()
        left: int = 0
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length