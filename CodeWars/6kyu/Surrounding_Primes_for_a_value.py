# We need a function prime_bef_aft() that gives the largest prime below a certain given value n,
#
# befPrime or bef_prime (depending on the language),
#
# and the smallest prime larger than this value,
#
# aftPrime/aft_prime (depending on the language).
#
# The result should be output in a list like the following:
#
# prime_bef_aft(n) == [befPrime, aftPrime]
# If n is a prime number it will give two primes, n will not be included in the result.
#
# Let's see some cases:
#
# prime_bef_aft(100) == [97, 101]
#
# prime_bef_aft(97) == [89, 101]
#
# prime_bef_aft(101) == [97, 103]
# Range for the random tests: 1000 <= n <= 200000
#
# (The extreme and special case n = 2 will not be considered for the tests. Thanks Blind4Basics)
#
# Happy coding!!
#
# FUNDAMENTALSMATHEMATICS
# Solution
from gmpy2 import is_prime, next_prime
def prime_bef_aft(i):
    return [next(filter(is_prime, range(i-1, 1, -1))), next_prime(i)]