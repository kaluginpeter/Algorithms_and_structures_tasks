# This is a more difficult version of this kata - I suggest solving that kata before attempting this one.
#
# Task
# Your task is similar to the kata above, however now you are not limited to only 2 sets of ratios - you will be given an array of ratios as strings, and you must return a combined ratio in its simplest form, as a string. See the example below:
#
# Example:
#
# ratio_combinator(["12:4","3:7","24:30"]) -> '36:12:28:35'
# The given input ratios may not be in their simplest form, and the inputs range from
# [
# 1
# ,
# 1
# 0
# 5
# ]
# [1,10
# 5
#  ] (1 to 1e5 inclusive).
#
# AlgorithmsFundamentals
# Solution
from math import gcd
from functools import reduce

def ratio_combinator(ratios):
    pairs = [tuple(map(int, r.split(":"))) for r in ratios]
    result = [pairs[0][0], pairs[0][1]]
    for left, right in pairs[1:]:
        current = result[-1]
        lcm = current * left // gcd(current, left)
        m1 = lcm // current
        m2 = lcm // left
        result = [x * m1 for x in result]
        result.append(right * m2)
    g = reduce(gcd, result)
    return ":".join(str(x // g) for x in result)