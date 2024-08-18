# You are given an array with several "even" words, one "odd" word, and some numbers mixed in.
#
# Determine if any of the numbers in the array is the index of the "odd" word. If so, return true, otherwise false.
#
# ALGORITHMS
# Solution
def odd_ball(arr):
    return any(arr[i] == 'odd' for i in [i for i in arr if type(i) == int and i <= len(arr)-1])