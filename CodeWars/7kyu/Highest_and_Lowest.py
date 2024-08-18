# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.
# FUNDAMENTALSSTRINGS
# Solution
import re
def high_and_low(numbers):
    list = [int(s) for s in re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", numbers)]
    list.sort()
    integer = ''
    return integer + str(list[-1]) + ' ' + str(list[0])