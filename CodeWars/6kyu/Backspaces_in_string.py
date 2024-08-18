# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#
# Your task is to process a string with "#" symbols.
#
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""
# FUNDAMENTALSSTRINGSALGORITHMS
# Solution
def clean_string(s):
    l = []
    for i in s:
        if i == '#' and l: l.pop()
        elif i != '#': l.append(i)
    return ''.join(l)
