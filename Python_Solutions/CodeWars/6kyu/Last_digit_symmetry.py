# Consider the number 1176 and its square (1176 * 1176) = 1382976. Notice that:
#
# the first two digits of 1176 form a prime.
# the first two digits of the square 1382976 also form a prime.
# the last two digits of 1176 and 1382976 are the same.
# Given two numbers representing a range (a, b), how many numbers satisfy this property within that range? (a <= n < b)
#
# Example
# solve(2, 1200) = 1, because only 1176 satisfies this property within the range 2 <= n < 1200.
# See test cases for more examples. The upper bound for the range will not exceed 1,000,000.
#
# Good luck!
#
# If you like this Kata, please try:
#
# Simple Prime Streaming
#
# Alphabet symmetry
#
# Upside down numbers
#
# ALGORITHMS
# Solution
def solve(a, b):
    l = set([str(i) for i in range(3, 100) if all(i % j != 0 for j in [2] + list(range(3, int(i ** 0.5)+1, 2)))])
    return sum(1 for i in range(max(a, 1000), b) if i % 100 == i*i % 100 and str(i)[:2] in l and str(i*i)[:2] in l)