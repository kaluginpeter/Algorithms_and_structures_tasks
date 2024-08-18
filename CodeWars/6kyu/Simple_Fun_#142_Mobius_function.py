# Task
# Compute the Mobius function
# �
# (
# �
# )
# μ(n) for a given value of n.
#
# For a given n, the Mobius function is equal to:
#
# 0 if n is divisible by the square of any prime number. For example n = 4, 8, 9 are all divisible by the square of at least one prime number.
#
# 1 if n is not divisible by the square of any prime numbers, and has an even number of prime factors. For example n = 6, 10, 21 satisfy these conditions (e.g. 21 = 3 * 7 so it has an even number (2) of distinct prime factors and is not divisible by the square of any prime numbers).
#
# -1 otherwise. For example n = 3, 5, 7, 30.
#
# Input/Output
# You will be given an integer n; you must return an integer - the Mobius function of n.
#
# Performance requirements:
#
# 2 <= n <= 1e12
#
# PUZZLES
# Solution
from gmpy2 import is_prime
def mobius(n):
  c = 0
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:
      if is_prime(i):
        if n % (i*i) == 0:return 0
        c += 1
      n = n // i
      if is_prime(n):
        c += 1
        break
  if c > 0 and c % 2 == 0:return 1
  return -1