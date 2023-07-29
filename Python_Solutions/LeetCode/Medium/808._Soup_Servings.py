# There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:
#
# Serve 100 ml of soup A and 0 ml of soup B,
# Serve 75 ml of soup A and 25 ml of soup B,
# Serve 50 ml of soup A and 50 ml of soup B, and
# Serve 25 ml of soup A and 75 ml of soup B.
# When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.
#
# Note that we do not have an operation where all 100 ml's of soup B are used first.
#
# Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
# Input: n = 50
# Output: 0.62500
# Explanation: If we choose the first two operations, A will become empty first.
# For the third operation, A and B will become empty at the same time.
# For the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
# Example 2:
#
# Input: n = 100
# Output: 0.71875
#
#
# Constraints:
#
# 0 <= n <= 109
# Solution
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        n = (n + 24) // 25
        d = {}
        def dyn_prog(x, y):
            if (x, y) in d:
                return d[(x,y)]
            if x <= 0 and y <= 0:
                return 0.5
            if x <= 0:
                return 1
            if y <= 0:
                return 0
            d[(x, y)] = 0.25 * (dyn_prog(x-4, y) + dyn_prog(x-3, y-1) + dyn_prog(x-2, y-2) + dyn_prog(x-1, y-3))
            return d[(x,y)]
        return dyn_prog(n, n)