# Getting the Minimum Absolute Difference
# Task
# Given an array of integers with at least 2 elements: a1, a2, a3, a4, ... aN
#
# The absolute difference between two array elements ai and aj, where i != j, is the absolute value of ai - aj.
#
# Return the minimum absolute difference (MAD) between any two elements in the array.
#
# Example
# For [-10, 0, -3, 1]
#
# the MAD is 1.
#
# Explanation:
#
# | -10 -    0  | = 10
# | -10 -  (-3) | =  7
# | -10 -    1  | = 11
# |   0 - (-10) | = 10
# |   0 -  (-3) | =  3
# |   0 -    1  | =  1
# |  -3 - (-10) | =  7
# |  -3 -    0  | =  3
# |  -3 -    1  | =  4
# |   1 - (-10) | = 11
# |   1 -    0  | =  1
# |   1 -  (-3) | =  4
# The minimum value is 1 ( both | 0 - 1 | and | 1 - 0 | ).
#
# Note
# Note that the same value can appear more than once in the array. In that case, the MAD will be 0.
#
# FUNDAMENTALSARRAYSALGORITHMS
# Solution
def getting_mad(arr):
    cop = list(set(arr))
    if len(cop) != len(arr):
        return 0
    ans: int = float('inf')
    for i in range(len(cop)):
        for j in range(i + 1, len(cop)):
            ans = min(ans, abs(cop[i] - cop[j]))
    return ans if ans < float('inf') else 0