# In this kata, you will be given a grid and a point, and you will want to return the numbers in the row, column and both the diagonals that point is on, like a queen's move in chess.
#
# For example, given the grid:
#
# [[ 1,  2,  3,  4,  5],
#  [ 6,  7,  8,  9,  0],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25]]
# The origin starts at the top left square. The points are 0-indexed so the first point is [0, 0] which would be the top left point. In the case of the grid above, it would be 1
#
# If given the point [2, 3], you should return the numbers on the row, column and both the diagonals containing that point.
#
# The [2, 3] point contains the number 18
#
# The row containing the [2, 3] point contains the numbers [16, 17, 18, 19, 20]
#
# The column containing the [2, 3] point contains the numbers [3, 8, 13, 18, 23]
#
# The top-left to bottom-right diagonal containing the [2, 3] point contains the numbers [6, 12, 18, 24]
#
# The top-right to bottom-left diagonal containing the [2, 3] point contains the numbers [0, 14, 18, 22]
#
# And you should return them in the order: [row, column, top-left to bottom-right diag, top-right to bottom-left diag]
#
# Therefore, in this case, you should return [[16, 17, 18, 19, 20], [3, 8, 13, 18, 23], [6, 12, 18, 24], [0, 14, 18, 22]] as a list of the lines.
#
# The order inside each row, column or diagonal doesnt matter, but you do have to return the lines in the same order as the one stated above.
#
# You will be given the grid as a list, the position of the point as a list, and the size of the grid as an int:
#
# def check_grid(grid, pos, size):
# The grids will always be square
# The sizes of the grids tested will be 2 <= size <= 100. There will be no grids smaller than 2.
# Good luck!
#
# AlgorithmsArraysListsLogic