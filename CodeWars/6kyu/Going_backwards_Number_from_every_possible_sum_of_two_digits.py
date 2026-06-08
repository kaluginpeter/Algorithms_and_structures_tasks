# Every possible sum of two digits
# Given a long number, return all the possible sum of two digits of it.
#
# For example, 12345: all possible sum of two digits from that number are:
#
# [ 1 + 2, 1 + 3, 1 + 4, 1 + 5, 2 + 3, 2 + 4, 2 + 5, 3 + 4, 3 + 5, 4 + 5 ]
# Therefore the result must be:
#
# [ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]
# We now interrupt your regularly scheduled programming
# Given the result, return the number!
#
# ( if there is more than one possibility, just return any one of them )
# Algorithms
# Solution
from math import isqrt

def find_number(sums):
    m = len(sums)
    if m == 0: return 0
    if m == 1:
        s = sums[0]
        a = min(9, s)
        b = s - a
        return int(f"{a}{b}")
    n = (1 + isqrt(1 + 8 * m)) // 2
    d1 = (sums[0] + sums[1] - sums[n - 1]) // 2
    digits = [d1]
    for i in range(n - 1): digits.append(sums[i] - d1)
    return int("".join(map(str, digits)))