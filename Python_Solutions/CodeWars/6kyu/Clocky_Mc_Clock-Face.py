# Story
# Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.
#
# And because the local council has lost most of our tax money to a Nigerian email
# scam there are no funds to fix the clock properly.
#
# Instead, they are asking for volunteer programmers to write some code that tell
# the time by only looking at the remaining hour-hand!
#
# What a bunch of cheapskates!
#
# Can you do it?
#
# Kata
# Given the angle (in degrees) of the hour-hand, return the time in 12 hour HH:MM format.
# Round down to the nearest minute.
#
# Examples
# 12:00 = 0 degrees
#
# 03:00 = 90 degrees
#
# 06:00 = 180 degrees
#
# 09:00 = 270 degrees
#
# 12:00 = 360 degrees
#
# Notes
# 0 <= angle <= 360
#
# Do not make any AM or PM assumptions for the HH:MM result. They are indistinguishable for this Kata.
#
# 3 o'clock is 03:00, not 15:00
# 7 minutes past midnight is 12:07
# 7 minutes past noon is also 12:07
# FUNDAMENTALS
# Solution
import math
def what_time_is_it(angle):
    calc = math.floor(angle / 30)
    remain = angle % 30
    min = math.floor(remain * 2)
    if angle == 0: return "12:00"
    elif calc == 0 and min < 10: return f"12:0{min}"
    elif calc == 0 and min > 9: return f"12:{min}"
    elif remain == 0 and calc < 10: return f"0{calc}:00"
    elif remain == 0 and calc > 9: return f"{calc}:00"
    elif min < 10 and calc < 10: return f"0{calc}:0{min}"
    elif min < 10 and calc > 9: return f"{calc}:0{min}"
    elif min > 9 and calc < 10: return f"0{calc}:{min}"
    elif min > 9 and calc > 9: return f"{calc}:{min}"