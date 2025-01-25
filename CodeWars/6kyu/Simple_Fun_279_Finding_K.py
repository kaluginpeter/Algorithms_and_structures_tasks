# Task
# Given an array arr, find the maximal value of k such a[i] mod k = a[j] mod k for all valid values of i and j.
#
# If it's impossible to find such number (there's an infinite number of ks), return -1 instead.
#
# Input/Output
# [input] integer array arr
#
# A non-empty array of positive integer.
#
# 2 <= arr.length <= 10
#
# 1 <= arr[i] <= 100
#
# [output] an integer
#
# The maximum value of k or -1 if there is none.
#
# Example
# For arr = [1, 2, 3], the output should be 1.
#
# 1 is the only k which satisfies the given conditions.
#
# For arr = [1, 1, 1], the output should be -1.
#
# 1 % k = 1 for any k > 1, so it's impossible to find the maximum.
#
# For arr = [5, 2, 8], the output should be 3.
#
# 5 % 3 == 2 % 3 == 8 % 3 == 2
#
# Algorithms
# Solution
def finding_k(arr):
    answer: int = -1
    for k in range(1, max(arr)):
        if all(i % k == j % k for i, j in zip(arr, arr[1:])):
            answer = k
    return answer