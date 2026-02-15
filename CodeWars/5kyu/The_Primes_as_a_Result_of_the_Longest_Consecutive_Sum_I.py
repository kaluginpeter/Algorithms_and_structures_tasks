# This kata is inspired by problem #50 from Project Euler.
#
# The prime
# 41
# 41 is the sum of many consecutive primes:
#
# 41
# =
# 2
# +
# 3
# +
# 5
# +
# 7
# +
# 11
# +
# 13
# 41=2+3+5+7+11+13
#
# Furthermore,
# 41
# 41 is the prime
# p
# ∣
# p
# <
# 100
# p∣p<100 with the longest chain of consecutive prime addends (6 addends).
#
# For primes
# p
# ∣
# p
# <
# 500
# p∣p<500, the prime with the largest chain of consecutive prime addends is
# 499
# 499 with 17 addends.
#
# 499
# =
# 3
# +
# 5
# +
# 7
# +
# 11
# +
# 13
# +
# 17
# +
# 19
# +
# 23
# +
# 29
# +
# 31
# +
# 37
# +
# 41
# +
# 43
# +
# 47
# +
# 53
# +
# 59
# +
# 61
# 499=3+5+7+11+13+17+19+23+29+31+37+41+43+47+53+59+61
#
# Write a function that takes an integer
# n
# n as an argument and returns a sorted list of prime numbers
# p
# ∣
# p
# <
# n
# p∣p<n that have the longest chain of consecutive prime addends.
#
# Let's see some cases (Input -> Output):
#
# * 100 -> [41]
# * 500 -> [499]
# * 499 -> [379, 491]
# Random tests use values of
# n
# n in the range
# 100
# ≤
# n
# ≤
# 500000
# 100≤n≤500000
#
# Enjoy it!
#
# PerformanceAlgorithmsMathematicsData StructuresArraysFundamentals
# Solution
def prime_maxlength_chain(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i): sieve[j] = False
    primes = [i for i in range(2, n) if sieve[i]]
    prefix = [0]
    for p in primes: prefix.append(prefix[-1] + p)
    max_len = 0
    result = []
    total_primes = len(primes)
    for length in range(total_primes, 0, -1):
        found = []
        for i in range(total_primes - length + 1):
            s = prefix[i + length] - prefix[i]
            if s >= n: break
            if sieve[s]: found.append(s)
        if found: return sorted(found)
    return []