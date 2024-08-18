# Consider an array that has no prime numbers, and none of its elements
# has any prime digit. It would start with: [1,4,6,8,9,10,14,16,18,40,44..].
#
# 12 and 15 are not in the list because 2 and 5 are primes.
#
# You will be given an integer n and your task will be return the number at that index in the array. For example:
#
# solve(0) = 1
# solve(2) = 6
# More examples in the test cases.
#
# Good luck!
#
# If you like Prime Katas, you will enjoy this Kata: Simple Prime Streaming
#
# ALGORITHMS
# Solution
from gmpy2 import is_prime
def solve(n):
    l = []
    c = 1
    while len(l) <= n:
        if not is_prime(c) and all(not is_prime(int(i)) for i in str(c)): l.append(c)
        c += 1
    return l[n]