# Description:
# Convert the continuous exclamation marks or question marks to a digit, Use all the digits to form a number.
# If this number is a prime number, return it. If not, divide this number by the smallest factor that it is greater
# than 1, until it becomes a prime number.
#
# You can assume that all test results are greater than 1 and the length of a continuous substring(! or ?)
# is always less than 10.
#
# Examples
# convert("!!") == 2
# convert("!??") == 3
# (12 --> 6 --> 3)
# convert("!???") == 13
# convert("!!!??") == 2
# (32 --> 16 --> 8 --> 4 --> 2)
# convert("!!!???") == 11
# (33 --> 11)
# convert("!???!!") == 11
# (132 --> 66 --> 33 --> 11)
# convert("!????!!!?") == 53
# (1431 --> 477 --> 159 --> 53)
# convert("!!!!!!!???????") == 11
# (77 --> 11)
# Note
# Please don't post issue about difficulty or duplicate.
#
# FUNDAMENTALS
# Solution
import re
def convert(s):
    n = int("".join(str(len(e)) for e in re.findall("!+|\?+", s)))
    for i in range(2, int(n**0.5) + 1):
        while n > i and n % i == 0: n //= i
    return n