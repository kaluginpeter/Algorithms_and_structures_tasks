# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.
#
# FUNDAMENTALS
# Solution
def find_short(s):
    # your code here
    return len(list(i for i in sorted(s.split(), key=len))[0])