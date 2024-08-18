# Little Annie is very excited for upcoming events. She wants to know how many days she has to wait for a specific event.
#
# Your job is to help her out.
#
# Task: Write a function which returns the number of days from today till the given date. The function will take a Date object as parameter. You have to round the amount of days.
#
# If the event is in the past, return "The day is in the past!"
# If the event is today, return "Today is the day!"
# Else, return "x days"
#
# PS: This is my first kata. I hope you have fun^^
#
# This kata is part of the Collection "Date fundamentals":
#
# #1 Count the Days!
# #2 Minutes to Midnight
# #3 Can Santa save Christmas?
# #4 Christmas Present Calculator
# DATE TIMEFUNDAMENTALS
# Solution
from datetime import datetime
def count_days(event_date):
    today = datetime.today()
    diff = event_date - today
    days = round(diff.total_seconds() / (24*60*60))
    if days < 0:
        return "The day is in the past!"
    elif days == 0:
        return "Today is the day!"
    return f"{days} days"