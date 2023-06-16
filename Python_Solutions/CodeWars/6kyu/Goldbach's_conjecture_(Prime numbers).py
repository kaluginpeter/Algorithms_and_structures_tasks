# Goldbach's conjecture is one of the oldest and best-known unsolved
# problems in number theory and all of mathematics. It states:
#
# Every even integer greater than 2 can be expressed as the sum of two primes. For example:
#
# 6 = 3 + 3
# 8 = 3 + 5
# 10 = 3 + 7 = 5 + 5
# 12 = 5 + 7
#
# Some rules for the conjecture:
#
# pairs should be descending like [3,5] not [5,3]
#
# all pairs should be in ascending order based on the first element of the pair: [[5, 13], [7, 11]] is accepted
# but [[7, 11],[5, 13]] is not accepted.
#
# Write the a function that find all identical pairs of prime numbers:
#
# def goldbach(even_number)
# You should return an array of containing pairs of primes, like:
#
# [[5, 13], [7, 11]]  # even_number = 18
# or
#
# [[3, 31], [5, 29], [11, 23], [17, 17]] # even_number = 34
# MATHEMATICSFUNDAMENTALS
# Solution
from gmpy2 import is_prime
def goldbach(even_number):
    l, s = [i for i in range(2, even_number+1) if is_prime(i)], []
    for i in l:
        for j in l:
            if i + j == even_number and i <= j: s.append([i, j])
    return s