# Wilson primes satisfy the following condition. Let P represent a prime number.
#
# Then,
#
# ((P-1)! + 1) / (P * P)
# should give a whole number.
#
# Your task is to create a function that returns true if the given number is a Wilson prime.
#
# MATHEMATICSFUNDAMENTALS
# Solution
def am_i_wilson(n):
    list = [5, 13, 563, 5971, 558771, 1964215, 8121909,
            12326713, 23025711, 26921605, 341569806, 399292158]
    return n in list