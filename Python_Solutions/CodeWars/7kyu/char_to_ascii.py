# Take a string and return a hash with all the ascii values of the characters in the string. Returns nil if the string is empty. The key is the character, and the value is the ascii value of the character. Repeated characters are to be ignored and non-alphebetic characters as well.
#
# STRINGSPARSINGFUNDAMENTALS
# Solution
def char_to_ascii(s):
    if isinstance(s, str) and s != '':
        d = {}
        for i in s:
            if i not in d and i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': d[i] = ord(i)
        return d