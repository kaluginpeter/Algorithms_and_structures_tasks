# Task
# You are given a chessboard with several rooks and bishops placed on some of its squares. How many unoccupied squares are there that are not under attack of any chess piece?
#
# Here, the standard rules are applied: a square is under attack of a rook or a bishop only if all squares between the piece and the current square are unoccupied.
#
# Input/Output
# [input] integer array chessboard
# matrix of size 8x8 containing numbers {-1, 0, 1} which represents chess pieces placement:
#
# -1 -> bishop, 0 -> empty square, 1 -> rook
#
# [output] an integer
# number of safe squares on the board.
#
# Puzzles