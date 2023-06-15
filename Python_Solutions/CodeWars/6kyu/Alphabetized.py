# The alphabetized kata
# Re-order the characters of a string, so that they are concatenated into a
# new string in "case-insensitively-alphabetical-order-of-appearance" order.
# Whitespace and punctuation shall simply be removed!
#
# The input is restricted to contain no numerals and only words containing the english alphabet letters.
#
# Example:
#
# alphabetized("The Holy Bible") # "BbeehHilloTy"
# Inspired by Tauba Auerbach
#
# STRINGSSORTING
# Solution
def alphabetized(s):
    return "".join(sorted(filter(str.isalpha, s),key=str.lower))