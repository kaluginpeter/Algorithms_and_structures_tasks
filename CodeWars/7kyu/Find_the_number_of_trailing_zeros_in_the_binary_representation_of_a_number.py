# Given a number n, find the number of trailing zeros in its binary representation.
#
# Examples:
# 4 should return 2 as it's represented as 100 and 5 should return 0  101
# Limits:
# 0 < n and n <= 10^4
# LOGICBITS
# Solution
def trailing_zeros(n) ->int:
    target: str = bin(n)[2:]
    n: int = len(target) - 1
    while n >= 0 and target[n] == '0':
        n -= 1
    return len(target) - n - 1