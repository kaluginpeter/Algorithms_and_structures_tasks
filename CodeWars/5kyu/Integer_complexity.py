# Integer complexity is the smallest number of 1s you need to make a certain positive number, using only addition and multiplication. Because we typically use infix notation for math expressions, grouping with parenthesis is also allowed.
#
# Your goal is for a given positive integer to compute its integer complexity.
#
# Your program will be tested against inputs up to 200 000. Even relatively fast solutions may time out occasionally. If your solution times out and it's close to finishing, try again.
#
# Examples:
#
# 1 -> 1    1
# 2 -> 2    1 + 1
# 3 -> 3    1 + 1 + 1
# 6 -> 5    (1 + 1 + 1) * (1 + 1)
# 8 -> 6    (1 + 1) * (1 + 1) * (1 + 1)
# MathematicsNumber TheoryPerformance
# Solution
dp: list[int] = [0, 1]
dp[1] = 1
def integer_complexity(n):
    if n < len(dp): return dp[n]
    for k in range(len(dp), n + 1):
        dp.append(dp[k - 1] + 1)
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                j = k // i
                complexity_via_factors = dp[i] + dp[j]
                dp[k] = min(dp[k], complexity_via_factors)
    return dp[n]