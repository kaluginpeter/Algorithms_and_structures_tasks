# Update the solution method to round the argument value to the closest precision of two. The argument will always be a float.
#
# 23.23456 --> 23.23
# 1.546    --> 1.55
# FUNDAMENTALS
# Solution
def solution(n):
    return round(n, 2)