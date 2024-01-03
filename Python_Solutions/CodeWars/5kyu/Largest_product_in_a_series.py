# Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits in the given string of digits.
#
# For example:
#
# greatestProduct("123834539327238239583") // should return 3240
# The input string always has more than five digits.
#
# Adapted from Project Euler.
#
# MATHEMATICSALGORITHMS
# Solution
import math
def greatest_product(st):
    top: int = 0
    for i in range(len(st) - 4):
        s = math.prod(int(j) for j in st[i:i+5])
        if s > top:
            top = s
    return top