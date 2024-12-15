# My 6th kata, implement a lexicographic sort order to make longer items go before any of their prefixes.
#
# In Python, write a function (custom_sort) that takes an input list (lst) of strings. The function should return a new list of strings sorted lexiographically but with longer items before their prefixes. The test cases give some examples.
#
# You can assume that all strings will consist of ASCII printable characters and that the largest character will be '~', which is chr(126). For an extra challenge code a solution that makes no such assumptions.
#
# Do vote and provide any feedback on the kata.
#
# If you like this kata, do checkout my other katas.
#
# AlgorithmsArraysSortingData Structures
# Solution
from functools import cmp_to_key

def comparator(x: str, y: str) -> int:
    if x.startswith(y):
        return -1
    elif y.startswith(x):
        return 1
    return (x > y) - (x < y)

def custom_sort(lst):
    return sorted(lst, key=cmp_to_key(comparator))