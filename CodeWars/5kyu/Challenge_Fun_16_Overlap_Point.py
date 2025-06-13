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
# Solution
import math

def math_stuff(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    r1_sq = r1 * r1
    r2_sq = r2 * r2
    x_min = math.ceil(max(x1 - r1, x2 - r2))
    x_max = math.floor(min(x1 + r1, x2 + r2))
    total_points = 0
    for x in range(int(x_min), int(x_max) + 1):
        dx1_sq = (x - x1)**2
        if dx1_sq > r1_sq: continue
        h1 = math.sqrt(r1_sq - dx1_sq)
        y1_start = y1 - h1
        y1_end = y1 + h1
        dx2_sq = (x - x2)**2
        if dx2_sq > r2_sq: continue
        h2 = math.sqrt(r2_sq - dx2_sq)
        y2_start = y2 - h2
        y2_end = y2 + h2
        final_y_start = max(y1_start, y2_start)
        final_y_end = min(y1_end, y2_end)
        iy_start = math.ceil(final_y_start)
        iy_end = math.floor(final_y_end)
        if iy_start <= iy_end:
            points_in_slice = iy_end - iy_start + 1
            total_points += points_in_slice
    return int(total_points)

def overlap_point(c1, c2):
    return math_stuff(c1, c2)