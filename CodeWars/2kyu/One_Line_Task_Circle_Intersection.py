# Task
# Given two congruent circles a and b of radius r, return the area of their intersection rounded down to the nearest integer.
#
# Code Limit
# Javascript: Less than 94 characters.
#
# Python: Less than 128 characters.
#
# To remain consistent across version, your code should also not include the 'assignment operator' :=.
#
# Example
# For c1 = [0, 0], c2 = [7, 0] and r = 5,
#
# the output should be 14.
#
# PuzzlesRestricted
# Solution
from numpy import*;circleIntersection=lambda x,y,r:(lambda z:int(max(0,r*r*(z-sin(z)))))(arccos(hypot(*array(x)-y)/2/r)*2)