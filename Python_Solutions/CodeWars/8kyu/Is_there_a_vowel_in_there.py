# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).
#
# If they are, change the array value to a string of that vowel.
#
# Return the resulting array.
#
# FUNDAMENTALSSTRINGSARRAYS
# Solution
def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(elem, elem) for elem in s]