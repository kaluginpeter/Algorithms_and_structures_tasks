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
# Solution
def bishops_and_rooks(M):
    n, m = len(M), len(M[0])
    for i in range(n):
        for j in range(m):
            if M[i][j] == -1:
                x, y = i - 1, j - 1
                while x >= 0 and y >= 0:
                    if M[x][y] not in {0, 2}: break
                    M[x][y] = 2
                    x, y = x - 1, y - 1
                x, y = i - 1, j + 1
                while x >= 0 and y < m:
                    if M[x][y] not in {0, 2}: break
                    M[x][y] = 2
                    x, y = x - 1, y + 1
                x, y = i + 1, j - 1
                while x < n and y >= 0:
                    if M[x][y] not in {0, 2}: break
                    M[x][y] = 2
                    x, y = x + 1, y - 1
                x, y = i + 1, j + 1
                while x < n and y < m:
                    if M[x][y] not in {0, 2}: break
                    M[x][y] = 2
                    x, y = x + 1, y + 1
            elif M[i][j] == 1:
                x = i - 1
                while x >= 0:
                    if M[x][j] not in {0, 2}: break
                    M[x][j] = 2
                    x -= 1
                x = i + 1
                while x < n:
                    if M[x][j] not in {0, 2}: break
                    M[x][j] = 2
                    x += 1
                y = j - 1
                while y >= 0:
                    if M[i][y] not in {0, 2}: break
                    M[i][y] = 2
                    y -= 1
                y = j + 1
                while y < m:
                    if M[i][y] not in {0, 2}: break
                    M[i][y] = 2
                    y += 1
    return sum(sum(not cell for cell in row) for row in M)