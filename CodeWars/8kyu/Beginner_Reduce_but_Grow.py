# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
# FUNDAMENTALSARRAYS
# Solution
def grow(arr):
    integer = 1
    for elem in arr:
        integer *= elem
    return integer