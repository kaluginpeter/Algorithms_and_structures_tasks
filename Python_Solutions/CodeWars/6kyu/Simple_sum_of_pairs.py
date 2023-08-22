# Given an integer n, find two integers a and b such that:
#
# A) a >= 0 and b >= 0
# B) a + b = n
# C) DigitSum(a) + Digitsum(b) is maximum of all possibilities.
# You will return the digitSum(a) + digitsum(b).
#
# For example:
# solve(29) = 11. If we take 15 + 14 = 29 and digitSum = 1 + 5 + 1 + 4 = 11. There is no larger outcome.
# n will not exceed 10e10.
#
# More examples in test cases.
#
# Good luck!
#
# FUNDAMENTALS
# Solution
def solve(n):
    c = int('0' + '9' * (len(str(n)) - 1))
    return sum(int(i) for i in str(c) + str(n - c))