# You have an amount of money a0 > 0 and you deposit it with an interest rate of p percent divided by 360 per day on the 1st of January 2016. You want to have an amount a >= a0.
#
# Task:
# The function date_nb_days (or dateNbDays...) with parameters a0, a, p will return, as a string, the date on which you have just reached a.
#
# Example:
# date_nb_days(100, 101, 0.98) --> "2017-01-01" (366 days)
#
# date_nb_days(100, 150, 2.00) --> "2035-12-26" (7299 days)
#
# Notes:
# The return format of the date is "YYYY-MM-DD"
# The deposit is always on the "2016-01-01"
# Don't forget to take the rate for a day to be p divided by 36000 since banks consider that there are 360 days in a year.
# You have: a0 > 0, p% > 0, a >= a0
# FUNDAMENTALSMATHEMATICS
# Solution
from math import ceil, log
from datetime import date, timedelta as td
def date_nb_days(a0, a, p):
    dur = log(a, 1 + p / 36000.0) - log(a0, 1 + p / 36000.0)
    return str(date(2016, 1, 1) + td(ceil(dur)))