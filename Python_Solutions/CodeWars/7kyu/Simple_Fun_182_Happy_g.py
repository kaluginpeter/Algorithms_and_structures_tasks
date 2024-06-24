# Task
# Let's say that "g" is happy in the given string, if there is another "g" immediately to the right or to the left of it.
#
# Find out if all "g"s in the given string are happy.
#
# Example
# For str = "gg0gg3gg0gg", the output should be true.
#
# For str = "gog", the output should be false.
#
# Input/Output
# [input] string str
# A random string of lower case letters, numbers and spaces.
#
# [output] a boolean value
# true if all "g"s are happy, false otherwise.
#
# PUZZLESSTRINGSREGULAR EXPRESSIONS
# Solution
def happy_g(st):
    idx: int = 0
    while idx < len(st):
        if st[idx] == 'g':
            if idx > 0 and st[idx - 1] == 'g': idx += 1
            elif idx + 1 == len(st): return False
            elif st[idx + 1] != 'g': return False
            else: idx += 1
        else:
            idx += 1
    return True