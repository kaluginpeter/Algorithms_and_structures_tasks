# Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return 1. If any argument is 0, return 0.
#
# MATHEMATICSALGORITHMS
# Solution
def lcm(*args):
    if not args:
        return 1
    if 0 in args:
        return 0
    m = max(args)
    lcm = m
    while any(lcm % i != 0 for i in args):
        lcm += m
    return lcm