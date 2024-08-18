# Task
# Given an array of numbers and an index, return either the index of the smallest number that is larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).
#
# Notes
# Multiple correct answers may be possible. In this case, return any one of them.
# The given index will be inside the given array.
# The given array will, therefore, never be empty.
#
# Example
# least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
# least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
# ALGORITHMSARRAYS
# Solution
def least_larger(a, i):
    top, ans = float('inf'), -1
    for x in range(len(a)):
        if a[x] > a[i]:
            if top > abs(a[i] - a[x]):
                top, ans = abs(a[i] - a[x]), x
    return ans