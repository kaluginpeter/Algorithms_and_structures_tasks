# Task
# Write a function that receives a non-negative integer n ( n >= 0 )
# and returns the next higher multiple of five of that number, obtained
# by concatenating the shortest possible binary string to the end of this number's binary representation.
#
# Examples
# 1.  next_multiple_of_five(8)
# Steps:
#
# 8 to binary == '1000'
# concatenate shortest possible string '11' to obtain '1000' + '11' == '100011'
# '100011' to decimal == 35 => the answer
# ('001' would do the job too, but '11' is the shortest string here)
#
# 2.  next_multiple_of_five(5)
# Steps:
#
# 5 to binary =='101'
# concatenate shortest possible string '0' to obtain '101' + '0' == '1010'
# '1010' to decimal == 10
# (5 is already a multiple of 5, obviously, but we're looking for the next multiple of 5)
#
# Note
# Numbers up to 1e10 will be tested, so you need to come up with something smart.
# ALGORITHMSLOGICPERFORMANCE
# Solution
def next_multiple_of_five(n):
    s = n % 5
    if n == 0:return 5
    elif s == 0:c = '0'
    elif s == 1:c = '01'
    elif s == 2:c = '1'
    elif s == 3:c = '11'
    elif s == 4:c = '011'
    return int(bin(n)[2:]+c,2)