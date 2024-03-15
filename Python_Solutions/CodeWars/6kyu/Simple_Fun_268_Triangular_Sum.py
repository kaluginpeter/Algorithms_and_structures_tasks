# Task
# Triangular numbers are defined by the formula n * (n + 1) / 2 with n starting from 1. They count the number of objects that can form an equilateral triangle as shown in the picture below:
#
#
#
# So the sequence of triangular numbers begins as follows:
#
# 1, 3, 6, 10, 15, 21, 28, ....
#
# It is proven that the sum of squares of any two consecutive triangular numbers is equal to another triangular number.
#
# You're given a triangular number n. Return true if it can be represented as a sum of squares of two consecutive triangular numbers, or false otherwise.
#
# Input/Output
# [input] integer n
#
# A positive triangular number
#
# 3 ≤ n ≤ 10^9
#
# [output] a boolean value
#
# true if it is possible to represent n as the sum of squares of two consecutive triangular numbers, and false otherwise.
#
# Example
# For n = 6, the output should be false.
#
# No two squared consecutive triangular numbers add up to 6.
#
# For n = 45, the output should be true.
#
# 3 * 3 + 6 * 6 = 9 + 36 = 45
#
# PUZZLES
# Solution
def triangular_sum(n):
    k = 1
    T_k = k * (k + 1) // 2
    while True:
        T_next = (k + 1) * (k + 2) // 2
        sum_of_squares = T_k**2 + T_next**2
        if sum_of_squares == n:
            return True
        if sum_of_squares > n:
            return False
        k += 1
        T_k = T_next