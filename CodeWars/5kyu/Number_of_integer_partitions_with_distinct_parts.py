# This Kata is based on Number of integer partitions.
#
# An integer partition with distinct parts of n is a decreasing list of positive integers which sum to n, in which no number occurs more than once.
#
# For example, there are 3 integer partitions of 5:
#
# [5], [4,1], [3,2].
# Write a function which returns the number of integer partition with distinct parts of n (1 <= n <= 600).
#
# MathematicsAlgorithmsDiscrete Mathematics
# Solution
def partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for x in range(1, n + 1):
        for s in range(n, x - 1, -1):
            dp[s] += dp[s - x]
    return dp[n]