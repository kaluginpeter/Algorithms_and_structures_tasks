# Consider the following series:
#
# 1, 2, 4, 8, 16, 22, 26, 38, 62, 74, 102, 104, 108, 116, 122
#
# It is generated as follows:
#
# For single digit integers, add the number to itself to get the next element.
# For other integers, multiply all the non-zero digits and add the result to the original number to get the next element.
# For example: 16 + (6 * 1) = 22 and 104 + (4 * 1) = 108.
#
# Let's begin the same series with a seed value of 3 instead of 1:
#
# 3, 6, 12, 14, 18, 26, 38, 62, 74, 102, 104, 108, 116, 122
#
# Notice that the two sequences converge at 26 and are identical therefter. We will call the series seeded by a value of 1 the "base series" and the other series the "test series".
#
# Let's look another test series that starts with 15
#
# 15, 20, 22, 26, 38, 62, 74, 102, 104, 108, 116, 122
#
# The sequences converge at 22 if the test series starts with 15
#
# You will be given a seed value for the test series and your task will be to return the number of integers that have to be generated in the test series before it converges to the base series. In the case above:
#
# convergence(3) = 5, the length of [3, 6, 12, 14, 18].
# convergence(15) = 2, the length of [15, 20].
# Good luck!
#
# If you like this Kata, please try:
#
# Simple Prime Streaming
#
# Unique digit sequence
#
# Divisor harmony
#
# ALGORITHMS
# Solution
from math import prod
def generate(x: int) -> int:
    if x < 10:
        return x * 2
    return x + prod(i for i in map(int, str(x)) if i > 0)
def convergence(n):
    base: int = 1
    ans_ln: int = 0
    while base != n:
        while base < n:
            base = generate(base)
        while n < base:
            ans_ln += 1
            n = generate(n)
    return ans_ln