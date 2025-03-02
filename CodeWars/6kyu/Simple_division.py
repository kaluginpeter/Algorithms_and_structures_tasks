# In this Kata, you will be given two numbers, a and b, and your task is to determine if the first number a is divisible by all the prime factors of the second number b. For example: solve(15,12) = False because 15 is not divisible by all the prime factors of 12 (which include2).
#
# See test cases for more examples.
#
# Good luck!
#
# If you like this Kata, please try:
#
# Sub-array division
#
# Divisor harmony
#
# Fundamentals
# Solution
def solve(a,b):
    primes: list[int] = []
    while b & 1 == 0:
        if not primes: primes.append(2)
        b //= 2
    bound: int = int(b**.5) + 1
    for d in range(3, bound + 1, 2):
        while b % d == 0:
            if not primes or primes[-1] != d:
                primes.append(d)
            b //= d
    if b > 2:
        primes.append(b)
    return all(a % prime == 0 for prime in primes)