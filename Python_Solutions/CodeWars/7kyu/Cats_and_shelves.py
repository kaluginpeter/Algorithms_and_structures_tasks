# Description
# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the shelf directly above its head), according to the illustration:
#
#                  ┌────────┐
#                  │-6------│
#                  └────────┘
# ┌────────┐
# │------5-│
# └────────┘  ┌─────► OK!
#             │    ┌────────┐
#             │    │-4------│
#             │    └────────┘
# ┌────────┐  │
# │------3-│  │
# BANG!────┘  ├─────► OK!
#   ▲  |\_/|  │    ┌────────┐
#   │ ("^-^)  │    │-2------│
#   │ )   (   │    └────────┘
# ┌─┴─┴───┴┬──┘
# │------1-│
# └────────┘
# Input
# Start and finish shelf numbers (always positive integers, finish no smaller than start)
#
# Task
# Find the minimum number of jumps to go from start to finish
#
# Example
# Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)
#
# Inspirers
# *picture with sweet cats
# inspirers
#
# ALGORITHMS
# Solution
def solution(start, finish):
    count = 0
    while finish > start:
        count += 1
        if start + 3 <= finish:
            start += 3
        else:
            start += 1
    return count