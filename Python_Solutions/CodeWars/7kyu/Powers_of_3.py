# Given a positive integer N, return the largest integer k such that 3^k < N.
#
# For example,
#
# largest_power(3) == 0
# largest_power(4) == 1
# You may assume that the input to your function is always a positive integer.
#
# MATHEMATICSALGORITHMS
# Solution
def largest_power(N):
    c = 0
    while 3**c < N:
        c += 1
    return c - 1