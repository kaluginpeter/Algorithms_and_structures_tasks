# Task
# Given any positive integer x ≤ 4000, find the smallest positive integer m such that mx consists of all 9's. Return -1 if no such m exists.
#
# Examples:
# 11 -> 9, because 11 * 9 == 99.
#
# 12 -> -1, because 12 is even, so no multiple of it can contain only nines.
#
# 13 -> 76923, because 13 * 76923 == 999999, and no smaller positive integer, when multiplied by 13, generates an integer containing only nines.
#
# NOTE: Although x ≤ 4000, m can be very very LARGE. Where necessary, the way of handling big integers appropriate to the language should be used.
#
# Mathematics
# Solution
def all_nines(x):
    if x % 10 in {2, 4, 5, 6, 8, 0}: return -1
    start: int = 9
    while start % x != 0:
        start = start * 10 + 9
    return start // x