# Write a function generator that will generate the first n primes grouped in tuples of size m. If there are not enough primes for the last tuple it will have the remaining values as None.
#
# Examples
# For n = 11 and m = 2:
# (2, 3), (5, 7), (11, 13), (17, 19), (23, 29), (31, None)
#
# For n = 11 and m = 3:
# (2, 3, 5), (7, 11, 13), (17, 19, 23), (29, 31, None)
#
# For n = 11 and m = 5:
# (2, 3, 5, 7, 11), (13, 17, 19, 23, 29), (31, None, None, None, None)
#
# For n = 3 and m = 1:
# (2,), (3,), (5,)
# Note: large numbers of n will be tested, up to 50000
#
# AlgorithmsFundamentals
# Solution
from gmpy2 import is_prime
def get_primes(n, m=2):
    primes: list[int] = []
    num: int = 2
    p: int = 0
    while p < n:
        if is_prime(num):
            p += 1
            primes.append(num)
            if len(primes) == m:
                yield tuple(primes)
                primes.clear()
        num += 1
    if n % m != 0:
        primes.extend([None] * (max(0, m - len(primes))))
        yield tuple(primes)