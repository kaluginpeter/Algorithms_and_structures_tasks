# Complete the function which accepts a string and return an
# array of character(s) that have the most spaces to their right and left.
#
# Notes:
#
# the string can have leading/trailing spaces - you should not count them
# the strings contain only unique characters from a to z
# the order of characters in the returned array doesn't matter
# Examples
# "a b  c"                        -->  ["b"]
# "a bcs           d k"           -->  ["d"]
# "    a b  sc     p     t   k"   -->  ["p"]
# "a  b  c  de"                   -->  ["b", "c"]
# "     a  b  c de        "       -->  ["b"]
# "abc"                           -->  ["a", "b", "c"]
# Good luck!
#
# STRINGSALGORITHMS
# Solution
import re
def loneliest(strng):
    l = [re.match(r'\s*\w\s*', strng.strip()[i:]) for i in range(len(strng))]
    le = max(len(i.group(0)) for i in l if i)
    return [i.group(0).strip() for i in l if i and len(i.group(0)) == le]
