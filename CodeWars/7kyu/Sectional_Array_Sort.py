# In this kata you are given an array to sort but you're expected to start sorting from a specific position of the array (in ascending order) and optionally you're given the number of items to sort.
#
# Inputs:
# An array to sort
# The starting index for sorting
# (Optional) The number of items to sort
# If the number of items to sort is not provided or is zero, sort the array from the starting position to the end.
#
# Examples:
# array: [1, 2, 5, 7, 4, 6, 3, 9, 8]
# start: 2
# length: not specified
# expected result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# array: [9, 7, 4, 2, 5, 3, 1, 8, 6]
# start: 2
# length: 5
# expected result: [9, 7, 1, 2, 3, 4, 5, 8, 6]
# ArraysSortingData StructuresAlgorithms
# Solution
def sect_sort(arr: list[int], start: int, bound: int = 0):
    n: int = len(arr)
    if not bound: bound = n
    return arr[:start] + sorted(arr[start:start+bound]) + arr[start+bound:]