# An array is called zero-balanced if its elements sum to 0 and for each positive element n, there exists another element that is the negative of n. Write a function named ìsZeroBalanced that returns true if its argument is zero-balanced array, else return false. Note that an empty array will not sum to zero.
#
# ARRAYSFUNDAMENTALS
# Solution
def is_zero_balanced(arr):
    return sum(arr) == 0 and all(abs(i) in arr if i < 0 else -i in arr for i in arr) if len(arr) > 0 else False