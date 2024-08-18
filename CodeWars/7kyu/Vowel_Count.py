# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.
#
# STRINGSFUNDAMENTALS
# Solution
def get_count(sentence):
    gl = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for x in sentence:
        if x in gl:
             count += 1
    return count