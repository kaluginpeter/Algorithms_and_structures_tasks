# Task
# Given a sorted array of integers A, find such an integer x that the value of abs(A[0] - x) + abs(A[1] - x) + ... + abs(A[A.length - 1] - x) is the smallest possible (here abs denotes the absolute value).
#
# If there are several possible answers, output the smallest one.
#
# Example
# For A = [2, 4, 7], the output should be 4.
#
# Input/Output
# [input] integer array A
#
# A non-empty array of integers, sorted in ascending order.
#
# Constraints:
#
# 1 ≤ A.length ≤ 200,
#
# -1000000 ≤ A[i] ≤ 1000000.
#
# [output] an integer
#
# PUZZLES
# Solution
def absolute_values_sum_minimization(lst):
    sm: int = float('inf')
    ans: int = -1
    for i in lst:
        x: int = sum(abs(j - i) for j in lst)
        if x < sm:
            sm, ans = x, i
    return ans