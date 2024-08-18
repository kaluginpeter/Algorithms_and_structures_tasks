# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#
# Return your answer as a number.
#
# FUNDAMENTALSSTRINGSARRAYS
# Solution
def sum_mix(arr):
    count = 0
    for elem in arr:
        count += int(elem)
    return count