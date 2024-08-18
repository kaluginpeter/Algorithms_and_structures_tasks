# Given a varying number of integer arguments, return the digits that are not present in any of them.
#
# Example:
#
# [12, 34, 56, 78]  =>  "09"
# [2015, 8, 26]     =>  "3479"
# Note: the digits in the resulting string should be sorted.
#
# FUNDAMENTALSFILTERINGARRAYS
# Solution
def unused_digits(*numbers):
    w = ''.join(str(i) for i in numbers)
    return ''.join(i for i in '0123456789' if i not in w)