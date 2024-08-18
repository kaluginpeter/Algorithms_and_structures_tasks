# Task
# You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have already watched.
#
# Example
# For part = "02:20:00" and total = "07:00:00", the output should be [1, 3].
#
# You have watched 1 / 3 of the whole video.
#
# Input/Output
# [input] string part
#
# A string of the following format "hh:mm:ss" representing the time you have been watching the video.
#
# [input] string total
#
# A string of the following format "hh:mm:ss" representing the total video duration.
#
# [output] an integer array
#
# An array of the following format [a, b] (where a / b is a reduced fraction).
#
# PUZZLES
# Solution
from math import gcd
def video_part(part, total):
    ch, cm, cs = map(int, part.split(':'))
    th, tm, ts = map(int, total.split(':'))
    x = th * 3600 + tm * 60 + ts
    y = ch * 3600 + cm * 60 + cs
    d = gcd(x, y)
    return [y // d, x // d]