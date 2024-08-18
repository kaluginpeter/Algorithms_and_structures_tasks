# You need to count the number of prime numbers less than or equal to some natural n.
#
# For example:
# count_primes_less_than(34) = 11
# count_primes_less_than(69) = 19
# count_primes_less_than(420) = 81
# count_primes_less_than(666) = 121
# In this kata all the tests will be with 1 ⩽ � ⩽ 1 0 10 1⩽n⩽10 10
# Code length limited to 3000 characters to avoid hardcoding.
# Good luck!
# Solution
import numpy as np
from bisect import bisect
def prime_sieve(n):
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[k*k//3::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
phi_cache, pi_cache = {}, {}
l = 10**8
primes = prime_sieve(l)
def phi(x, a):
    if (x, a) in phi_cache: return phi_cache[(x,a)]
    p = primes[a - 1]
    if p * p >= x and x < primes[-1]: return bisect(primes, x) - a + 1
    if a == 1: return (x + 1) // 2
    r = phi(x, a-1) - phi(x // primes[a-1], a-1)
    phi_cache[(x, a)] = r
    return r
def pi(x):
    if x in pi_cache: return pi_cache[x]
    if x < l:
        r = bisect(primes, x)
        pi_cache[x] = r
        return r
    a = pi(int(x ** (1./4) + 1e-6))
    b = pi(int(x ** (1./2) + 1e-6))
    c = pi(int(x ** (1./3) + 1e-6))
    r = phi(x,a) + (b+a-2) * (b-a+1) // 2
    for i in range(a+1, b+1):
        w = x // primes[i-1]
        b_i = pi(int(w ** (1./2) + 1e-6))
        r = r - pi(w)
        if i <= c:
            for j in range(i, b_i+1):
                r = r - pi(w // primes[j-1]) + j - 1
    pi_cache[x] = r
    return r
def count_primes_less_than(n):
    if n < 3: return 0
    if n < l:
        return np.searchsorted(primes, n + 1)
    return pi(n)