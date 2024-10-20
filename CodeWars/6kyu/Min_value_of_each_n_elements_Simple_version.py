# When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said
#
# Description:
# Complete the function. Two arguments will be given:
#
# arr: An array that contains some integers(positve,negative or zero).
# n: A positive integer. n <= arr.length.
# Your task is to find the minimum value of each n adjacent elements in arr. Returns by a new array. For example:
#
# arr = [1,2,3,10,-5], n = 2   ==>  [1,2,3,-5]
# # The min value of each 2 adjacent elements are:
# [(1,2)...] --> 1,
# [.(2,3)..] --> 2
# [..(3,10).] --> 3
# [...(10,-5)] --> -5
# Some Examples
# [1,-2,3,-4,5,-6,7,8], 1  ==>  [1,-2,3,-4,5,-6,7,8]
# [1,-2,3,-4,5,-6,7,8], 2  ==>  [-2,-2,-4,-4,-6,-6,7]
# [1,-2,3,-4,5,-6,7,8], 3  ==>  [-2,-4,-4,-6,-6,-6]
# [1,-2,3,-4,5,-6,7,8], 4  ==>  [-4,-4,-6,-6,-6]
# Note:
#
# You can assume that all inputs are valid.
# This is a simple version, please look forward to the challenge version ;-)
# A bit difficulty, A bit of fun, happy coding ;-)
# ALGORITHMSPUZZLES
# Solution
from collections import deque
def min_value(arr, window_size):
    n: int = len(arr)
    result: list[int] = []
    dq: list[int] = deque()

    for i in range(n):
        if dq and dq[0] < i - window_size + 1:
            dq.popleft()
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()
        dq.append(i)
        if i >= window_size - 1:
            result.append(arr[dq[0]])
    return result