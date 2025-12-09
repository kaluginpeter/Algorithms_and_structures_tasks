# Sorting Singularly Nested Lists by Depth
# You are given a list of lists, where each subarray can either be an empty list or contain one next nested list. Your task is to sort the main list in ascending order based on the depth of these subarrays.
#
# Input:
#
# You will receive an array of arrays (a list of lists).
# Each sub-array can only contain either another array or nothing (empty)
# Main array might be completely empty
# Understanding Depth
#
# The depth is zero-based:
#
# The elements in the main array have depth 1.
# A single nested empty array ([[]]) has depth 2.
# A double-nested empty array ([[[]]]) has depth 3, and so on.
# Examples:
#
# [ [[[[[]]]]], [[]], [], [[[]]], []]  -> [ [], [], [[]], [[[]]], [[[[[]]]]] ]
#
# [] has a depth of 1
# [[]] has a depth of 2
# [[[]]] has a depth of 3
# [[[[[]]]]] has a depth of 5
# [ [[]], [], [], [] , [[[[[[[]]]]]]], [], [[]] , [[[]]], [] ]  -> [ [], [], [], [], [], [[]], [[]], [[[]]], [[[[[[[]]]]]]] ]
#
# [ [[]], [] ] -> [[], [[]] ]
#
# The final sorted order places the shallowest subarrays first and the deepest last.
#
# ListsArraysSorting