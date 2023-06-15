# Backwards Read Primes are primes that when read backwards
# in base 10 (from right to left) are a different prime. (This rules out primes which are palindromes.)
#
# Examples:
# 13 17 31 37 71 73 are Backwards Read Primes
# 13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.
#
# Task
# Find all Backwards Read Primes between two positive given numbers (both inclusive),
# the second one always being greater than or equal to the first one.
# The resulting array or the resulting string will be ordered following the natural order of the prime numbers.
#
# Examples (in general form):
# backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97]
# backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967] backwardsPrime(501, 599) => []
#
# See "Sample Tests" for your language.
#
# Notes
# Forth Return only the first backwards-read prime between start and end or 0 if you don't find any
# Ruby Don't use Ruby Prime class, it's disabled.
# MATHEMATICSALGORITHMS
# Solution
from gmpy2 import is_prime
def backwards_prime(start, stop):
    l = []
    for i in range(start, stop+1):
        if is_prime(i) and is_prime(int(str(i)[::-1])) and str(i) != str(i)[::-1]: l.append(i)
    return l