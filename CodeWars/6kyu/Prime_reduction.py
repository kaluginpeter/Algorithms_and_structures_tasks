# Consider the prime number 23. If we sum the square of its digits we get: 2^2 + 3^2 = 13,
# then for 13: 1^2 + 3^2 = 10, and finally for 10: 1^2 + 0^2 = 1.
#
# Similarly, if we start with prime number 7, the sequence is: 7->49->97->130->10->1.
#
# Given a range, how many primes within that range will eventually end up being 1?
#
# The upperbound for the range is 50,000. A range of (2,25) means that: 2 <= n < 25.
#
# Good luck!
#
# If you like this Kata, please try:
#
# Prime reversion
#
# Domainant primes
#
# ALGORITHMS
# Solution
from gmpy2 import is_prime
def check(n):
    l = []
    while n not in l:
        l += [n]
        n = sum(int(i)**2 for i in str(n))
        if n==1: return True
    return False
def solve(a,b):
    return len([i for i in range(a,b) if is_prime(i) and check(i)])