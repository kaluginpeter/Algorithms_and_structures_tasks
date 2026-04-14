# This kata is the third part of a series: Neighbourhood kata collection. You may want to do the first two before trying this version.
#
# Now we are ready for higher dimensions
# We add one dimension. You should have good spatial thinking to solve this kata.
#
# There are two popular types of cellular neighbourhoods:
#
# Moore neighborhood - cells that shape a 'square' around the given cell
# Von Neumann neighborhood - cells that shape a 'diamond' around the given cell
# Task
# Given a neighbourhood type ("moore" or "von_neumann"), a MxNxK 3D matrix (list of lists of lists), a 3-tuple of coordinates and the distance, return the list of neighbours of the given cell.
#
# Order of the indices: The first index should be applied for the outer/first matrix layer. The last index for the most inner/last layer. coordinates = (i, j, k) should be applied like mat[i][j][k]
#
# Note: you should return an empty array if any of these conditions are true:
#
# Matrix is empty
# Coordinates are outside the matrix
# Distance is equal to 0
# Example:
# I have tried my best to represent a 3D matrix.
#
# It would be very difficult to represent distances higher than 1 in the example. But you already know what to do with the distance from the previous kata.
#
# (i==0) k 0    1    2
#     j  ----------------  (i==1)
#     0  | 0  | 1  | 2  | ---------------- (i==2)
#     1  | 3  | 4  | 5  | | 9  | 10 | 11 | ----------------
#     2  | 6  | 7  | 8  | | 12 | 13 | 14 | | 18 | 19 | 20 |
#        ---------------- | 15 | 16 | 17 | | 21 | 22 | 23 |
#                         ---------------- | 24 | 25 | 26 |
#                                          ----------------
#
#
# get_neighbourhood("moore", mat, (2,2,2), 1) == [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26]
#
# get_neighbourhood("von_neumann", mat, (2,2,2), 1) == [10,12,14,16,4,22]
#
# get_neighbourhood("moore", mat, (100,100,100), 1) == []
# get_neighbourhood("moore", [[[]]], (0,0,0), 1) == []
# get_neighbourhood("moore", mat, (0,0,0), 0) == []
# Translations are appreciated ^^
#
# If you like chess take a look at Chess Aesthetics
#
# If you like puzzles take a look at Rubik's cube
#
# AlgorithmsData StructuresArraysListsMatrix