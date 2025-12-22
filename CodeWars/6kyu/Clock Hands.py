# In some parts of the world you might still find round analog clocks with hour, minute, and second hands. Such clocks are divided up into 12 hours, with a 12 at the top and a 6 at the bottom.
#
# Write a function that produces a sequence of successive times in which the hour and minute hand make a given angle, which will be given in degrees, measured clockwise from the hour hand to the minute hand. The times must be formatted as HH:MM:SS, zero-padding all time components. Use 12 (not 00) for the hour component for midnight. If the actual time is in between two seconds, choose the smaller time value.
#
# The first result in your array should be either midnight or the first time after midnight, such as 12:32:43 for the 180 degree case. There should be only 11 results in the output.
#
# Date TimeMathematicsGeometryFundamentals
# Solution
import math

def clock_hands(angle):
    times = []
    for k in range(-12, 12):
        t = (angle + 360 * k) / 5.5
        if t < 0: continue
        total_seconds = math.floor(t * 60)
        hours = (total_seconds // 3600) % 12
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        if hours == 0: hours = 12
        times.append((total_seconds, f"{hours:02d}:{minutes:02d}:{seconds:02d}"))
    times.sort(key=lambda x: x[0])
    return [t[1] for t in times[:11]]