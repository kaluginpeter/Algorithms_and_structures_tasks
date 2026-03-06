# If you haven't already done so, you should do the 5x5 and 15x15 Nonogram solvers first.
#
# In this kata, you have to solve nonograms from any size up to one with an average side length of 50. The nonograms are not all square. However, they all will be valid and should only have one solution.
#
# I highly recommend not to try and use a brute force solution as some of the grids are very big. Also, you may not be able to solve all the grids by deduction alone so may have to guess one or two squares. :P
#
# You will be given three arguments: The clues, the width, and the height:
#
# # clues is given in the same format as the previous two nonogram katas:
# clues = (tuple((column_clues,) for column_clues in column),
#          tuple((row_clues,) for row_clues in row))
#
# # width is the width of the puzzle (distance from left to right)
# width = width_of_puzzle
#
# # height is the height of the puzzle (distance from top to bottom)
# height = height_of_puzzle
# and you will have to finish the function:
#
# def solve(clues, width, height):
#     pass
# You should return an array of arrays (or equivalent for your language) of the solved grid, see the tests for details.
#
# For example, the second example test case looks like:
#
# Img
#
# Therefore, you would be given the arguments:
#
# clues = (((3,), (4,), (2, 2, 2), (2, 4, 2), (6,), (3,)),
#          ((4,), (6,), (2, 2), (2, 2), (2,), (2,), (2,), (2,), (), (2,), (2,)))
# width = 6
# height = 11
# Zero will be given as an array (or equivalent).
#
# Test sizes:
# You will be given 60 random tests in total. There will be:
#
# 35 small tests: 3 < the average of the side lengths <= 25
# 15 medium tests: 25 < the average of the side lengths <= 35
# 10 big tests: 40 <= the average of the side lengths <= 50
# Good luck :)
#
# AlgorithmsLogicGamesGame Solvers
# Solution
def dp(n, k, black, ll, gl, groups, whites, blacks,
       blacks_filled, prefix_whites, memo_table):
    if (n, k, black) not in memo_table:
        if n > ll:
            return False
        if n == ll:
            return k == gl

        res = False

        if blacks_filled[n]:
            if dp(n + 1, k, False, ll, gl, groups, whites, blacks,
                  blacks_filled, prefix_whites, memo_table):
                whites[n] = True
                res = True

        if k < gl and not black:
            n_ = n + groups[k]
            if n_ <= ll and prefix_whites[n_] - prefix_whites[n] == 0:
                if dp(n_, k + 1, True, ll, gl, groups, whites, blacks,
                      blacks_filled, prefix_whites, memo_table):
                    for i in range(n, n_):
                        blacks[i] = True
                    res = True

        memo_table[(n, k, black)] = res

    return memo_table[(n, k, black)]


def solve_lines(board, clues, changed_rows, changed_columns, solved_cells, rotate=False):
    for index in changed_rows:
        line = ''.join([board[i][index] for i in range(len(board))]) if rotate else ''.join(board[index])
        delta = solve_line(line, clues[index], changed_columns, board, index, rotate)
        if delta is None:
            return None
        solved_cells += delta
    return solved_cells

def solve_line(line, groups, changed_columns, board, j, rotate=False):
    length, group_count = len(line), len(groups)
    whites = [False] * (length + 1)
    blacks = [False] * (length + 1)
    blacks_filled = [ch != 'X' for ch in line]
    prefix_whites = [0] * (length + 1)

    for i in range(length):
        prefix_whites[i + 1] = prefix_whites[i] + (line[i] == '.')

    memo = {}
    dp(0, 0, False, length, group_count, groups, whites, blacks, blacks_filled, prefix_whites, memo)

    solved_cells = 0
    for i in range(length):
        row, col = (i, j) if rotate else (j, i)
        if whites[i] and blacks[i]:
            board[row][col] = '?'
        elif whites[i]:
            if line[i] == '?':
                solved_cells += 1
                changed_columns.add(i)
            board[row][col] = '.'
        elif blacks[i]:
            if line[i] == '?':
                solved_cells += 1
                changed_columns.add(i)
            board[row][col] = 'X'
        else:
            return None
    return solved_cells

def solve(clues: tuple, width, height):
    column_clues, row_clues = clues
    board = [['?' for _ in range(width)] for _ in range(height)]
    total_cells = height * width

    solved_cells, iteration = cycle(board, row_clues, column_clues, height, width, total_cells)
    total_solved = solved_cells
    total_iterations = iteration

    unsolved = [(r, c) for r in range(height) for c in range(width) if board[r][c] == '?']
    unsolved.sort(key=lambda x: min(
        sum(row_clues[x[0]]) - sum(1 for ch in board[x[0]] if ch == 'X'),
        sum(column_clues[x[1]]) - sum(1 for r in range(height) if board[r][x[1]] == 'X')
    ))

    for r, c in unsolved:
        snapshot = [row.copy() for row in board]
        board[r][c] = 'X'
        result = cycle(board, row_clues, column_clues, height, width, total_cells)

        if result is None:
            board = [row.copy() for row in snapshot]
            board[r][c] = '.'
            total_solved += 1
        else:
            solved_cells, iteration = result
            total_iterations += iteration
            if total_solved + solved_cells + 1 == total_cells:
                break
            board = [row.copy() for row in snapshot]

    matrix = tuple(tuple(row) for row in board)
    output = []
    for row in matrix:
        tmp = [1 if i == 'X' else 0 for i in row]
        output.append(tuple(tmp))
    return tuple(output)

def cycle(board, row_clues, column_clues, height, width, total_cells):
    prev_count = -1
    iteration = 0
    solved_cells = 0
    rows_to_update, cols_to_update = [set(range(height)), set(range(width))]

    while prev_count < solved_cells < total_cells:
        updated_rows = set()
        prev_count = solved_cells
        iteration += 1

        solved_cells = solve_lines(board, row_clues, rows_to_update, cols_to_update, solved_cells)
        if solved_cells is None:
            return None

        solved_cells = solve_lines(board, column_clues, cols_to_update, updated_rows, solved_cells, rotate=True)
        if solved_cells is None:
            return None

        rows_to_update, cols_to_update = updated_rows, set()

    return solved_cells, iteration