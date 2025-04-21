# You wrote a program that can calculate the sum of all the digits of a non-negative integer.
#
# However, it's not fast enough. Can you make it faster?
#
# Input size
# Python:
#
# 50 random tests of n <= 2^64
# 50 random tests of n <= 2^120000
# Fundamentals
# Solution
def digit_sum(n):
    return sum(int(d) for d in str(n))