# Task
# Given 2 circles c1 and c2, output the number of integer points inside the intersection area between them.
#
# Each circle is represented as an array of three elements. The first two elements are the coordinates of the center, the third is the radius.
#
# Example
# For c1 = [2, 2, 3] and c2 = [0, -1, 3], the output should be 8 (see the picture below)
#
#
#
# There are 8 integer points inside the intersection area between them:
#
# (0,2),(0,1),(1,1),(2,1),(0,0),(1,0),(2,0),(2,-1)
#
# Input/Output
# [input] integer array c1
# The first circle.
#
# -1000 ≤ c1[0] and c1[1](coordinates) ≤ 1000
#
# -1600 ≤ c1[2](radius) ≤ 1600
#
# [input] integer array c2
# The second circle.
#
# -1000 ≤ c2[0] and c2[1](coordinates) ≤ 1000
#
# -1600 ≤ c2[2](radius) ≤ 1600
#
# [output] an integer
# The number of integer points inside the intersection area between c1 and c2.
#
# Algorithms