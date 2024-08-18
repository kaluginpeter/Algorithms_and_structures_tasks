# Related to MrZizoScream's Product Array kata. You might want to solve that one first :)
#
# This is an adaptation of a problem I came across on LeetCode.
#
# Given an array of numbers, your task is to return a new array where each
# index (new_array[i]) is equal to the product of the original array, except for the number at that index (array[i]).
#
# Two things to keep in mind:
#
# Zeroes will be making their way into some of the arrays you are given
# O(n^2) solutions will not pass.
# Examples:
#
# product_sans_n([1,2,3,4]) => [24, 12, 8, 6]
# product_sans_n([2,3,4,5]) => [60, 40, 30, 24]
# product_sans_n([1,1,1]) => [1, 1, 1]
# product_sans_n([9,0,-2]) => [0, -18, 0])
# product_sans_n([0,-99,0]) => [0, 0, 0])
# product_sans_n([3,14,9,11,11]) => [15246, 3267, 5082, 4158, 4158])
# product_sans_n([-8,1,5,13,-1]) => [-65, 520, 104, 40, -520])
# product_sans_n([4,7,3,6,2,14,7,5]) => [123480, 70560, 164640, 82320, 246960, 35280, 70560, 98784]
# Note: All inputs will be valid arrays of nonzero length.
#
# Have fun! Please upvote if you enjoyed :)
#
# ARRAYSFUNDAMENTALS
# Solution
from functools import reduce
la = lambda x: reduce(lambda a, b:a*b, x)
def product_sans_n(N):
    l, z = len(N), N.count(0)
    if z > 1: return l*[0]
    if z == 1: i = N.index(0); return [0]*(i)+[la(N[:i])*la(N[i+1:])]+[0]*(l-i-1)
    p = la(N);               return [p//i for i in N]