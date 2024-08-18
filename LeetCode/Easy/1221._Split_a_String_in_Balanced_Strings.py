# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s, split it into some number of substrings such that:
#
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.
#
#
#
# Example 1:
#
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:
#
# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
# Example 3:
#
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
#
#
# Constraints:
#
# 2 <= s.length <= 1000
# s[i] is either 'L' or 'R'.
# s is a balanced string.
# Solutions
# Solution 1 by Stack
class Solution(object):
    def balancedStringSplit(self, s):
        stack, count, top = [], 0, s[0]
        for i in range(len(s)):
            if len(stack) == 0:
                count += 1
                top = s[i]
            if s[i] == top:
                stack.append(s[i])
            elif len(stack) != 0:
                stack.pop()
        return count
# Solution 2 by count (best solution)
class Solution(object):
    def balancedStringSplit(self, s):
        top, count = 0, 0
        for i in range(len(s)):
            if s[i] == 'L':
                top += 1
            else:
                top -= 1
            if top == 0:
                count += 1
        return count
# Solution 3 - My initial solution
class Solution(object):
    def balancedStringSplit(self, s):
        count, left, right = 0, 0, 0
        for i in s:
            if i == 'R':
                right += 1
            else:
                left += 1
            if left == right:
                count += 1
                left = 0
                right = 0
        return count