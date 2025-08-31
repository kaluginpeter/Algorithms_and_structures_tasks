# In chess, the queen can be moved across any number of unoccupied squares in a straight line vertically, horizontally, or diagonally, thus combining the moves of the rook and bishop.
#
# Task
# Given the square of a queen on a chessboard, your function must output an array of the squares the queen can move to. Squares are represented as strings using chess algebraic notation.
#
# Input
# A valid input position is a string of one letter from A to H followed by a digit from 1 to 8, for example "A1", "C8", "B3".
# If the input is anything else (e.g. not a string, or an invalid position such as A10 or H0), return an empty array.
# Output
# An array of positions (strings). It should be sorted in lexicographical order and should not include the starting square of the queen.
#
# Example
# For example when input position is A1 return value should be:
#
# ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "C1", "C3", "D1", "D4", "E1", "E5", "F1", "F6", "G1", "G7", "H1", "H8"]
#      A   B   C   D   E   F   G   H
#    + - + - + - + - + - + - + - + - +
# 1  | Q | x | x | x | x | x | x | x |
#    + - + - + - + - + - + - + - + - +
# 2  | x | x |   |   |   |   |   |   |
#    + - + - + - + - + - + - + - + - +
# 3  | x |   | x |   |   |   |   |   |
#    + - + - + - + - + - + - + - + - +
# 4  | x |   |   | x |   |   |   |   |
#    + - + - + - + - + - + - + - + - +
# 5  | x |   |   |   | x |   |   |   |
#    + - + - + - + - + - + - + - + - +
# 6  | x |   |   |   |   | x |   |   |
#    + - + - + - + - + - + - + - + - +
# 7  | x |   |   |   |   |   | x |   |
#    + - + - + - + - + - + - + - + - +
# 8  | x |   |   |   |   |   |   | x |
#    + - + - + - + - + - + - + - + - +
#
# Q = queen
# x = available move
# ArraysFundamentals