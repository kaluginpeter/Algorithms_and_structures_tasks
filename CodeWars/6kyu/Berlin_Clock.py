# The "Berlin Clock" is the first public clock in the world that tells the time by means of illuminated, coloured fields, for which it entered the Guinness Book of Records upon its installation on 17 June 1975.
#
# alt text
#
# The clock is read from the top row to the bottom:
#
# the round Yellow light on top blinks to denote even- (when on) or odd-numbered (off) seconds,
# the first row of four Red fields denote five full hours each,
# the second row, also of four Red fields, which denote one full hour each (displaying the hour value in 24-hour format)
# the third row consists of eleven Yellow-and-Red fields, which denote five full minutes each (the red ones also denoting 15, 30 and 45 minutes past),
# the bottom row has another four Yellow fields, which mark one full minute each.
# For example:
#
# Two fields are lit in the first row (2 x 5 = 10), but no fields are lit in the second row (0); therefore the hour value is 10. Six fields are lit in the third row (6 x 5 = 30), while the bottom row has one field on (1). Hence, the lights of the clock altogether tell the time as 10:31 (Source: Wikipedia)
#
# Task
# Complete the function that takes a particular time in 24h format ("hh:mm:ss") and outputs a string that reproduces the Berlin Clock. The lights should be represented as follows:
#
# R : Red
# Y : Yellow
# O : Off
# Note: the rows of the output string should be joined with newlines (\n) - see the examples below.
#
# Examples
# "12:56:01"  ==>  "O\nRROO\nRROO\nYYRYYRYYRYY\nYOOO"
#
# # when printed:
# O
# RROO
# RROO
# YYRYYRYYRYY
# YOOO
#
# "00:00:00"  ==>  "Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"
# "22:32:45"  ==>  "O\nRRRR\nRROO\nYYRYYROOOOO\nYYOO"
# Date TimeStringsFundamentals
# Solution
def berlin_clock(t):
 h,m,s=map(int,t.split(':'))
 return'\n'.join([
 'YO'[s%2],
 'R'*(h//5)+'O'*(4-h//5),
 'R'*(h%5)+'O'*(4-h%5),
 ('YYR'*4)[:m//5].ljust(11,'O'),
 'Y'*(m%5)+'O'*(4-m%5)])