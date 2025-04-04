# You have a grid with
# m
# m rows and
# n
# n columns. Return the number of unique ways that start from the top-left corner and go to the bottom-right corner. You are only allowed to move right and down.
#
# For example, in the below grid of
# 2
# 2 rows and
# 3
# 3 columns, there are
# 10
# 10 unique paths:
#
# o----o----o----o
# |    |    |    |
# o----o----o----o
# |    |    |    |
# o----o----o----o
# Note: there are random tests for grids up to 1000 x 1000 in most languages, so a naive solution will not work.
#
# Hint: use mathematical permutation and combination
#
# FundamentalsMathematics
# Solution
dp: list[list[int]] = [[0] * (1001) for _ in range(1001)]
dp[0][0] = 1
for r in range(1001):
    for c in range(1001):
        if r: dp[r][c] += dp[r - 1][c]
        if c: dp[r][c] += dp[r][c - 1]
def number_of_routes(m, n):
    return dp[n][m]