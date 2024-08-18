# Given a sorted array of distinct integers, write a function index_equals_value that returns the lowest index for which array[index] == index.
# Return -1 if there is no such index.
#
# Your algorithm should be very performant.
#
# [input] array of integers ( with 0-based nonnegative indexing )
# [output] integer
#
# Examples:
# input: [-8,0,2,5]
# output: 2 # since array[2] == 2
#
# input: [-1,0,3,6]
# output: -1 # since no index in array satisfies array[index] == index
# Random Tests Constraints:
# Array length: 200 000
#
# Amount of tests: 1 000
#
# Time limit: 1.5 s
#
# If you liked this Kata check out my more complex creations:
#
# Find the neighbourhood in big dimensions. Neighbourhood collection
#
# The Rubik's cube
#
# ARRAYSALGORITHMS
# Solution O(logN) O(1) Binary Search
def index_equals_value(arr):
    left, right = 0, len(arr) - 1
    ans: int = -1
    while left <= right:
        middle = (left + right) // 2
        if middle == arr[middle]:
            ans = middle
            right = middle - 1
        elif middle > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return ans