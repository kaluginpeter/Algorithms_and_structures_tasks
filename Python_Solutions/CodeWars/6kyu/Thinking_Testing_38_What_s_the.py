# No Story
#
# No Description
#
# Only by Thinking and Testing
#
# Look at result of testcase, guess the code!
#
# #Series:
# 01:A and B?
# 02:Incomplete string
# 03:True or False
# 04:Something capitalized
# 05:Uniq or not Uniq
# 06:Spatiotemporal index
# 07:Math of Primary School
# 08:Math of Middle school
# 09:From nothingness To nothingness
# 10:Not perfect? Throw away!
# 11:Welcome to take the bus
# 12:A happy day will come
# 13:Sum of 15(Hetu Luosliu)
# 14:Nebula or Vortex
# 15:Sport Star
# 16:Falsetto Rap Concert
# 17:Wind whispers
# 18:Mobile phone simulator
# 19:Join but not join
# 20:I hate big and small
# 21:I want to become diabetic ;-)
# 22:How many blocks?
# 23:Operator hidden in a string
# 24:Substring Magic
# 25:Report about something
# 26:Retention and discard I
# 27:Retention and discard II
# 28:How many "word"?
# 29:Hail and Waterfall
# 30:Love Forever
# 31:Digital swimming pool
# 32:Archery contest
# 33:The repair of parchment
# 34:Who are you?
# 35:Safe position
# 36:Sort in order
# 37:Convert number
# 38:What's the "?"
#
# PUZZLESGAMES
# Solution
def test_it(arr):
    colors: dict[str, int] = dict()
    shapes: dict[str, int] = dict()
    for item in arr:
        if item == '?': continue
        color, shape = item.split()
        colors[color] = colors.get(color, 0) + 1
        shapes[shape] = shapes.get(shape, 0) + 1
    color, color_time = None, float('inf')
    shape, shape_time = None, float('inf')
    for name, time in colors.items():
        if color_time > time:
            color, color_time = name, time
    for name, time in shapes.items():
        if shape_time > time:
            shape, shape_time = name, time
    return color + ' ' + shape