# Compare two strings by comparing the sum of their values (ASCII character code).
#
# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.
#
# Examples:
# "AD", "BC"  -> equal
# "AD", "DD"  -> not equal
# "gf", "FG"  -> equal
# "zz1", ""   -> equal (both are considered empty)
# "ZzZz", "ffPFF" -> equal
# "kl", "lz"  -> not equal
# null, ""    -> equal
# MATHEMATICSSTRINGSFUNDAMENTALS
# Solution
def compare(s1,s2):
    if not s1 and not s2:
        return True
    if any(x for x in s1 if not x.isalpha()):
        s1 = ''
    if any(x for x in s2 if not x.isalpha()):
        s2 = ''
    return sum(ord(x.upper()) for x in s1) == sum(ord(x.upper()) for x in s2)