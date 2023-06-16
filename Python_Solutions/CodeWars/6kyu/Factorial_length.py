# In this Kata, you will implement a function count that takes an
# integer and returns the number of digits in factorial(n).
#
# For example, count(5) = 3, because 5! = 120, and 120 has 3 digits.
#
# More examples in the test cases.
#
# Brute force is not possible. A little research will go a long way, as this is a well known series.
#
# Good luck!
#
# Please also try:
#
# ALGORITHMS
# Solution
import math
def count(n):
    if (n < 0): return 0
    if (n <= 1): return 1
    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0))
    return math.floor(x) + 1