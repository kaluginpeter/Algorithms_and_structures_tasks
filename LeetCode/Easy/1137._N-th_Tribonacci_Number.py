# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
#
# Example 1:
#
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:
#
# Input: n = 25
# Output: 1389537
#
# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
# Solution
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        a, b, c = 0, 1, 1
        for i in range(n-2): a, b, c = b, c, a + b + c
        return c


# Solution Recursion O(N) O(1)
class Solution:
    def tribonacci(self, n: int, a: int = 0, b: int = 0, c: int = 1) -> int:
        if n == 0:
            return b
        return self.tribonacci(n - 1, b, c, a + b + c)