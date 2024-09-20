# You are given a string s. You can convert s to a
# palindrome
#  by adding characters in front of it.
#
# Return the shortest palindrome you can find by performing this transformation.
#
#
#
# Example 1:
#
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
#
# Input: s = "abcd"
# Output: "dcbabcd"
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.
# Solution
# Python O(N) O(N) Knuth Morris Pratt String Matching
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        concatenated_s: str = s + '#' + s[::-1]
        pattern: list[int | None] = [None] * len(concatenated_s)
        left, right = 0, 1
        while right < len(concatenated_s):
            if concatenated_s[left] == concatenated_s[right]:
                pattern[right] = left
                left, right = left + 1, right + 1
            elif left and pattern[left - 1] is not None:
                left = pattern[left - 1] + 1
            elif left: left = 0
            else: right += 1
        if pattern[-1] is None:
            return ''
        pattern_length: int = len(s) - pattern[-1] - 1
        return s[::-1][:pattern_length] + s