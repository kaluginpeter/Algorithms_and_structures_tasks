# Generate a valid randomly generated hexadecimal color string. Assume all of them always have 6 digits.
#
# Valid Output
# #ffffff
# #FfFfFf
# #25a403
# #000001
# Non-Valid Output
# #fff
# #aaa
# #zzzzz
# cafebabe
# #a567567676576756A7
# PUZZLES
# Solution
import random
def generate_color_rgb():
    return ['#%06X' % random.randint(0, 0xFFFFFF)][0]