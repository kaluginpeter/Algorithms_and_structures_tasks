# Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:
#
# input:   [numerator, denominator]
# output:  [reduced numerator, reduced denominator]
# example: [45, 120] --> [3, 8]
# All numerators and denominators will be positive integers.
#
# Note: This is an introductory Kata for a series... coming soon!
#
# FUNDAMENTALSRECURSIONALGORITHMS
# Solution
def reduce_fraction(fraction):
    x, y = fraction
    if x >= y:
        if x % y == 0:
            return x // y, 1
        else:
            for i in range(y - 1, 0, -1):
                if x % i == 0 and y % i == 0:
                    return x // i, y // i
    else:
        if y % x == 0:
            return 1, y // x
        for i in range(x - 1, 0, -1):
            if x % i == 0 and y % i == 0:
                return x // i, y // i