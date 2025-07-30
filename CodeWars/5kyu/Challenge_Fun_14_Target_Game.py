# Task
# In your favorite game, you must shoot a target with a water-gun to gain points. Each target can be worth a different amount of points.
#
# You are guaranteed to hit every target that you try to hit. You cannot hit consecutive targets though because targets are only visible for one second (one at a time) and it takes you a full second to reload your water-gun after shooting (you start the game already loaded).
#
# Given an array vals with the order of each target's point value, determine the maximum number of points that you can win.
#
# Example
# For vals = [1, 2, 3, 4], the result should be 6.
#
# your optimal strategy would be to let the first one pass and shoot the second one with value 2 and the 4th one with value 4 thus:
#
# vals[1](2) + vals[3](4) = 6
#
# For vals = [5, 5, 5, 5, 5], the result should be 15.
#
# your optimal strategy would be to shoot the 1st, 3rd and 5th value:
#
# 5 + 5 + 5 = 15
#
# You haven't shoot the 2nd, 4th value because you are reloading your water-gun after shooting other values.
#
# Note that the value can be zero or negative, don't shoot them ;-)
#
# For vals = [0, 0, -1, -1], the result should be 0.
#
# For vals = [5, -2, -9, -4], the result should be 5.
#
# Shoot the first one is enough.
#
# Input/Output
# [input] integer array vals
# The point values (negative or non-negative) of the targets (in order of appearance).
#
# [output] an integer
# The maximum number of points that you can score.
#
# AlgorithmsArrays