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