# The Padovan sequence is the sequence of integers defined by the initial values
#
# P(0) = P(1) = P(2) = 1
# and the recurrence relation
#
# P(n) = P(n-2) + P(n-3)
# The first few values of P(n) are:
#
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265, ...
# Task
# Your task is to write a method that returns nth Padovan number
#
# ALGORITHMS
# Solution
def padovan(n):
    x = y = z = 1
    for _ in range(n - 2): x, y, z = y, z, x + y
    return z