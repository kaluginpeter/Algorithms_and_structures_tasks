# Task
# Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.
#
# Given an integer n, find its digit degree.
#
# Example
# For n = 5, the output should be 0;
#
# For n = 100, the output should be 1;
#
# For n = 91, the output should be 2.
#
# Input/Output
# [input] integer n
#
# Constraints: 5 ≤ n ≤ 109.
#
# [output] an integer
#
# Puzzles
# Solution
def digit_degree(n):
    degree: int = 0
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
        degree += 1
    return degree