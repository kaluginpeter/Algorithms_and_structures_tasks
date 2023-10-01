# Complete the method which accepts an array of integers, and returns one of the following:
#
# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise
# You can assume the array will always be valid, and there will always be one correct answer.
#
# ARRAYSSORTINGFUNDAMENTALS
# Solution
def is_sorted_and_how(arr):
    if sorted(arr, key = int) == arr:
        return 'yes, ascending'
    elif sorted(arr, key = int, reverse = True) == arr:
        return 'yes, descending'
    return 'no'