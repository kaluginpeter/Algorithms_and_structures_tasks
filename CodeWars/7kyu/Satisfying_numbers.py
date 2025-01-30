# 2520 is the smallest number that can be divided by each of the integers from 1 to 10 without any remainder.
#
# Find the smallest positive number that is evenly divisible by all of the integers from 1 to n, (in this kata,
# 1
# ≤
# n
# ≤
# 40
# 1≤n≤40).
#
# For example:
#
# 5 --> 60      // 1 to 5 can all divide evenly into 60
# 10 --> 2520
# Algorithms
# Solution
from math import lcm
def smallest(n):
    return lcm(*range(1, n + 1))
