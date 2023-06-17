# Definition (Primorial Of a Number)
# Is similar to factorial of a number, In primorial, not all the
# natural numbers get multiplied, only prime numbers are multiplied
# to calculate the primorial of a number. It's denoted with P# and it is the product of the first n prime numbers.
#
# Task
# Given a number N , calculate its primorial.!alt!alt
# Notes
# Only positive numbers will be passed (N > 0) .
# Input >> Output Examples:
# 1- numPrimorial (3) ==> return (30)
# Explanation:
# Since the passed number is (3) ,Then the primorial should obtained by multiplying 2 * 3 * 5 = 30 .
#
# Mathematically written as , P3# = 30 .
# 2- numPrimorial (5) ==> return (2310)
# Explanation:
# Since the passed number is (5) ,Then the primorial should obtained by multiplying  2 * 3 * 5 * 7 * 11 = 2310 .
#
# Mathematically written as , P5# = 2310 .
# 3- numPrimorial (6) ==> return (30030)
# Explanation:
# Since the passed number is (6) ,Then the primorial should obtained by multiplying  2 * 3 * 5 * 7 * 11 * 13 = 30030 .
#
# Mathematically written as , P6# = 30030 .
# Playing with Numbers Series
# Playing With Lists/Arrays Series
# For More Enjoyable Katas
# ALL translations are welcomed
# Enjoy Learning !!
# Zizou
# FUNDAMENTALSARRAYSNUMBER THEORY
# Solution
import functools
def num_primorial(n):
    def sieveOfEratosthenes(n):
        if n <= 2:
            return []
        sieve = list(range(3, n, 2))
        top = len(sieve)
        for si in sieve:
            if si:
                bottom = (si*si - 3) // 2
                if bottom >= top:
                    break
                sieve[bottom::si] = [0] * -((bottom - top) // si)
        return [2] + [el for el in sieve if el]
    return functools.reduce(lambda a, b: a*b, sieveOfEratosthenes(10000)[:n])