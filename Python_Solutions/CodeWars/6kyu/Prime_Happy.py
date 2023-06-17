# A number n is called prime happy if there is at least one prime
# less than n and the sum of all primes less than n is evenly divisible by n.
# Write isPrimeHappy(n) which returns true if n is prime happy else false.
#
# FUNDAMENTALS
# Solution
from gmpy2 import is_prime
def is_prime_happy(n):
    if n < 5: return False
    return sum([i for i in range(2, n) if is_prime(i)]) % n == 0