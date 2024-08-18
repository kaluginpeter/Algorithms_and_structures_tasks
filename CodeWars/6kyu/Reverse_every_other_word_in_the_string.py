# Reverse every other word in a given string, then return the string.
# Throw away any leading or trailing whitespace, while ensuring there is
# exactly one space between each word. Punctuation marks should be
# treated as if they are a part of the word in this kata.
#
# ARRAYSFUNDAMENTALS
# Solution
def reverse_alternate(s):
    list = s.split()
    for elem in list[1::2]:
        word = elem[::-1]
        list.insert(list.index(elem), word)
        list.remove(elem)
    return ' '.join(list)