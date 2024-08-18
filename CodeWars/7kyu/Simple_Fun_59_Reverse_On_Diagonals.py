# Task
# Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.
#
# The longest diagonals of a square matrix are defined as follows:
#
# the first longest diagonal goes from the top left corner to the bottom right one;
# the second longest diagonal goes from the top right corner to the bottom left one.
# Example
# For the matrix
#
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# the output should be:
#
# 9, 2, 7
# 4, 5, 6
# 3, 8, 1
# Input/Output
# [input] 2D integer array matrix
#
# Constraints: 1 ≤ matrix.length ≤ 10, matrix.length = matrix[i].length, 1 ≤ matrix[i][j] ≤ 1000
#
# [output] 2D integer array
#
# Matrix with the order of elements on its longest diagonals reversed.
#
# PUZZLES
# Solution
def reverse_on_diagonals(matrix):
    idx: int = 0
    middle: int = len(matrix) // 2
    for row in range(len(matrix)):
        if idx == middle: break
        matrix[idx][idx], matrix[-idx - 1][-idx - 1] = matrix[-idx - 1][-idx - 1], matrix[idx][idx]
        idx += 1
    idx = 0
    for row in range(len(matrix)):
        if idx == middle: break
        matrix[idx][-idx - 1], matrix[-idx - 1][idx] = matrix[-idx - 1][idx], matrix[idx][-idx - 1]
        idx += 1
    return matrix