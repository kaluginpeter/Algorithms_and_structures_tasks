# A stranger has lost himself in a forest which looks like a 2D square grid.
# Night is coming, so he has to protect himself from wild animals. That is why he decided to put up a campfire.
#
# Suppose this stranger has four sticks with the same length which is equal to k.
# He can arrange them in square grid so that they form k x k square (each stick endpoint lies on a grid node). Using this strategy he can build campfire with areas 1, 4, 9, ... Also, if he rotates the sticks as it is shown in the image, he will get another campfire areas 2, 5, 10, ...
#
# (If the image does not show up, check the link)alt text
#
# Problem
# Given campfire area A (A is a natural number) is it possible to construct a
# campfire with four sticks so that their endpoints lie on grid nodes?
#
# Input
# 1
# ≤
# �
# ≤
# 1
# 0
# 9
# 1≤A≤10
# 9
#
# Output
# Return boolean (true if it is possible to construct a campfire, otherwise false):
#
# True or False in Python
# true or false in C/C++ or JavaScript
# Cases
# If A = 3, then it is impossible to construct a campfire because it
# is impossible to get the square root of 3 on the grid
# If A = 8, then it is possible to construct a campfire, for example,
# by doubling the side length of a square with area 2 in the image
# Inspiration
# This kata is inspired by the Numberphile video
#
# MATHEMATICSALGORITHMS
# Solution
from math import sqrt
def is_constructable(area):
    return any(sqrt(area - i**2).is_integer() for i in range(int(sqrt(area)) + 1))