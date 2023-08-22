# In this Kata, you will be given an integer n and your task will be to return the largest integer that is <= n and has the highest digit sum.
#
# For example:
#
# solve(100) = 99. Digit Sum for 99 = 9 + 9 = 18. No other number <= 100 has a higher digit sum.
# solve(10) = 9
# solve(48) = 48. Note that 39 is also an option, but 48 is larger.
# Input range is 0 < n < 1e11
#
# More examples in the test cases.
#
# Good luck!
#
# ALGORITHMS
# Solution
def solve(n):
    x = str(n)
    c = [x] + [str(int(x[:i]) - 1) + '9' * (len(x) - i) for i in range(1, len(x))]
    return int(max(c, key=lambda x: (sum(map(int, x)), int(x))))