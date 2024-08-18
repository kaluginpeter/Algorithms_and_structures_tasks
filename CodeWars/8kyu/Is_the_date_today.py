# Write a simple function that takes a Date as a parameter and returns a Boolean representing whether the date is today or not.
#
# Make sure that your function does not return a false positive by only checking the day.
#
# DATE TIMEPUZZLES
# Solution
from datetime import datetime
def is_today(date):
    return date.date() == datetime.today().date()