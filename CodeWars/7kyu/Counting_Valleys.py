# You need count how many valleys you will pass.
#
# Start is always from zero level.
#
# Every time you go down below 0 level counts as an entry of a valley, and as you go up to 0 level from valley counts as an exit of a valley.
#
# One passed valley is equal one entry and one exit of a valley.
#
# s='FUFFDDFDUDFUFUF'
# U=UP
# F=FORWARD
# D=DOWN
# To represent string above
#
# (level 1)  __
# (level 0)_/  \         _(exit we are again on level 0)
# (entry-1)     \_     _/
# (level-2)       \/\_/
# So here we passed one valley
#
# ALGORITHMSSTRINGS
# Solution
def counting_valleys(s):
    level, valleys = 0, 0
    for step in s:
        if step == 'U' and level == -1:
            valleys += 1
        level += {'U': 1, 'F': 0, 'D': -1}[step]
    return valleys