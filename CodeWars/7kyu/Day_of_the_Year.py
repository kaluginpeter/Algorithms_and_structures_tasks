# Work out what number day of the year it is.
#
# toDayOfYear([1, 1, 2000]) => 1
# The argument passed into the function is an array with the format [D, M, YYYY], e.g. [1, 2, 2000] for February 1st, 2000 or [22, 12, 1999] for December 22nd, 1999.
#
# Don't forget to check for whether it's a leap year! Three criteria must be taken into account to identify leap years:
#
# The year can be evenly divided by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.
# FUNDAMENTALS
# Solution
import calendar
def to_day_of_year(date):
    count = 0
    for i in range(1, date[1]):
        count += calendar.monthrange(date[-1], i)[1]
    count += date[0]
    return count