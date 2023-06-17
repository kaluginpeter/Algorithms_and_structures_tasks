# Define a "prime prime" number to be a rational number written as one prime number over another
# prime number: primeA / primeB (e.g. 7/31)
#
# Given a whole number N / n, generate the number of "prime prime" rational numbers less than 1,
# using only prime numbers between 0 and N / n(non inclusive).
#
# Return the count of these "prime primes", and the integer part of their sum.
#
# Example
# N = 6
#
# # The "prime primes" less than 1 are:
# 2/3, 2/5, 3/5               # count: 3
#
# 2/3 + 2/5 + 3/5 = 1.6667    # integer part: 1
#
# Thus, the function should return 3 and 1.
# ALGORITHMS
# Solution
from gmpy2 import is_prime
import itertools
def prime_primes(N):
    primes = [2] + [i for i in range(3, 1000, 2) if is_prime(i)]
    pairs = list(itertools.combinations((i for i in primes if i < N), 2))
    return len(pairs), int(sum(a/b for a, b in pairs))