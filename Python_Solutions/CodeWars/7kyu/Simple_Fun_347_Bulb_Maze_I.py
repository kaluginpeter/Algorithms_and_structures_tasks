# Description
# You are fleeing from enemies through a maze. You need to reach the exit through many rooms that are laid out in a straight line.
#
# Some rooms have a light bulb. If the light bulb is lit when you enter the room, the enemy will see you and you will be caught. In other words, you can only walk in the darkness.
#
# Fortunately, the status of these bulbs (on/off) is switched automatically every minute. So you have a chance to go through the maze, if the lightbulbs are turned off at the right time.
#
# You have to be constantly on the move, otherwise the enemy will catch up to you.
#
# Specifications
# The rooms are represented by a string, e.g. "xo oxox".
#
# 'x' means there is a bulb in the room, and its initial status is off
# 'o' means there is a bulb in the room, and its initial status is on
# ' '(space) means a room without bulb, it is always dark.
# Your task is to determine if you can go through the maze. Return true if you can, false otherwise.
#
# Notes
# Your initial position is at the leftmost room; the exit position is at the rightmost.
# Your moving speed is 1 minute per room. You have to keep moving constantly, i.e. you cannot wait for the next room to become dark.
# You have to start moving immediately.
# Examples
# For "xo oxox", the output should be true:
#
# step 0 :  xo oxox
#           ^ <--------You are here
# step 1 :  ox xoxo
#            ^ <--------You are here
# step 2 :  xo oxox
#             ^ <--------You are here
# step 3 :  ox xoxo
#              ^ <--------You are here
# step 4 :  xo oxox
#               ^ <--------You are here
# step 5 :  ox xoxo
#                ^ <--------You are here
# step 6 :  xo oxox
#                 ^ <--------You are here
# step 7 :  ox xoxo
#                  ^ <--------You've go through the maze :)
# For "xo  oxox", the output should be false:
#
# step 0 :  xo  oxox
#           ^ <--------You are here
# step 1 :  ox  xoxo
#            ^ <--------You are here
# step 2 :  xo  oxox
#             ^ <--------You are here
# step 3 :  ox  xoxo
#              ^ <--------You are here
# step 4 :  xo  oxox
#               ^ <--------You were caught by the enemy :(
# Happy Coding ^_^
#
# FUNDAMENTALS