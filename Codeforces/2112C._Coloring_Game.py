# C. Coloring Game
# time limit per test2.5 seconds
# memory limit per test256 megabytes
# Alice and Bob are playing a game using an integer array a
#  of size n
# .
#
# Initially, all elements of the array are colorless. First, Alice chooses 3
#  elements and colors them red. Then Bob chooses any element and colors it blue (if it was red — recolor it). Alice wins if the sum of the red elements is strictly greater than the value of the blue element.
#
# Your task is to calculate the number of ways that Alice can choose 3
#  elements in order to win regardless of Bob's actions.
#
# Input
# The first line contains a single integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (3≤n≤5000
# ).
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤a1≤a2≤⋯≤an≤105
# ).
#
# Additional constraint on the input: the sum of n
#  over all test cases doesn't exceed 5000
# .
#
# Output
# For each test case, print a single integer — the number of ways that Alice can choose 3
#  elements in order to win regardless of Bob's actions.
#
# Example
# InputCopy
# 6
# 3
# 1 2 3
# 4
# 1 1 2 4
# 5
# 7 7 7 7 7
# 5
# 1 1 2 2 4
# 6
# 2 3 3 4 5 5
# 5
# 1 1 1 1 3
# OutputCopy
# 0
# 0
# 10
# 2
# 16
# 0
# Note
# In the first two test cases, no matter which three elements Alice chooses, Bob will be able to paint one element blue so that Alice does not win.
#
# In the third test case, Alice can choose any three elements. If Bob colors one of the red elements, the sum of red elements will be 14
# , and the sum of blue elements will be 7
# . If Bob chooses an uncolored element, the sum of red elements will be 21
# , and the sum of blue elements will be 7
# .
#
# In the fourth test case, Alice can choose either the 1
# -st, 3
# -rd and 4
# -th element, or the 2
# -nd, 3
# -rd and 4
# -th element.