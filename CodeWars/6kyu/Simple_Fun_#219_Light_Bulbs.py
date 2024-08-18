# Task
# Some light bulbs are placed in a circle (clockwise direction). Each one is either on (1) or off (0).
#
# Every turn, the light bulbs change their states. If a light bulb was on at the previous turn, the light bulb to the right of it changes its state, i.e. if lights[0] is on. then, if lights[1] was on, it turns off and vice versa.
#
# Find the state of the light bulbs after n turns.
#
# Input/Output
# [input] integer array lights
# A non-empty array, the initial states of the light bulbs.
#
# 0 ≤ lights.length ≤ 100
#
# [input] integer n
# The number of turns.
#
# 0 ≤ n ≤ 300
#
# [output] an integer array
# The final light bulbs' states.
#
# Example
# For lights = [0,1,1,0,1,1], n = 2, the output should be [1, 0, 1, 1, 0, 1]
#
# Here are how the light bulbs' states change each turn:
#
# 0) 0 1 1 0 1 1   -- orginal state
# 1) 1 1 0 1 1 0   -- 1st turn
# 2) 1 0 1 1 0 1   -- 2nd turn
# If it's hard to understand, please look at the following "image" ;-)
#
# turn 0:
#      0       <--- lights[0]
#  1       1   <--- lights[5] (left) and lights[1] (right)
#  1       1   <--- lights[4] (left) and lights[2] (right)
#      0       <--- lights[3]
#
# turn 1:
#      1
#  0       1
#  1       0
#      1
# lights[0] changed to  on, because its left side (lights[5]) is on at the previous turn (turn 0)
# lights[2] changed to off, because its left side (lights[1]) is on at the previous turn (turn 0)
# lights[3] changed to  on, because its left side (lights[2]) is on at the previous turn (turn 0)
# lights[5] changed to off, because its left side (lights[4]) is on at the previous turn (turn 0)
#
# turn 2:
#      1
#  1       0
#  0       1
#      1
# lights[1] changed to off, because its left side (lights[0]) is on at the previous turn (turn 1)
# lights[2] changed to  on, because its left side (lights[1]) is on at the previous turn (turn 1)
# lights[4] changed to off, because its left side (lights[3]) is on at the previous turn (turn 1)
# lights[5] changed to  on, because its left side (lights[4]) is on at the previous turn (turn 1)
# PUZZLESALGORITHMS
# Solution
def light_bulbs(lights, n):
    return lights if not n else light_bulbs([v^lights[k-1] for k,v in enumerate(lights)], n-1)