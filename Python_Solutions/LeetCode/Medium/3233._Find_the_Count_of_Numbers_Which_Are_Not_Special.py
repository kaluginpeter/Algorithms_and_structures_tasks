# You are given 2 positive integers l and r. For any number x, all positive divisors of x except x are called the proper divisors of x.
#
# A number is called special if it has exactly 2 proper divisors. For example:
#
# The number 4 is special because it has proper divisors 1 and 2.
# The number 6 is not special because it has proper divisors 1, 2, and 3.
# Return the count of numbers in the range [l, r] that are not special.
#
#
#
# Example 1:
#
# Input: l = 5, r = 7
#
# Output: 3
#
# Explanation:
#
# There are no special numbers in the range [5, 7].
#
# Example 2:
#
# Input: l = 4, r = 16
#
# Output: 11
#
# Explanation:
#
# The special numbers in the range [4, 16] are 4 and 9.
#
#
#
# Constraints:
#
# 1 <= l <= r <= 109
# Solution Math O(sqrtN log log sqrtN) O(sqrtN)
import math
class Solution:
    def sieve_of_eratosthenes(self, limit: int) -> list[int]:
        is_prime: list[bool] = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[start]:
                for multiple in range(start*start, limit + 1, start):
                    is_prime[multiple] = False
        return [num for num, prime in enumerate(is_prime) if prime]

    def nonSpecialCount(self, l: int, r: int) -> int:
        upper_limit: int = int(math.sqrt(r)) + 1
        primes: list[int] = self.sieve_of_eratosthenes(upper_limit)
        semi_primes: int = 0
        for i in range(len(primes)):
            semi_prime = primes[i]**2
            if l <= semi_prime <= r:
                semi_primes += 1
            if semi_prime > r: break
        return (r - l + 1) - semi_primes