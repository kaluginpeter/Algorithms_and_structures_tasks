# Given an integer num, return a string of its base 7 representation.
#
# Example 1:
#
# Input: num = 100
# Output: "202"
# Example 2:
#
# Input: num = -7
# Output: "-10"
#
# Constraints:
# -107 <= num <= 107
# Solution
class Solution:
    def convertToBase7(self, num: int) -> str:
        # import numpy
        # return numpy.base_repr(num, 7)
        n, resul = abs(num), ''
        while n:
            resul = str(n % 7) + resul
            n //= 7
        return '-' * (num < 0) + resul or '0'