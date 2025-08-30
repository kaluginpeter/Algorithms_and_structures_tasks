# Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.
#
# The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.
#
# For Sudoku rules, see the Wikipedia article.
#
# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]
#
# sudoku(puzzle)
# # Should return
#  [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]
# GamesGame SolversAlgorithms
# Solution
def backtrack(r: int, c: int, board: list[list[int]], row_hash: list[set[int]], col_hash: list[set[int]], square_hash: list[set[int]], n: int, m: int) -> bool:
    if r == n: return True
    n_r: int = r
    n_c: int = c + 1
    if n_c == m:
        n_c = 0
        n_r += 1
    if board[r][c]: return backtrack(n_r, n_c, board, row_hash, col_hash, square_hash, n, m)
    for k in range(1, 10):
        square: int = r // 3 * 3 + c // 3
        if k in row_hash[r] or k in col_hash[c] or k in square_hash[square]: continue
        board[r][c] = k
        row_hash[r].add(k)
        col_hash[c].add(k)
        square_hash[square].add(k)
        if backtrack(n_r, n_c, board, row_hash, col_hash, square_hash, n, m): return True
        board[r][c] = 0
        row_hash[r].remove(k)
        col_hash[c].remove(k)
        square_hash[square].remove(k)
    return False

def sudoku(board: list[list[int]]) -> list[list[int]]:
    n: int = len(board)
    m: int = len(board[0])
    row_hash: list[set[int]] = [set() for _ in range(n)]
    col_hash: list[set[int]] = [set() for _ in range(m)]
    square_hash: list[set[int]] = [set() for _ in range((n // 3 + 1) * (m // 3 + 1))]
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.': continue
            row_hash[i].add(board[i][j])
            col_hash[j].add(board[i][j])
            square_hash[i // 3 * 3 + j // 3].add(board[i][j])
    backtrack(0, 0, board, row_hash, col_hash, square_hash, n, m)
    return board