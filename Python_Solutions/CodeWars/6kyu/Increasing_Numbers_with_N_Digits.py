# An non decreasing number is one containing no two consecutive digits (left to right), whose the first is higer than the second. For example, 1235 is an non decreasing number, 1229 is too, but 123429 isn't.
#
# Write a function that finds the number of non decreasing numbers up to 10**N (exclusive) where N is the input of your function. For example, if N=3, you have to count all non decreasing numbers from 0 to 999.
#
# You'll definitely need something smarter than brute force for large values of N!
#
# MATHEMATICSFUNDAMENTALS
# Solution
def increasing_numbers(digits):
    if digits == 0:
        return 1
    dp = [[0] * 10 for _ in range(digits + 1)]
    for j in range(10):
        dp[1][j] = 1

    for i in range(2, digits + 1):
        for j in range(10):
            for k in range(j + 1):
                dp[i][j] += dp[i - 1][k]
    total_count = sum(dp[digits][j] for j in range(1, 10))
    return total_count + 1