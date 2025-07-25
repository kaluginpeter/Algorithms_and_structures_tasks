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
# Solution
def squares_covered(pos: str, piece: str) -> list[list[int]]:
    board = [[0 for _ in range(8)] for _ in range(8)]

    col_char = pos[0]
    row_char = pos[1]
    col = ord(col_char) - ord('a')
    row = 8 - int(row_char)
    board[row][col] = -1
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    king_moves = rook_dirs + bishop_dirs
    if piece in ('R', 'Q'):
        for dr, dc in rook_dirs:
            nr, nc = row + dr, col + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                board[nr][nc] = 1
                nr += dr
                nc += dc
    if piece in ('B', 'Q'):
        for dr, dc in bishop_dirs:
            nr, nc = row + dr, col + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                board[nr][nc] = 1
                nr += dr
                nc += dc
    if piece == 'N':
        for dr, dc in knight_moves:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                board[nr][nc] = 1
    if piece == 'K':
        for dr, dc in king_moves:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                board[nr][nc] = 1

    return board