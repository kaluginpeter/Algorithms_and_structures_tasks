# This time no story, no theory. The examples below show you how to write function accum:
#
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.
#
# FUNDAMENTALSSTRINGSPUZZLES
# Solution
def accum(s):
    word = ''
    count = -1
    for i in s:
        count+=1
        char = i.lower() * count
        word = word + (i.upper() + char + '-')
    return word[:-1]