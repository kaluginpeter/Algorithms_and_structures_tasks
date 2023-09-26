# Can Santa save Christmas?
# Oh no! Santa's little elves are sick this year. He has to distribute the presents on his own.
#
# But he has only 24 hours left. Can he do it?
#
# Your Task:
# You will get an array as input with time durations as string in the following format: HH:MM:SS. Each duration represents the time taken by Santa to deliver a present. Determine whether he can do it in 24 hours or not. In case the time required to deliver all of the presents is exactly 24 hours, Santa can complete the delivery ;-) .
#
# If this kata was to easy for you. Try the harder one.
#
# This kata is part of the Collection "Date fundamentals":
# #1 Count the Days!
# #2 Minutes to Midnight
# #3 Can Santa save Christmas?
# #4 Christmas Present Calculator
# DATE TIMEFUNDAMENTALS
# Solution
def determineTime(arr):
    total_sec = sum(h * 3600 + m * 60 + s for h, m, s in [list(map(int, elem.split(':'))) for elem in arr])
    return total_sec <= 86400