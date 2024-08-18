# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.
# Solution Stack O(N) O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack: list[int] = list()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        ans: list[str] = list()
        for i in range(len(s)):
            if stack and i != stack[0]:
                ans.append(s[i])
            elif stack:
                stack.pop(0)
            else:
                ans.append(s[i])
        return ''.join(ans)