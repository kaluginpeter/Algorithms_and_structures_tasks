# Task
# Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.
#
# Example
# For n = 152, the output should be 52;
#
# For n = 1001, the output should be 101.
#
# Input/Output
# [input] integer n
#
# Constraints: 10 ≤ n ≤ 1000000.
#
# [output] an integer
#
# PUZZLES
# Solution
def delete_digit(n):
    l = []
    for k, v in enumerate(str(n)):
        l.append(int(str(n).replace(str(n)[k], '', 1)))
    return max(l)