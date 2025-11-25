# This kata is based on Project Euler Problem 164
#
# Objective
# Write a function that takes a number n and returns the number of n digit numbers (without leading zeros) that no three consecutive digits have a sum greater than 9
#
# Examples
# | n  |  number of numbers
# |--------------------------
# | 1  |  9 (0 doesn't count)
# | 2  | 45
# | 3  | 165
# Note:
# n ranges from 1 to 500
# Code length limit = 5000 to avoid hard coded solutions
# MathematicsAlgorithms
# Solution
def number_of_numbers(n):
    if n == 1: return 9
    dp = [[0] * 10 for _ in range(10)]
    for a in range(1, 10):
        for b in range(10):
            if a + b <= 9: dp[a][b] = 1
    for _ in range(3, n + 1):
        new_dp = [[0] * 10 for _ in range(10)]
        for a in range(10):
            for b in range(10):
                if dp[a][b] == 0: continue
                for c in range(10):
                    if a + b + c <= 9: new_dp[b][c] += dp[a][b]
        dp = new_dp
    return sum(sum(row) for row in dp)