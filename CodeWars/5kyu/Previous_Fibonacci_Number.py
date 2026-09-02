# Your mission, should you choose to accept it, is to determine the predecessor of a given Fibonacci number n in the Fibonacci sequence.

# The Fibonacci sequence is defined by the following properties:

# fib(0) == 0
# fib(1) == 1
# fib(n) == fib(n - 1) + fib(n - 2)
# The first numbers in the Fibonacci sequence are:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# As you can see, we don't handle negative numbers, so 0 has no predecessor. Furthermore, the number 1 has 2 possible predecessors, namely 0 and 1.

# If there are multiple possible predecessors, take the smaller one. If there is no predecessor, return None.

# You should expect the following random tests:

# 4 test cases with n <= fib(2**18)
# 4 test cases with n <= fib(2**22)
# 4 test cases with n <= fib(2**26)
# This means that you should be prepared to handle numbers with up to 46_589_786 bits.

# MathematicsNumber Theory
# Solution
import math

import gmpy2
_mpz = gmpy2.mpz

_LOG2_PHI = math.log2((1 + 5 ** 0.5) / 2)
_LOG2_SQRT5 = 0.5 * math.log2(5)


def _fib_pair(k: int):
    a, b = _mpz(0), _mpz(1) 
    for bit in bin(k)[2:]:
        c = a * (2 * b - a)  
        d = a * a + b * b      
        if bit == '1': a, b = d, c + d
        else: a, b = c, d
    return a, b


def _estimate_k(n: int) -> int:
    bl = n.bit_length()
    shift = max(0, bl - 64)
    top = int(n >> shift)
    log2n = math.log2(top) + shift
    return round((log2n + _LOG2_SQRT5) / _LOG2_PHI)


def previous_fib(n: int) -> int | None:
    if n == 0: return None
    if n == 1: return 0  
    k = max(_estimate_k(n), 2)
    a, b = _fib_pair(k) 
    n = _mpz(n)
    while a != n:
        if a > n: a, b = b - a, a    
        else: a, b = b, a + b   
    return int(b - a)