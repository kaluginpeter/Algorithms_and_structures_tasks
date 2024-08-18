# A happy number is one where if you repeatedly square its digits and add them together, you eventually end up at 1.
#
# For example:
#
# 7 -> 49 -> 97 -> 130 -> 10 -> 1 so 7 is a happy number.
#
# 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 so 42 is not a happy number.
#
# This can also be done with powers other than 2.
#
# Complete the function that receives 2 arguments: the starting number and the exponent.
# It should return an array of numbers containing whatever loop it encounters, or [1] if
# it doesn't encounter any. This array should only include the numbers in the loop, not
# any that lead into the loop, and should repeat the first number as the last number e.g.:
#
# [42, 20, 4, 16, 37, 58, 89, 145, 42]
# The first number in the array should be where the loop is first encountered.
#
# All function inputs will be positive integers, with the exponent being between 2 and 4.
#
# ALGORITHMS
# Solution
def isHappy(n, pow):
    l = []
    while True:
        l.append(n)
        n = sum([i**pow for i in map(int, str(n))])
        if n == 1: return [1]
        if n in l: return l[l.index(n):] + [n]