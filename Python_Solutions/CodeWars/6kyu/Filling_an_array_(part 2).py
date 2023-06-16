# Following on from Part 1, part 2 looks at some more complicated array contents.
#
# So let's try filling an array with...
#
# ...square numbers
# The numbers from 1 to n*n
#
# const squares = n => ???
# squares(5) // [1, 4, 9, 16, 25]
# ...a range of numbers
# A range of numbers starting from start and increasing by step
#
# const range = (n, start, step) => ???
# range(6, 3, 2) // [3, 5, 7, 9, 11, 13]
# ...random numbers
# A bunch of random integers between min and max
#
# const random = (n, min, max) => ???
# random(4, 5, 10) // [5, 9, 10, 7]
# ...prime numbers
# All primes starting from 2 (obviously)...
#
# const primes = n => ???
# primes(6) // [2, 3, 5, 7, 11, 13]
# HOTE: All the above functions should take as their first
# parameter a number that determines the length of the returned array.
#
# ARRAYSALGORITHMSFUNDAMENTALS
# Solution
def squares(n):
    return [i**2 for i in range(1, n+1)]
def num_range(n, start, step):
    l = []
    for i in range(n):
        l.append(start)
        start += step
    return l
def rand_range(n, mn, mx):
    from random import randint
    l = []
    for i in range(n):
        l.append(randint(mn, mx))
    return l
def primes(n):
    from gmpy2 import is_prime
    l = []
    c = 1
    while len(l) < n:
        if is_prime(c): l.append(c)
        c += 1
    return l