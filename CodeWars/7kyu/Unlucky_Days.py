# Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.
#
# Find the number of Friday 13th in the given year.
#
# Input: Year in Gregorian calendar as integer.
#
# Output: Number of Black Fridays in the year as an integer.
#
# Examples:
#
# unluckyDays(2015) == 3
# unluckyDays(1986) == 1
# DATE TIME
# Solution
import calendar
def unlucky_days(year):
	return sum(calendar.weekday(year, m, 13) == 4 for m in range(1, 13))