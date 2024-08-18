# Task
# You are given a function that should insert an asterisk (*) between every pair of even digits in the given input, and return it as a string. If the input is a sequence, concat the elements first as a string.
#
# Input
# The input can be an integer, a string of digits or a sequence containing integers only.
#
# Output
# Return a string.
#
# Examples
# 5312708     -->  "531270*8"
# "0000"      -->  "0*0*0*0"
# [1, 4, 64]  -->  "14*6*4"
# Have fun!
#
# STRINGSALGORITHMS
# Solution
def asterisc_it(n):
    if type(n) == list: n = ''.join(str(i) for i in n)
    if type(n) == int : n = str(n)
    return ''.join([a + '*' if int(a) % 2 == 0 and int(b) % 2 == 0 else a for a,b in zip(n, n[1:])]) + n[-1]