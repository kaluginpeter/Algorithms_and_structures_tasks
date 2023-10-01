# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.
#
# ARRAYSFUNDAMENTALS
# Solution
def positive_sum(arr):
    # Your code here
    count = 0
    for i in arr:
        if i > 0:
            count += i
    return count