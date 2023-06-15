# You are given an array. Complete the function that returns the number
# of ALL elements within an array, including any nested arrays.
#
# Examples
# []                   -->  0
# [1, 2, 3]            -->  3
# ["x", "y", ["z"]]    -->  4
# [1, 2, [3, 4, [5]]]  -->  7
# The input will always be an array.
#
# ARRAYSRECURSIONFUNDAMENTALS
# Solution
from functools import reduce
def deep_count(a):
    if not isinstance(a, list):
        return 0
    if len(a) == 0:
        return 0
    return len(a) + reduce(lambda x,y : x + deep_count(y), a, 0)