# Union of closed disjoint intervals
# Write a function interval_insert which takes as input
#
# a list myl of disjoint closed intervals with integer endpoints, sorted by increasing order of left endpoints
# an interval interval
# and returns the union of interval with the intervals in myl, as an array of disjoint closed intervals.
#
# Terminology
# A closed interval includes its endpoints. For example [0,5] means greater than or equal to 0 and less than or equal to 5. For more, refer to Wikipedia.
#
# Two intervals are said to be disjoint if they have no element in common. Equivalently, disjoint intervals are intervals whose intersection is the empty interval. For example,
# [1,3] and [4,6] are disjoint
# [1,3] and [3,5] are not.
#
# Examples:
#                          [(1, 2)], (3, 4) -> [(1, 2), (3, 4)]
#                          [(3, 4)], (1, 2) -> [(1, 2), (3, 4)]
#                  [(1, 2), (4, 6)], (1, 4) -> [(1, 6)]
# [(0, 2), (3, 6), (7, 7), (9, 12)], (1, 8) -> [(0, 8), (9, 12)]
# MathematicsFundamentals
# Solution
import bisect
def interval_insert (myl, interval):
    bisect.insort(myl, interval)
    output: list[tuple[int, int]] = []
    prev_end: int = 0
    prev_start: int = 0
    for i in range(len(myl)):
        if not i:
            prev_start, prev_end = myl[i]
        elif myl[i][0] > prev_end:
            output.append((prev_start, prev_end))
            prev_start, prev_end = myl[i]
        else:
            prev_end = max(prev_end, myl[i][1])
    output.append((prev_start, prev_end))
    return output