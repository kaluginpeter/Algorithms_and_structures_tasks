# Write a function that returns a sequence (index begins with 1) of all the even characters from a string. If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".
#
# For example:
#
# "abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
# "a"             --> "invalid string"
# FUNDAMENTALSSTRINGSARRAYS
# Solution
def even_chars(st):
    return [i for i in st[1::2]] if 1 < len(st) < 100 else 'invalid string'