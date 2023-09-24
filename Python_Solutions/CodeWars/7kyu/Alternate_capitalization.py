# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.
#
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
#
# The input will be a lowercase string with no spaces.
#
# Good luck!
#
# If you like this Kata, please try:
#
# Indexed capitalization
#
# Even-odd disparity
#
# STRINGSFUNDAMENTALS
# Solution
def capitalize(s):
    even = ''.join([word.capitalize()  if i % 2 == 0 else word for i, word in enumerate(s)])
    odd = ''.join([word.capitalize()  if i % 2 == 1 else word for i, word in enumerate(s)])
    return [even, odd]