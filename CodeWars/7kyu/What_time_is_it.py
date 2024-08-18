# Given a time in AM/PM format as a string, convert it to 24-hour military time time as a string.
#
# Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock
#
# Try not to use built-in Date/Time libraries.
#
# Examples
# "07:05:45PM"  -->  "19:05:45"
# "12:00:01AM"  -->  "00:00:01"
# "11:46:47PM"  -->  "23:46:47"
# DATE TIMEFUNDAMENTALS
# Solution
from datetime import datetime
def get_military_time(time):
    in_time = datetime.strptime(time, "%I:%M:%S%p")
    return datetime.strftime(in_time, "%H:%M:%S")