# A. Make it White
# time limit per test2 seconds
# memory limit per test256 megabytes
# You have a horizontal strip of n
#  cells. Each cell is either white or black.
#
# You can choose a continuous segment of cells once and paint them all white. After this action, all the black cells in this segment will become white, and the white ones will remain white.
#
# What is the minimum length of the segment that needs to be painted white in order for all n
#  cells to become white?
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The descriptions of the test cases follow.
#
# The first line of each test case contains a single integer n
#  (1≤n≤10
# ) — the length of the strip.
#
# The second line of each test case contains a string s
# , consisting of n
#  characters, each of which is either 'W' or 'B'. The symbol 'W' denotes a white cell, and 'B' — a black one. It is guaranteed that at least one cell of the given strip is black.
#
# Output
# For each test case, output a single number — the minimum length of a continuous segment of cells that needs to be painted white in order for the entire strip to become white.
#
# Example
# InputCopy
# 8
# 6
# WBBWBW
# 1
# B
# 2
# WB
# 3
# BBW
# 4
# BWWB
# 6
# BWBWWB
# 6
# WWBBWB
# 9
# WBWBWWWBW
# OutputCopy
# 4
# 1
# 1
# 2
# 4
# 6
# 4
# 7
# Note
# In the first test case of the example for the strip "WBBWBW", the minimum length of the segment to be repainted white is 4
# . It is necessary to repaint to white the segment from the 2
# -nd to the 5
# -th cell (the cells are numbered from 1
#  from left to right).