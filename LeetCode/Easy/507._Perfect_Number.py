# A perfect number is a positive integer that is equal to the sum of its positive divisors,
# excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.
#
# Example 1:
#
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
# Example 2:
#
# Input: num = 7
# Output: false
#
# Constraints:
# 1 <= num <= 108
# Solution
import math
class Solution:
    def checkPerfectNumber(self, num):
        if num<=1:
            return False
        scale=int(math.sqrt(num))
        ans=1
        for i in range(2,scale+1):
            if num % i==0:
                ans+=i+num/i
        return num == ans