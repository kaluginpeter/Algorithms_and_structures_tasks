# Task
# Given an array of 2k integers (for some integer k), perform the following operations until the array contains only one element:
#
# On the 1st, 3rd, 5th, etc.
# iterations (1-based) replace each pair of consecutive elements with their sum;
# On the 2nd, 4th, 6th, etc.
# iterations replace each pair of consecutive elements with their product.
# After the algorithm has finished, there will be a single element left in the array. Return that element.
#
# Example
# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be 186.
#
# We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so the answer is 186.
#
# Input/Output
# [input] integer array arr
#
# Constraints: 21 ≤ arr.length ≤ 25, -9 ≤ arr[i] ≤ 99.
#
# [output] an integer
#
# Puzzles
# Solution
def array_conversion(arr):
    make_sum: bool = True
    while len(arr) > 1:
        if make_sum:
            arr = [arr[i] + arr[i + 1] for i in range(0, len(arr), 2)]
        else:
            arr = [arr[i] * arr[i + 1] for i in range(0, len(arr), 2)]
        make_sum = not make_sum
    return arr[0]