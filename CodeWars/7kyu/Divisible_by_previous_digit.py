# Take a number and check each digit if it is divisible by the digit on its left checked and return an array of booleans.
#
# The booleans should always start with false becase there is no digit before the first one.
#
# Examples
# 73312        => [false, false, true, false, true]
# 2026         => [false, true, false, true]
# 635          => [false, false, false]
# *** Remember 0 is evenly divisible by all integers but not the other way around ***
#
# ALGORITHMS
# Solution
def divisible_by_last(n):
    l = list(map(int, f"0{n}"))
    return [i and not j%i for i,j in zip(l, l[1:])]