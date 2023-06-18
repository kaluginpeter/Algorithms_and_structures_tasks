# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Given a string s, return the power of s.
#
# Example 1:
#
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:
#
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
#
# Constraints:
# 1 <= s.length <= 500
# s consists of only lowercase English letters.
# Solution
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        w, count, flag = s[0], 0, False
        for i in range(1, len(s)):
            if s[i] == w[0]:
                w += s[i]
                flag = True
                continue
            if len(w) > count:
                count = len(w)
            w, flag = s[i], False
        if flag:
            count = len(w) if len(w) > count else count
        return count
