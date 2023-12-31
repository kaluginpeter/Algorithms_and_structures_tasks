# Given that
#
# f0 = '0'
# f1 = '01'
# f2 = '010' = f1 + f0
# f3 = '01001' = f2 + f1
# You will be given a number and your task is to return the nth fibonacci string. For example:
#
# solve(2) = '010'
# solve(3) = '01001'
# More examples in test cases. Good luck!
#
# If you like sequence Katas, you will enjoy this Kata: Simple Prime Streaming
#
# ALGORITHMS
# Solution
def solve(n):
    a, b = '0', '01'
    for i in range(n):
        a, b = b, b + a
    return a