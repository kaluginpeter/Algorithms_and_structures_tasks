# Consider a sequence made up of the consecutive prime numbers. This infinite sequence would start with:
#
# "2357111317192329313741434753596167717379..."
# You will be given two numbers: a and b, and your task will be to return b elements starting from index a in this sequence.
#
# For example:
# solve(10,5) == `19232` Because these are 5 elements from index 10 in the sequence.
# Tests go up to about index 20000.
#
# More examples in test cases. Good luck!
#
# Please also try Simple time difference
#
# ALGORITHMS
# Solution
from gmpy2 import is_prime
def solve(a, b):
    l, top = [], 2
    while len(l) != b + a:
        if is_prime(top):
            l.append(str(top))
        top += 1
    l = ''.join(l)
    return l[a:a+b]