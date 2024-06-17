# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
#
#
#
# Example 1:
#
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
#
# Input: c = 3
# Output: false
#
#
# Constraints:
#
# 0 <= c <= 231 - 1
# Solution Binary Search Math O(sqrt(N)) O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**.5) + 1
        while left <= right:
            sm: int = left**2 + right**2
            if sm == c:
                return True
            elif sm > c:
                right -= 1
            else:
                left += 1
        return False