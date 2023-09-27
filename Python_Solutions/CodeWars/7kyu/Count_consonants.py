# Complete the function that takes a string of English-language text and returns the number of consonants in the string.
#
# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.
#
# STRINGSFUNDAMENTALS
# Solution
def consonant_count(s):
    return sum([1 if i not in 'aeiou' and i.isalpha() else 0 for i in s.replace(' ', '').lower()])