# Our standard numbering system is base-10, that uses digits 0 through 9. Binary is base-2, using only 1s and 0s. And hexadecimal is base-16, using digits 0 to 9 and A to F. A hexadecimal F has a base-10 value of 15.
#
# Base-64 has 64 individual characters ("digits") which translate to the base-10 values of 0 to 63. These are (in ascending order):
#
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
# (so A is equal to 0 and / is equal to 63)
#
# Task
# Complete the method that will take a base-64 number (as a string) and output its base-10 value as an integer.
#
# Examples
# "/"   -->  63
# "BA"  -->  64
# "BB"  -->  65
# "BC"  -->  66
# "WIN" -->  90637
# Puzzles
# Solution
def base64_to_base10(s):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    mp = {c: i for i, c in enumerate(digits)}
    ans = 0
    for c in s:
        ans = ans * 64 + mp[c]
    return ans