# In this Kata, you will be given a series of times at which an alarm sounds. Your task will be to determine the maximum time interval between alarms. Each alarm starts ringing at the beginning of the corresponding minute and rings for exactly one minute. The times in the array are not in chronological order. Ignore duplicate times, if any.
#
# For example:
# solve(["14:51"]) = "23:59". If the alarm sounds now, it will not sound for another 23 hours and 59 minutes.
# solve(["23:00","04:22","18:05","06:24"]) == "11:40". The max interval that the alarm will not sound is 11 hours and 40 minutes.
# In the second example, the alarm sounds 4 times in a day.
#
# More examples in test cases. Good luck!
#
# ALGORITHMSDATE TIMESTRINGS
# Solution
from datetime import datetime
def solve(arr):
    l = [datetime(2000, 1, 1, *map(int, x.split(':'))) for x in sorted(arr)]
    c = max(int((j - i).total_seconds() - 60) for i, j in zip(l, l[1:] + [l[0].replace(day=2)]))
    return '{:02}:{:02}'.format(*divmod(c//60, 60))