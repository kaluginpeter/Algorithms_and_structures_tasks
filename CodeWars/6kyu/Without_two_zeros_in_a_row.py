# You are given a positive integer n.
#
# The task is to calculate how many binary numbers without leading zeros (such that their length is n and they do not contain two zeros in a row) there are. Note that zero itself ("0") meets the conditions (for n = 1).
#
# For example, there are three eligible binary numbers of length 3:
#
# 101
# 110
# 111
# 100 is not suitable.
#
# Remember that n may be fairly big (up to 10^4). Good luck!
#
# Dynamic Programming
# Solution
def zeros(n: int) -> int:
    if n == 1: return 2
    dp: list[int] = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = dp[i - 1] + (dp[i - 2] if i >= 2 else 1)
    return dp[n - 1]