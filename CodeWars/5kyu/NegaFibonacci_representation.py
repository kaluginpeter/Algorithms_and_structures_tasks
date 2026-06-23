# Zeckendorf's Theorem[wiki] states that every positive integer can be represented uniquely as the sum of one or more distinct Fibonacci numbers in such a way that the sum does not include any two consecutive Fibonacci numbers. This representation can be used for Fibonacci Coding[wiki] of positive integers.
#
# The representation and encoding can be extended to use NegaFibonacci numbers[wiki], which would allow us to encode negative numbers as well as positive numbers. 0 Can be represented, but not encoded; this kata will therefore use the representation and not the encoding for its expected value.
#
# Task
# Define a function that accepts an integer and returns its representation as an array of zero (!) or more non-consecutive NegaFibonacci integers, sorted descending by absolute value.
#
# Examples
# negative_fibonacci_representation(0) => []
# negative_fibonacci_representation(1) => [1]
# negative_fibonacci_representation(4) => [5,-1]
# negative_fibonacci_representation(-17) => [-21,5,-1]
# negative_fibonacci_representation(64) => [89,-21,-3,-1]
# Notes
# The formula that generates the Fibonacci numbers in one direction also generates the NegaFibonacci numbers in the other direction. The first 12 terms are given in the Example tests, but you'll need more.
# This is not intended to be a performance kata, but there will be ~3000 tests over the full range of Int ( Python: abs(n) <= 2^64 ). Your naive Fibonacci implementation will bomb. :]
# I take no responsibility for the content of external resources.
# Number TheoryPuzzlesAlgorithms
# Solution
from typing import List
from functools import lru_cache

def negative_fibonacci_representation(n: int) -> List[int]:
    if n == 0: return []
    fib = [0, 1, 1]
    limit = 1 << 65
    while fib[-1] < limit: fib.append(fib[-1] + fib[-2])
    negfib = [0]
    for i in range(1, len(fib)): negfib.append(fib[i] if i & 1 else -fib[i])

    @lru_cache(None)
    def bounds(i: int, blocked: bool):
        if i == 0: return (0, 0)
        if blocked: return bounds(i - 1, False)
        mn0, mx0 = bounds(i - 1, False)
        mn1, mx1 = bounds(i - 1, True)
        v = negfib[i]
        return (min(mn0, mn1 + v), max(mx0, mx1 + v))
    m = len(negfib) - 1
    while m > 0:
        mn, mx = bounds(m, False)
        if mn <= n <= mx: break
        m -= 1
    target = n
    result = []
    blocked = False
    for i in range(m, 0, -1):
        if blocked:
            blocked = False
            continue
        mn, mx = bounds(i - 1, True)
        if mn <= target - negfib[i] <= mx:
            result.append(negfib[i])
            target -= negfib[i]
            blocked = True
    return result