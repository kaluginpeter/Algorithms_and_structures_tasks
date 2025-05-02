# B. Vlad and Shapes
# time limit per test1 second
# memory limit per test256 megabytes
# Vladislav has a binary square grid of n×n
#  cells. A triangle or a square is drawn on the grid with symbols 1
# . As he is too busy being cool, he asks you to tell him which shape is drawn on the grid.
#
# A triangle is a shape consisting of k
#  (k>1
# ) consecutive rows, where the i
# -th row has 2⋅i−1
#  consecutive characters 1
# , and the central 1s are located in one column. An upside down triangle is also considered a valid triangle (but not rotated by 90 degrees).
# Two left pictures contain examples of triangles: k=4
# , k=3
# . The two right pictures don't contain triangles.
# A square is a shape consisting of k
#  (k>1
# ) consecutive rows, where the i
# -th row has k
#  consecutive characters 1
# , which are positioned at an equal distance from the left edge of the grid.
# Examples of two squares: k=2
# , k=4
# .
# For the given grid, determine the type of shape that is drawn on it.
#
# Input
# The first line contains a single integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (2≤n≤10
# ) — the size of the grid.
#
# The next n
#  lines each contain n
#  characters 0
#  or 1
# .
#
# The grid contains exactly one triangle or exactly one square that contains all the 1
# s in the grid. It is guaranteed that the size of the triangle or square is greater than 1
#  (i.e., the shape cannot consist of exactly one 1).
#
# Output
# For each test case, output "SQUARE" if all the 1
# s in the grid form a square, and "TRIANGLE" otherwise (without quotes).
#
# Example
# InputCopy
# 6
# 3
# 000
# 011
# 011
# 4
# 0000
# 0000
# 0100
# 1110
# 2
# 11
# 11
# 5
# 00111
# 00010
# 00000
# 00000
# 00000
# 10
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 1111111110
# 0111111100
# 0011111000
# 0001110000
# 0000100000
# 3
# 111
# 111
# 111
# OutputCopy
# SQUARE
# TRIANGLE
# SQUARE
# TRIANGLE
# TRIANGLE
# SQUARE