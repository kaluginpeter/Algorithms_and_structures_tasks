# Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
#
# An integer m is a divisor of n if there exists an integer k such that n = k * m.
#
#
#
# Example 1:
#
# Input: n = 2
# Output: false
# Explantion: 2 has only two divisors: 1 and 2.
# Example 2:
#
# Input: n = 4
# Output: true
# Explantion: 4 has three divisors: 1, 2, and 4.
#
#
# Constraints:
#
# 1 <= n <= 104
# Solution 1 Speed O(N // 2) Memory O(1)
class Solution(object):
    def isThree(self, n):
        count = 1
        for i in range(1, n // 2 + 1):
            top = 1
            while i * top < n:
                top += 1
            if top * i == n:
                count += 1
        return count == 3

# Solution 2 Speed O(log(N)) Memory O(1)
class Solution(object):
    def isThree(self, n):
        limit, count = n, 0
        for i in range(1, limit):
            if n % i == 0:
                limit = n / i
                if limit != i:
                    count += 1
                count += 1
        return count == 3