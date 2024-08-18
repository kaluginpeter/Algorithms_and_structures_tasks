# The number 23 is special in the sense that all of its digits are prime numbers. Furthermore, it's a prime itself. There are 4 such numbers between 10 and 100: 23, 37, 53, 73. Let's call these numbers "total primes".
#
# Complete the function that takes a range (a, b) and returns the number of total primes within that range (a <= primes < b). The test ranges go up to 107.
#
# Examples
# (10, 100)  ==> 4  # 23, 37, 53, 73
# (500, 600) ==> 3  # 523, 557, 577
# Happy coding!
#
# MATHEMATICSALGORITHMS
# Solution
import gmpy2
import itertools
import math
def get_total_primes(a, b):
    l, c = [], 0
    for i in range(math.ceil(math.log10(a)),math.ceil(math.log10(b))+1):
        l += list(map("".join, itertools.product('2357',repeat = i)))
    for i in l:
        if gmpy2.is_prime(int(i)) and int(i) < b and int(i) >= a: c += 1
    return c