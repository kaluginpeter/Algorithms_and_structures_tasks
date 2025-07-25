# Task
# N lamps are placed in a line, some are switched on and some are off. What is the smallest number of lamps that need to be switched so that on and off lamps will alternate with each other?
#
# You are given an array a of zeros and ones - 1 mean switched-on lamp and 0 means switched-off.
#
# Your task is to find the smallest number of lamps that need to be switched.
#
# Example
# For a = [1, 0, 0, 1, 1, 1, 0], the result should be 3.
#
# a      --> 1 0 0 1 1 1 0
# switch --> 0 1     0
# became --> 0 1 0 1 0 1 0
# Input/Output
# [input] integer array a
# array of zeros and ones - initial lamp setup, 1 mean switched-on lamp and 0 means switched-off.
#
# 2 < a.length <= 1000
#
# [output] an integer
# minimum number of switches.
#
# Puzzles
# Solution
def lamps(a):
    # only two cases
    # 1st start with "on"
    first_case: int = sum(a[i] == 1 if i & 1 else a[i] == 0 for i in range(len(a)))
    # 2nd start with "off"
    second_case: int = sum(a[i] == 0 if i & 1 else a[i] == 1 for i in range(len(a)))
    return min(first_case, second_case)