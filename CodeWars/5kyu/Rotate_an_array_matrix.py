# Write a function that rotates a two-dimensional array (a matrix) either clockwise or anti-clockwise by 90 degrees, and returns the rotated array.
#
# The function accepts two parameters: a matrix, and a string specifying the direction or rotation. The direction will be either "clockwise" or "counter-clockwise".
#
# Examples
# For matrix:
#
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Clockwise rotation:
#
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]
# Counter-clockwise rotation:
#
# [
#   [3, 6, 9],
#   [2, 5, 8],
#   [1, 4, 7]
# ]
# MATRIXARRAYSALGORITHMS
# Solution
def rotate(matrix, direction):
    mtrx: list = []
    if direction == 'clockwise':
        for column in range(len(matrix[0])):
            top: list = []
            for row in range(len(matrix) - 1, -1, -1):
                top.append(matrix[row][column])
            mtrx.append(top)
        return mtrx
    else:
        for column in range(len(matrix[0]) - 1, -1, -1):
            top: list = []
            for row in range(len(matrix)):
                top.append(matrix[row][column])
            mtrx.append(top)
        return mtrx