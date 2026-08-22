# Xor reduction (medium)
# Given two integers, m and n, return the cumulative xor of all positive integers between them, inclusive. E.g. (0, 6), return 0^1^2^3^4^5^6 => 7.
#
# Constraints:
# 0 <= m < n <= 10^15
#
# Hints
# Try the easy variant first
# Brute-force solutions will likely be rejected due to time-out.
# Read more about xor.
# Look for patterns for successive n values.
# AlgorithmsPuzzles
# Solution
def xor_reduction(m, n):
    def f(k):
        if k < 0: return 0
        mod = k % 4
        if mod == 0: return k
        elif mod == 1: return 1
        elif mod == 2: return k + 1
        return 0

    return f(n) ^ f(m - 1)