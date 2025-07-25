# You will be making a program that shows all positions a chess piece can go to. The function has 2 parameters: the position on the chess board in the format a1 and a letter representing the piece. This will be K, Q, R, B, N for respectively the King, Queen, Rook, Bishop and Knight
#
# This is what the matrix looks like for a queen in d3:
#
# [[0,  0,  0,  1,  0,  0,  0,  0],
#  [0,  0,  0,  1,  0,  0,  0,  1],
#  [1,  0,  0,  1,  0,  0,  1,  0],
#  [0,  1,  0,  1,  0,  1,  0,  0],
#  [0,  0,  1,  1,  1,  0,  0,  0],
#  [1,  1,  1, -1,  1,  1,  1,  1],
#  [0,  0,  1,  1,  1,  0,  0,  0],
#  [0,  1,  0,  1,  0,  1,  0,  0]]
# Take a look at the test cases for some more examples.
#
# See https://en.wikipedia.org/wiki/Chess#Movement for the movement rules of the pieces.
#
# Good luck :P
#
# AlgorithmsMatrix