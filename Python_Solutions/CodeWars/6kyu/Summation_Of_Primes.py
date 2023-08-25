# Summation Of Primes
# The sum of the primes below or equal to 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below or equal to the number passed in.
#
# From Project Euler's Problem #10.
#
# ALGORITHMSMATHEMATICS
# Solution
from gmpy2 import is_prime
def summationOfPrimes(primes):
    return sum(i for i in range(2, primes+1) if is_prime(i))