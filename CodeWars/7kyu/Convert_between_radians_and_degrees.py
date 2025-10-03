# Extend the Math object/module to convert degrees to radians and vice versa. Return the result in string format, rounded to two decimal points when not an integer, otherwise truncate the result (see the examples).
#
# Note that all methods of Math object are static.
#
# Examples
# math.degrees(math.pi)  -->  "180deg"
# math.radians(180)      -->  "3.14rad"
# MathematicsFundamentals
# Solution
def degrees(rad):
    x: float = round(180 / math.pi * rad, 2)
    if int(x) == x: return f'{int(x)}deg'
    return f'{x}deg'

def radians(deg):
    y: float = round(math.pi / 180 * deg, 2)
    if int(y) == y: return f'{int(y)}rad'
    return f'{y}rad'

math.degrees = degrees
math.radians = radians