# In this kata, we will make a function to test whether a period is late.
#
# Our function will take three parameters:
#
# last - The Date object with the date of the last period
#
# today - The Date object with the date of the check
#
# cycleLength - Integer representing the length of the cycle in days
#
# Return true if the number of days passed from last to today is greater than cycleLength. Otherwise, return false.
#
# FUNDAMENTALSDATE TIME
# Solution
from datetime import *
def period_is_late(last, today, cycle_length):
    return last + timedelta(days = cycle_length) < today