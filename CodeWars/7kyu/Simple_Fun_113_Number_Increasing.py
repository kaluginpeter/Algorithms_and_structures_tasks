# Task
# Initially a number 1 is written on a board. It is possible to do the following operations with it:
#
# multiply the number by 3
# increase the number by 5
# Your task is to determine if, using these two operations step by step, is it possible to obtain number n?
#
# Example
# For n = 1, the result should be true.
#
# 1 = 1
#
# For n = 2, the result should be false.
#
# For n = 3, the result should be true.
#
# 1 x 3 = 3
#
# For n = 4, the result should be false.
#
# For n = 5, the result should be false.
#
# For n = 6, the result should be true.
#
# 1 + 5 = 6
#
# For n = 18, the result should be true.
#
# 1 + 5 = 6  -->  6 x 3 = 18
#
# For n = 32, the result should be true.
#
# 1 x 3 x 3 x 3 = 27  -->  27 + 5 = 32
#
# For n = 100, the result should be false.
#
# For n = 101, the result should be true.
#
# 1 + 5 + 5 + 5 ... +5 = 101
#
# Input / Output
# [input] integer n
# positive integer, 1 ≤ n ≤ 100_000
#
# [output] a boolean value
# true if n can be obtained using given operations, false otherwise.
#
# Puzzles
# Solution
def number_increasing(n: int) -> bool:
    dp: list[bool] = [False] * (n + 1)
    dp[1] = True
    for i in range(1, n + 1):
        if not dp[i]: continue
        if i * 3 <= n: dp[i * 3] = True
        if i + 5 <= n: dp[i + 5] = True
    return dp[n]