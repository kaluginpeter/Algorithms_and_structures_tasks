# Given an integer n, we can construct a new integer with the following procedure:
#
# For each digit d in n, find the dth prime number. (If d=0, use 1)
# Take the product of these prime numbers. This is our new integer.
# For example, take 25: The 2nd prime is 3, and the 5th is 11. So 25 would evaluate to 3*11 = 33.
#
# If we iterate this procedure, we generate a sequence of integers.
#
# Write a function that, given a positive integer n, returns the maximum value in the sequence starting at n.
#
# Example: 8 -> 19 -> 46 -> 91 -> 46 -> 91 -> ...
# So the maximum here would be 91.
# 0 <= n <= 10^12
#
# PUZZLES
# Solution
from functools import reduce
def find_max(n):
    l = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    s = set()
    while n not in s:
        s.add(n)
        n = reduce(lambda x, d: x * l[int(d)], str(n), 1)
    return max(s)