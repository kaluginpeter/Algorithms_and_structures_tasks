# In this Kata, you will be given a number and your task will be to return the nearest prime number.
#
# solve(4) = 3. The nearest primes are 3 and 5. If difference is equal, pick the lower one.
# solve(125) = 127
# We'll be testing for numbers up to 1E10. 500 tests.
#
# More examples in test cases.
#
# Good luck!
#
# If you like Prime Katas, you will enjoy this Kata: Simple Prime Streaming
#
# ALGORITHMS
# Solution
from gmpy2 import is_prime
def solve(n, i=0):
    return is_prime(n-i) and n-i or is_prime(n+i) and n+i or solve(n,i+1)