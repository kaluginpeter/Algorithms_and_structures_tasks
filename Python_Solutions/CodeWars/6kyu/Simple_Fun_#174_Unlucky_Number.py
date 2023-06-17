# Task
# The number is considered to be unlucky if it does not have digits 4 and 7 and is divisible by 13. Please count all unlucky numbers not greater than n.
#
# Example
# For n = 20, the result should be 2 (numbers 0 and 13).
#
# For n = 100, the result should be 7 (numbers 0, 13, 26, 39, 52, 65, and 91)
#
# Input/Output
# [input] integer n
# 1 ≤ n ≤ 10^8(10^6 in Python)
#
# [output] an integer
# PUZZLES
# Solution
def unlucky_number(n):
    return sum((i % 13 == 0 and '4' not in str(i) and '7' not in str(i)) for i in range(n+1))