# You will be given an array that contains two strings. Your job is to create a function that will take those two strings and transpose them, so that the strings go from top to bottom instead of left to right.
#
# e.g. transposeTwoStrings(['Hello','World']);
#
# should return
#
# H W
# e o
# l r
# l l
# o d
# A few things to note:
#
# There should be one space in between the two characters
# You don't have to modify the case (i.e. no need to change to upper or lower)
# If one string is longer than the other, there should be a space where the character would be
# ARRAYSSTRINGSFUNDAMENTALS
# Solution
import itertools
def transpose_two_strings(arr):
    return '\n'.join(' '.join(i) for i in itertools.zip_longest(arr[0], arr[1], fillvalue=' '))