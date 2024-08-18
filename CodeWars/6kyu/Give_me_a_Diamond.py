# Jamie is a programmer, and James' girlfriend. She likes diamonds,
# and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.
#
# Task
# You need to return a string that looks like a diamond shape when printed on the screen,
# using asterisk (*) characters. Trailing spaces should be removed, and every line must be
# terminated with a newline character (\n).
#
# Return null/nil/None/... if the input is an even number or negative, as it is not possible
# to print a diamond of even or negative size.
#
# Examples
# A size 3 diamond:
#
#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"
#
# A size 5 diamond:
#
#   *
#  ***
# *****
#  ***
#   *
# ...that is:
#
# "  *\n ***\n*****\n ***\n  *\n"
# STRINGSASCII ARTFUNDAMENTALS
# Solution
def diamond(n):
    if n < 1 or not n % 2:
        return None
    s = ''
    for i in range(n):
        ast = '*'*(i*2 + 1) if i <= n/2 else '*'*((n-i)*2 - 1)
        s += ' '*int((n-len(ast)) / 2) + ast + '\n'
    return s