# When provided with a String, capitalize all vowels
#
# For example:
#
# Input : "Hello World!"
#
# Output : "HEllO WOrld!"
#
# Note: Y is not a vowel in this kata.
#
# FUNDAMENTALSSTRINGS
# Solution
def swap(st):
    return ''.join(i.swapcase() if i in 'aeiou' else i for i in st)