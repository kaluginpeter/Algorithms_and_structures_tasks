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


# Python O(N^2)* O(201*201) DynamicProgramming Math
from math import ceil

dp: list[list[float]] = [[-1] * 201 for _ in range(201)]


class Solution:
    def dfs(self, a: int, b: int) -> float:
        if a <= 0 and b <= 0:
            return 0.5
        elif a <= 0 and b > 0:
            return 1
        elif a > 0 and b <= 0:
            return 0
        if dp[a][b] != -1: return dp[a][b]
        dp[a][b] = 0.25 * (
                    self.dfs(a - 4, b) + self.dfs(a - 3, b - 1) + self.dfs(a - 2, b - 2) + self.dfs(a - 1, b - 3))
        return dp[a][b]

    def soupServings(self, n: int) -> float:
        if n > 4450: return 1
        bound: int = ceil(n / 25)
        return self.dfs(bound, bound)

# C++ O(N^2)* O(201*201) DynamicProgramming Math
class Solution {
    double dp[201][201];
public:
    double dfs(int a, int b) {
        if (a <= 0 && b <= 0) return 0.5;
        else if (a > 0 && b <= 0) return 0;
        else if (a <= 0 && b > 0) return 1;
        else if (dp[a][b] != -1) return dp[a][b];
        dp[a][b] = 0.25 * (dfs(a - 4, b) + (dfs(a - 3, b - 1) + dfs(a - 2, b - 2) + dfs(a - 1, b - 3)));
        return dp[a][b];
    }

    double soupServings(int n) {
        if (n >= 4450) return 1;
        std::fill(&dp[0][0], &dp[0][0] + 201 * 201, -1);
        int bound = std::ceil(static_cast<double>(n) / 25);
        return dfs(bound, bound);
    }
};