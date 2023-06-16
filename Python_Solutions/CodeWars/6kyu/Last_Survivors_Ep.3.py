# Given a list of strings (of letters and spaces), and a list of numbers:
#
# Considering the list of strings as a 2D character array,
# the idea is to remove from each column, starting from bottom,
# as many letters as indicated in the list of numbers. Then return the remaining letters in any order as a string.
#
# If there aren't enough letters, just remove those you can.
# The strings in the list will all be of the same length.
# The list of numbers will be of the same length as the strings in the list of strings.
# Strings will contain only lowercase letters and spaces.
# There can be duplicated letters and numbers.
# Example:
# strings
#
# ["abc",
#  " z ",
#  " a "]
# numbers
#
#  [0,4,1]
# the output would be "a".
#
# If you like this kata, check out another one: Survivors Ep.4
#
# FUNDAMENTALSARRAYS
# Solution
def last_survivors(a, n):
    return ''.join(i[j:] for i,j in zip([''.join(k for k in i if k!=' ')[::-1] for i in zip(*a)], n))