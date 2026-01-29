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
# Solution
from typing import List


def capture_pieces(board: List[List[str]], piece: str) -> List[str]:
    rook_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    bishop_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
    knight_moves = [
        (2,1),(2,-1),(-2,1),(-2,-1),
        (1,2),(1,-2),(-1,2),(-1,-2)
    ]
    def inside(r, c):
        return 0 <= r < 8 and 0 <= c < 8

    for i in range(8):
        for j in range(8):
            if board[i][j] == piece:
                r, c = i, j
                break

    while True:
        capture = None
        def try_capture(nr, nc):
            nonlocal capture
            if inside(nr, nc) and board[nr][nc] != '.': capture = (nr, nc)
        if piece == 'P':
            for dc in (-1, 1):
                try_capture(r - 1, c + dc)

        elif piece == 'N':
            for dr, dc in knight_moves:
                try_capture(r + dr, c + dc)
        elif piece == 'K':
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    if dr or dc: try_capture(r + dr, c + dc)
        else:
            dirs = []
            if piece in ('R', 'Q'): dirs += rook_dirs
            if piece in ('B', 'Q'): dirs += bishop_dirs
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while inside(nr, nc):
                    if board[nr][nc] != '.':
                        capture = (nr, nc)
                        break
                    nr += dr
                    nc += dc
                if capture: break
        if not capture: break
        nr, nc = capture
        new_piece = board[nr][nc]
        board[r][c] = '.'
        board[nr][nc] = new_piece
        r, c = nr, nc
        piece = new_piece
    remaining = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != '.': remaining.append(board[i][j])
    return sorted(remaining)