# Given a positive integer n, return first n dgits of Thue-Morse sequence, as a string (see examples).
#
# Thue-Morse sequence is a binary sequence with 0 as the first element. The rest of the sequence is obtained by adding the boolean (binary) complement of a group obtained so far.
#
# For example:
#
# 0
# 01
# 0110
# 01101001
# and so on...
# alt
#
# Ex.:
#
#  1 --> "0"
#  2 --> "01"
#  5 --> "01101"
# 10 --> "0110100110"
# You don't need to test if n is valid - it will always be a positive integer.
# n will be between 1 and 10000
# Thue-Morse on Wikipedia
#
# Another kata on Thue-Morse by @myjinxin2015
#
# STRINGSBINARYALGORITHMS
# Solution
def thue_morse(n):
    if n == 1: return '0'
    n -= 1
    digits: list[str] = ['0']
    accumulate: int = ''
    while len(digits) <= n:
        new_pair: list[str] = [['1', '0'][i == '1'] for i in digits]
        digits.extend(new_pair)
    return ''.join(digits[:n + 1])