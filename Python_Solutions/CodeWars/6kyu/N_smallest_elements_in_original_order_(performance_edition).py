# This challenge is based on a kata by GiacomoSorbi.
# Before doing this one it is advisable to complete the non-performance version first.
#
# Task
# You will be given an array of integers in a [1; 50] range, and a number n.
# You have to extract n smallest elements out of the array preserving their original order.
#
# Notes
# There will be duplicates in the array, and they have to be returned in the order of their each separate appearence.
# This kata is an example of the "know your data" principle. Remember this while searching for the correct approach.
# Examples
# numbers = [1, 2, 3, 4, 5]
# n = 3
# result = [1, 2, 3]
#
# numbers = [5, 4, 3, 2, 1]
# n = 3
# result = [3, 2, 1]
#
# numbers = [1, 2, 4, 1, 2]
# n = 3
# result = [1, 2, 1]
# ALGORITHMSARRAYSPERFORMANCE
# Solution
def performant_smallest(arr, n):
    return [arr[i] for i in sorted(sorted(range(len(arr)), key=lambda k: arr[k])[:n])]