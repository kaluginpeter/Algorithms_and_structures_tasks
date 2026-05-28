# Convert Decimal Degrees to Degrees, Minutes, Seconds.
#
# Remember: 1 degree = 60 minutes; 1 minute = 60 seconds.
#
# Input: Positive number.
#
# Output: Array [degrees, minutes, seconds]. E.g [30, 25, 25]
#
# Trailing zeroes should be omitted in the output. E.g
#
# convert (50)
# //correct output -> [50]
# //wrong output -> [50, 0, 0]
#
# convert(80.5)
# //correct output -> [ 80, 30 ]
# //wrong output -> [80, 30, 0]
#
# convert(0.0001388888888888889)
# //correct output -> [ 0, 0, 1 ]
# //wrong output -> [1]
# Round the seconds to the nearest integer.
#
# Fundamentals
# Solution
def convert(degrees):
    d = int(degrees)
    minutes_float = (degrees - d) * 60
    m = int(minutes_float)
    seconds_float = (minutes_float - m) * 60
    s = round(seconds_float)
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        d += 1

    result = [d]
    if m != 0 or s != 0: result.append(m)
    if s != 0:
        if len(result) == 1: result.append(0)
        result.append(s)
    return result