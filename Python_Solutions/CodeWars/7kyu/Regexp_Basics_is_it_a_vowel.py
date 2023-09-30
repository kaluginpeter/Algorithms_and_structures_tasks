# Implement the function which should return true if given object is a vowel (meaning a, e, i, o, u, uppercase or lowercase), and false otherwise.
#
# REGULAR EXPRESSIONSFUNDAMENTALS
# Solution
def is_vowel(s):
    return s.lower() in ['a', 'e', 'i', 'o', 'u']