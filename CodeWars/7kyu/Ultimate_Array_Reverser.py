# Task
# Given an array of strings, reverse them and their order in such way that their length stays the same as the length of the original inputs.
#
# Example:
# Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
# Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}
# Good luck!
#
# FUNDAMENTALSALGORITHMS
# Solution
def reverse(a):
    l = reversed(''.join(a))
    return [''.join(next(l) for k in i) for i in a]