# Task:
# Capture pieces on a chessboard where each capture transforms the capturing piece into the captured piece.
#
# Inputs:
# (1) A two-dimensional array, representing a position on a 8 x 8 chessboard. The board will contain exactly one of each piece ('B' for bishop, 'K' for king, 'N' for knight, 'P' for pawn, 'Q' for queen, 'R' for rook). The king can be captured like any other piece.
# (2) A single letter representing the piece to start capturing with.
#
# Output:
# A list of the pieces remaining on the board after the sequence of captures terminates, sorted alphabetically.
#
# Example:
# Consider the following position, shown as an 2d-array on the right but probably clearer as displayed on the left.
#
#  ....R...                 [ ['.', '.', '.', '.', 'R', '.', '.', '.'],
#  ........                   ['.', '.', '.', '.', '.', '.', '.', '.'],
#  .K..N...                   ['.', 'K', '.', '.', 'N', '.', '.', '.'],
#  B.P.....                   ['B', '.', 'P', '.', '.', '.', '.', '.'],
#  ........                   ['.', '.', '.', '.', '.', '.', '.', '.'],
#  ........                   ['.', '.', '.', '.', '.', '.', '.', '.'],
#  ...Q....                   ['.', '.', '.', 'Q', '.', '.', '.', '.'],
#  ........                   ['.', '.', '.', '.', '.', '.', '.', '.'] ]
# Suppose the starting piece is 'Q'. The queen can capture the bishop. The inputs are generated so that it will always be the case that at each step either only one capture or no captures are possible. Capturing the bishop transforms the queen into a bishop. The bishop can then capture the king, transforming into a king. The king can then capture the pawn, transforming into a pawn. The pawn has no possible captures (pawns always move up the board). The function should return ['N', 'P', 'R'], the pieces remaining on the board in alphabetical order.
#
# Suppose the starting piece is 'R'. The rook captures the knight, which captures the pawn, which captures the king, which captures the bishop, which captures the queen, which is the only piece left on the board. The function should return ['Q'].
#
# If the starting piece was 'B', there would be two possible captures, either the king or the queen. It is guaranteed that such inputs will never occur.
#
# This kata was inspired by Transforming Chess Piece Puzzle, as well as the challenges at the website Echo Chess.
#
# For other kata related to capturing chess pieces, see Explain the Algebraic Chess Notation as well as The Capturing Rook and Losing Chess.
#
# GamesListsArrays