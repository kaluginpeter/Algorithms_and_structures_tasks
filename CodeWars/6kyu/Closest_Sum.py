# Given an array (ints) of n integers, find three integers
# in arr such that the sum is closest to a given number (num), target.
#
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# closest_sum([-1, 2, 1, -4], 1) # 2 (-1 + 2 + 1 = 2)
# Note: your solution should not modify the input array.
#
# FUNDAMENTALS
# Solution
from itertools import combinations
def closest_sum(ints, num):
    return sum(min(combinations(ints, 3), key=lambda x: abs(num - sum(x))))