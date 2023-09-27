# Covfefe
# Your are given a string. You must replace any occurence of the sequence coverage by covfefe, however, if you don't find the word coverage in the string, you must add covfefe at the end of the string with a leading space.
#
# For the languages where the string is mutable (such as ruby), don't modify the given string, otherwise this will break the test cases.
#
# STRINGS
# Solution
def covfefe(s):
    if 'coverage' in s: return s.replace('coverage', 'covfefe')
    return s + ' covfefe'