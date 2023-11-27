# Given an integer n, add a dot (".") as the thousands separator and return it in string format.
#
#
#
# Example 1:
#
# Input: n = 987
# Output: "987"
# Example 2:
#
# Input: n = 1234
# Output: "1.234"
#
#
# Constraints:
#
# 0 <= n <= 231 - 1
# Solution
class Solution(object):
    def thousandSeparator(self, n):
        if n == 0:
            return '0'
        top, count = '', 0
        while n:
            top = str(n % 10) + top
            count += 1
            n //= 10
            if n:
                if count == 3:
                    top = '.' + top
                    count = 0
        return top
