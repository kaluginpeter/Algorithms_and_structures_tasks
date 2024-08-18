# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
#
# Given an integer n, return the nth ugly number.
#
#
#
# Example 1:
#
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:
#
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
#
#
# Constraints:
#
# 1 <= n <= 1690
# Solution
# Dynamic Programming
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp: list[int] = []
        dp.append(1)
        acc2 = acc3 = acc5 = 0
        next_of_2: int = 2 * 1
        next_of_3: int = 3 * 1
        next_of_5: int = 5 * 1
        next_ugly: int = 1
        for i in range(n - 1):
            next_ugly = min(next_of_2, next_of_3, next_of_5)
            dp.append(next_ugly)
            if next_ugly == next_of_2:
                acc2 += 1
                next_of_2 = dp[acc2] * 2
            if next_ugly == next_of_3:
                acc3 += 1
                next_of_3 = dp[acc3] * 3
            if next_ugly == next_of_5:
                acc5 += 1
                next_of_5 = dp[acc5] * 5
        return next_ugly

# Min Heap (Priority Queue)
# Complexity
# Time complexity: O(NlogN)
# Space complexity: O(N)
# Code
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen: set[int] = set()
        ugly: int = 1
        ugly_heap: list[int] = [ugly]
        seen.add(ugly)
        modules: list[int] = [2, 3, 5]
        for _ in range(n):
            current_ugly = heapq.heappop(ugly_heap)
            for module in modules:
                new_ugly: int = current_ugly * module
                if new_ugly not in seen:
                    heapq.heappush(ugly_heap, new_ugly)
                    seen.add(new_ugly)
        return current_ugly