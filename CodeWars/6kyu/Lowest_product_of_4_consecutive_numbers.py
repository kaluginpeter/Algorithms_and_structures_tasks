# Create a function that returns the lowest product of 4 consecutive digits in a number given as a string.
#
# This should only work if the number has 4 digits or more. If not, return "Number is too small".
#
# Example
# lowest_product("123456789") --> 24 (1x2x3x4)
# lowest_product("35") --> "Number is too small"
# FUNDAMENTALS
# Solution
from operator import mul
from functools import reduce
def lowest_product(input):
    return min(reduce(mul, [*map(int, input)][i:i + 4]) for i in range(0, len(input) - 3)) if len(input) > 3 else "Number is too small"