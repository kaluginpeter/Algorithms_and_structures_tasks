# Given a string s, return the maximum length of a
# substring
#  such that it contains at most two occurrences of each character.
#
#
# Example 1:
#
# Input: s = "bcbbbcba"
#
# Output: 4
#
# Explanation:
#
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:
#
# Input: s = "aaaa"
#
# Output: 2
#
# Explanation:
#
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
#
#
# Constraints:
#
# 2 <= s.length <= 100
# s consists only of lowercase English letters.
# Solution Sliding Window O(N) O(N)
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans: int = 0
        ht: dict = dict()
        left: int = 0
        for right in range(len(s)):
            ht[s[right]] = ht.get(s[right], 0) + 1
            while ht[s[right]] > 2:
                ht[s[left]] -= 1
                left += 1
            ans = max(ans, right + 1 - left)
        return ans