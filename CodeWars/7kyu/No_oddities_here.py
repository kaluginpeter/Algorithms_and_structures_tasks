# Write a small function that returns the values of an array that are not odd.
#
# All values in the array will be integers. Return the good values in the order they are given.
#
# ARRAYSFUNDAMENTALS
# Solution
def no_odds(values):
    return [i for i in values if i % 2 == 0]