# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:
#
# Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: 3
# Explanation: Initially, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Example 2:
#
# Input: n = 1
# Output: 0
#
#
# Constraints:
#
# 1 <= n <= 1000
# Solution Math Dynamic Programming O(N log log N) O(N)
class Solution:
    def get_primes(self, n: int) -> list[int]:
        m: int = n + 1
        numbers: list[bool] = [True] * m
        for i in range(2, int(n ** 0.5 + 1)):
            if numbers[i]:
                for j in range(i * i, m, i):
                    numbers[j] = False

        primes: list[int] = []
        for i in range(2, m):
            if numbers[i]:
                primes.append(i)
        return primes

    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        primes: list[int] = self.get_primes(n)
        if n in primes: return n
        total: int = 0
        while n:
            for prime in primes:
                if n % prime == 0:
                    n //= prime
                    total += prime
                if n == 1: return total
        return total