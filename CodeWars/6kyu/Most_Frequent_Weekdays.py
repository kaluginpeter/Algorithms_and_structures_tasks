# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
#
# You are given a year as integer (e. g. 2001).
# You should return the most frequent day(s) of the week in that year.
# The result has to be a list of days sorted by the order of days in week
# (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.
#
# Input: Year as an int.
#
# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).
#
# Preconditions:
#
# Week starts on Monday.
# Year is between 1583 and 4000.
# Calendar is Gregorian.
# Examples (input -> output):
# * 2427 -> ['Friday']
# * 2185 -> ['Saturday']
# * 2860 -> ['Thursday', 'Friday']
# FUNDAMENTALS
# Solution
from datetime import date
def most_frequent_days(year):
    names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start = date(year,1,1).weekday()
    end = date(year, 12, 31).weekday()
    days = list(range(start, 7)) + list(range(0 ,end +1))
    total = days.count(max(days,key=days.count))
    result = []
    for day in [0,1,2,3,4,5,6]:
        if day in days:
            if days.count(day) == total:
                result.append(day)
    return list(map(lambda x: names[x], result))