# Task
# Your task is to check whether a segment is completely in one quadrant or it crosses more. Return true if the segment lies in two or more quadrants. If the segment lies within only one quadrant, return false.
#
# There are two parameters: A (coord) and B (coord), the endpoints defining the segment AB.
#
# No coordinate will be zero; expect that all X and Y are positive or negative.
#
# Examples
# This whole segment is in the first quadrant.
# [(1, 2), (3, 4)] -> false
# Example 1
# This segment intersects the Y axis, therefore being in two quadrants: I and II.
# [(9, 3), (-1, 6)] -> true
# Example 2
# This segment is completely in the second quadrant.
# [(-1, 6), (-9, 1)] -> false
# Example 3
# Predefined
# There is a class named coord/Coord (see in code). It has the following members:
#
# (constructor): Constructs the coordinate
# x (number): The X coordinate
# y (number): The Y coordinate
# x (number): The X coordinate
# y (number): The Y coordinate
# Task Series
# Quadrants
# Quadrants 2: Segments (this kata)
# FUNDAMENTALSMATHEMATICSGEOMETRY
# Solution
def quadrant_segment(A, B):
    return (A[0] < 0, A[1] < 0) != (B[0] < 0, B[1] < 0)