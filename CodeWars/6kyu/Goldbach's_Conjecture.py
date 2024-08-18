# Goldbach's conjecture is amongst the oldest and well-known unsolved
# mathematical problems out there. In correspondence with Leonhard Euler in 1742,
# German mathematician Christian Goldbach made a conjecture stating that:
#
# "Every even integer greater than 2 can be written as the sum of two primes"
#
# which is known today as the (strong) Goldbach's conjecture.
#
# Even though it's been thoroughly tested and analyzed and seems to be true, it hasn't been
# proved yet (thus, remaining a conjecture.)
#
# Your task is to implement the function in the starter code, taking into account the following:
#
# If the argument isn't even and greater than two, return an empty array/tuple.
# For arguments even and greater than two, return a two-element array/tuple with two prime
# numbers whose sum is the given input.
# The two prime numbers must be the farthest ones (the ones with the greatest difference)
# The first prime number must be the smallest one.
# A few sample test cases:
#
# checkGoldbach(2)/check_goldbach(2) should return []
#
# checkGoldbach(5)/check_goldbach(5) should return []
#
# checkGoldbach(4)/check_goldbach(4) should return [2, 2]
#
# checkGoldbach(6)/check_goldbach(6) should return [3, 3]
#
# checkGoldbach(14)/check_goldbach(14) should return [3, 11]
#
# ALGORITHMSNUMBER THEORY
# Solution
from gmpy2 import is_prime
def check_goldbach(n):
    if n <= 2 or n % 2 != 0: return []
    l = [i for i in range(2, n) if is_prime(i)]
    for i in l:
        for j in l:
            if i + j == n: return [i, j]