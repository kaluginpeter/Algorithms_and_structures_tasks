# Since there are lots of katas requiring you to round numbers to 2 decimal places, you decided to extract the method to ease out the process.
#
# And you can't even get this right!
#
# Quick, fix the bug before everyone in CodeWars notices that you can't even round a number correctly!
#
# FUNDAMENTALSDEBUGGING
# Solution
from decimal import Decimal, ROUND_HALF_UP
def round_by_2_decimal_places(n):
    return n.quantize(Decimal('.01'), rounding = ROUND_HALF_UP)