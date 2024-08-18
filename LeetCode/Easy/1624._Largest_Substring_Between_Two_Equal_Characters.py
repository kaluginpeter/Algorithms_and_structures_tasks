# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
#
# A substring is a contiguous sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:
#
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:
#
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
#
#
# Constraints:
#
# 1 <= s.length <= 300
# s contains only lowercase English letters.
# Solution O(N**2) O(1)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count: int = -1
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    count = max(count, j - i - 1)
        return count
# Solution 2 O(N) O(N)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count: int = -1
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    count = max(count, j - i - 1)
        return count