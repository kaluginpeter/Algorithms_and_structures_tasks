# B. Scale
# time limit per test2 seconds
# memory limit per test256 megabytes
# Tina has a square grid with n
#  rows and n
#  columns. Each cell in the grid is either 0
#  or 1
# .
#
# Tina wants to reduce the grid by a factor of k
#  (k
#  is a divisor of n
# ). To do this, Tina splits the grid into k×k
#  nonoverlapping blocks of cells such that every cell belongs to exactly one block.
#
# Tina then replaces each block of cells with a single cell equal to the value of the cells in the block. It is guaranteed that every cell in the same block has the same value.
#
# For example, the following demonstration shows a grid being reduced by factor of 3
# .
#
# Original grid
# 0
# 0
# 0
# 1
# 1
# 1
# 0
# 0
# 0
# 1
# 1
# 1
# 0
# 0
# 0
# 1
# 1
# 1
# 1
# 1
# 1
# 0
# 0
# 0
# 1
# 1
# 1
# 0
# 0
# 0
# 1
# 1
# 1
# 0
# 0
# 0
# Reduced grid
# 0
# 1
# 1
# 0
# Help Tina reduce the grid by a factor of k
# .
#
# Input
# The first line contains t
#  (1≤t≤100
# ) – the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤n≤1000
# , 1≤k≤n
# , k
#  is a divisor of n
# ) — the number of rows and columns of the grid, and the factor that Tina wants to reduce the grid by.
#
# Each of the following n
#  lines contain n
#  characters describing the cells of the grid. Each character is either 0
#  or 1
# . It is guaranteed every k
#  by k
#  block has the same value.
#
# It is guaranteed the sum of n
#  over all test cases does not exceed 1000
# .
#
# Output
# For each test case, output the grid reduced by a factor of k
#  on a new line.
#
# Example
# InputCopy
# 4
# 4 4
# 0000
# 0000
# 0000
# 0000
# 6 3
# 000111
# 000111
# 000111
# 111000
# 111000
# 111000
# 6 2
# 001100
# 001100
# 111111
# 111111
# 110000
# 110000
# 8 1
# 11111111
# 11111111
# 11111111
# 11111111
# 11111111
# 11111111
# 11111111
# 11111111
# OutputCopy
# 0
# 01
# 10
# 010
# 111
# 100
# 11111111
# 11111111
# 11111111
# 11111111
# 11111111
# 11111111
# 11111111
# 11111111