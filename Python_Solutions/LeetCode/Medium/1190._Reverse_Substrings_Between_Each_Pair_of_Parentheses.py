# You are given a string s that consists of lower case English letters and brackets.
#
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
# Your result should not contain any brackets.
#
#
#
# Example 1:
#
# Input: s = "(abcd)"
# Output: "dcba"
# Example 2:
#
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.
# Example 3:
#
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
#
#
# Constraints:
#
# 1 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It is guaranteed that all parentheses are balanced.
# Solution Stack
# Note:
# In Python, string is immutable object, so because this solution uses list of alphabet characters for perfomance.
# You can use a whole string, if it mutable in your language.
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
class Solution:
    def reverseParentheses(self, s: str) -> str:
        storage: list[list[str]] = []
        current_substring: list[str] = []
        for char in s:
            if char == '(':
                storage.append(current_substring)
                current_substring = []
            elif char == ')':
                current_substring = storage.pop() + current_substring[::-1]
            else:
                current_substring.append(char)
        return ''.join(current_substring)