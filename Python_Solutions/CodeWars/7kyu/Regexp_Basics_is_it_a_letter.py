# Complete the code which should return true if the given object is a single ASCII letter (lower or upper case), false otherwise.
#
# REGULAR EXPRESSIONSFUNDAMENTALS
# Solution
def is_letter(s):
    return s.isalpha() and len(s) == 1