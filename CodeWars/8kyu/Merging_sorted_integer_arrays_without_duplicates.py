# Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.
#
# ARRAYSFUNDAMENTALS
# Solution
def merge_arrays(first, second):
    return sorted(set(first + second))