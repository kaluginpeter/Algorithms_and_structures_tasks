# Create a function isAlt() that accepts a string as an argument and
# validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.
#
# is_alt("amazon")  # True
# is_alt("apple")   # False
# is_alt("banana")  # True
# Arguments consist of only lowercase letters.
#
# ALGORITHMSSTRINGS
# Solution
import re
def is_alt(word):
    return not re.search('[aeiou]{2}|[^aeiou]{2}', word)