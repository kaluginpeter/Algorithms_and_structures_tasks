# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
#
# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
#
#
#
# Example 1:
#
# Input: n = 7
# Output: 21
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
# Example 2:
#
# Input: n = 10
# Output: 40
# Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
# Example 3:
#
# Input: n = 9
# Output: 30
# Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.
#
#
# Constraints:
#
# 1 <= n <= 103
# Solution
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        count = 0
        for i in range(3, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                count += i
        return count
# Runtime 102ms Beats 45.93% - Memory 16.2 MB Beats 63.46%
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        a, b, c, d, e, f, g = n // 3, n // 5, n // 7, n // 15, n // 21, n // 35, n // 105

        return (
                3 * a * (a + 1)  #
                + 5 * b * (b + 1)  # <-- three venn circles
                + 7 * c * (c + 1)  #

                - 15 * d * (d + 1)  #
                - 21 * e * (e + 1)  # <-- three venn lunes
                - 35 * f * (f + 1)  #

                + 105 * g * (g + 1)  # <-- one venn circular triangle
        ) // 2
# Runtime 43ms Beats 99.39% - Memory 16.3 MB Beats 63.46%