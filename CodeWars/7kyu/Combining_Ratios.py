# 2 ratios given as strings in the form A:B and B:C
#
# eg 12:4 3:7
#
# Your program must return the ratio of A:B:C in simplest form
#
# eg 12:4 3:7 ---> 9:3:7
#
# Given Ratios are not in simplest form A,B and C are always in the range of 1 --> 1e5
#
# return as a string in the format "9:3:7"
#
# For a harder version goto this kata
# Solution
from math import gcd


def merge_ratios(ratio1, ratio2):
    a, b1 = map(int, ratio1.split(":"))
    b2, c = map(int, ratio2.split(":"))
    lcm = b1 * b2 // gcd(b1, b2)
    m1 = lcm // b1
    m2 = lcm // b2
    a *= m1
    b = lcm
    c *= m2
    g = gcd(gcd(a, b), c)
    return f"{a // g}:{b // g}:{c // g}"