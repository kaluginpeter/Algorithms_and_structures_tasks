# Given a Date (in JS and Ruby) or hours and minutes (in C and Python), return the angle between the two hands of a 12-hour analog clock in radians.
#
# Notes:
# The minute hand always points to the exact minute (there is no seconds hand).
# The hour hand does not "snap" to the tick marks: e.g. at 6:30 the angle is not 0 because the hour hand is already half way between 6 and 7.
# Return the smaller of the angles ( <= π ).
# Return π if the hands are opposite.
# Examples
# at noon the angle is: 0
# at 3:00 the angle is: π/2 (90 degrees)
# at 6:00 the angle is: π (180 degrees)
# at 9:00 the angle is: π/2 (90 degrees)
# MATHEMATICSDATE TIMEALGORITHMS
# Solution
from math import pi
def hand_angle(hours, minutes):
    h, m = .5 * (60 * hours + minutes), 6 * minutes
    angel = abs(h - m)
    x = min(angel, 360 - angel)
    return (pi / 180) * x