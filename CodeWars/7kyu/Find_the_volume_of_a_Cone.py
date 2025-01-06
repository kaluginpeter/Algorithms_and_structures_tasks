# Find the volume of a cone whose radius and height are provided as parameters to the function volume. Use the value of PI provided by your language (for example: Math.PI in JS, math.pi in Python or Math::PI in Ruby) and round down the volume to an Interger.
#
# If you complete this kata and there are no issues, please remember to give it a ready vote and a difficulty rating. :)
#
# GeometryFundamentals
# Solution
from math import pi
def volume(r, h):
    return int(1/3 * pi*r**2*h)