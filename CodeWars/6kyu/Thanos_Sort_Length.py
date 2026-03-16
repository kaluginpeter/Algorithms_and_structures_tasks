# Thanos Sort Length
# The Mad Titan believes the universe must be perfectly balanced.
#
# Given an array of integers, he repeatedly performs the following operation:
#
# If the current array is sorted in non-decreasing order, he stops.
# Otherwise, he destroys exactly half of the elements.
# The removed elements must form one contiguous half of the array:
#
# either the left half, or
# the right half.
# This process may repeat multiple times.
#
# Your task is not to return the array itself. Instead, you must determine the maximum possible length of a sorted array that can remain after performing these operations optimally.
#
# Implement this function:
#
# def thanos_sort(arr: List[int]) -> int
# that solves this task.
#
# Disclaimer
# The original task was to simply implement thanos sort and return a possible resulting array. However the user can just simply:
#
# thanos_sort=lambda arr: arr[0]
# And since the true thanos sort is random, the user is technically correct. Therefore this kata is no longer the true thanos sort, rather a modified version.
#
# IMPORTANT
# For odd length arrays, include the middle element with the left half.
#
# Example: [1,2,3,6,5] -> [1,2,3] and [6,5]
#
# Examples
# Example 1
# thanos_sort([3, 1, 4, 2]) -> 1
# Explanation
# Possible sequences:
#
# Remove right half → [3,1] → not sorted → snap again → [1]
#
# Remove left half → [4,2] → not sorted → snap again → [2]
#
# The largest sorted result has length 1.
#
# Example 2
# thanos_sort([1, 2, 3, 7, 5, 6]) -> 3
# Explanation
# Removing the right half gives [1,2,3], which is already sorted.
#
# No other sequence yields a longer sorted result.
#
# Constraints
# 0 ≤ len(arr) ≤ 1000
#
# Elements may appear multiple times.
#
# Return 0 for an empty array.
#
# Notes
# A single element is always sorted.
#
# The optimal strategy is not always obvious.
#
# Efficiency does not matter for large inputs.
#
# AlgorithmsArrays