# B. T-primes
# time limit per test2 seconds
# memory limit per test256 megabytes
# We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer t Т-prime, if t has exactly three distinct positive divisors.
#
# You are given an array of n positive integers. For each of them determine whether it is Т-prime or not.
#
# Input
# The first line contains a single positive integer, n (1 ≤ n ≤ 105), showing how many numbers are in the array. The next line contains n space-separated integers xi (1 ≤ xi ≤ 1012).
#
# Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.
#
# Output
# Print n lines: the i-th line should contain "YES" (without the quotes), if number xi is Т-prime, and "NO" (without the quotes), if it isn't.
#
# Examples
# inputCopy
# 3
# 4 5 6
# outputCopy
# YES
# NO
# NO
# Note
# The given test has three numbers. The first number 4 has exactly three divisors — 1, 2 and 4, thus the answer for this number is "YES". The second number 5 has two divisors (1 and 5), and the third number 6 has four divisors (1, 2, 3, 6), hence the answer for them is "NO".
# Solution Math O(N) O(k) where k is length of primes
import math
import sys


def sieve_of_eratosthenes(limit: int) -> list:
    is_prime: list[bool] = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]


def solution(n: int, nums: list) -> str:
    upper_boundary: int = int(math.sqrt(max(nums))) + 1
    primes: set = set(sieve_of_eratosthenes(upper_boundary))
    for num in nums:
        root: int = math.sqrt(num)
        if root != int(root):
            print('NO')
        else:
            print(['NO', 'YES'][int(root) in primes])


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, nums)
