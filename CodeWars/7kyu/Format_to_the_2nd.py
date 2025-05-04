# Given some positive integers, I wish to print the integers such that all take up the same width by adding a minimum number of leading zeroes. No leading zeroes shall be added to the largest integer.
#
# For example, given 1, 23, 2, 17, 102, I wish to print out these numbers as follows:
#
# 001
# 023
# 002
# 017
# 102
# Write a function that takes a variable number of integers and returns the string to be printed out.
#
# StringsFundamentals
# Solution
def print_nums(*args):
    if not args: return ''
    x: int = max(args)
    width: int = 0
    while x:
        width += 1
        x //= 10
    return '\n'.join(f'{"0" * (width - len(str(num)))}{num}' for num in args)