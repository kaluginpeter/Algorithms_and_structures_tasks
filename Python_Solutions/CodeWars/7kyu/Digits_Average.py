# Given an integer, take the (mean) average of each pair of consecutive digits. Repeat this process until you have a single integer, then return that integer. e.g.
#
# Note: if the average of two digits is not an integer, round the result up (e.g. the average of 8 and 9 will be 9)
#
# Examples
# digitsAverage(246)  ==>  4
#
# original: 2   4   6
#            \ / \ /
# 1st iter:   3   5
#              \ /
# 2nd iter:     4
#
#
# digitsAverage(89)  ==>  9
#
# original: 8   9
#            \ /
# 1st iter:   9
# p.s. for a bigger challenge, check out the one line version of this kata by myjinxin2015!
#
# ALGORITHMS
# Solution
def digits_average(input):
    l = [int(c) for c in str(input)]
    while len(l) > 1:
        l = [(a + b + 1)//2 for a, b in zip(l, l[1:])]
    return l[0]