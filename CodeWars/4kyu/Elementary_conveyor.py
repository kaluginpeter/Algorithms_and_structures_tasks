# The conveyor can move parts in four directions: right(r), left(l), up(u) and down(d), wrapping around the border of the grid. There is also one element that is the output of the conveyor(f).
#
# The conveyor is represented by a rectangular list of strings, as shown below:
#
# ["rdfrd",
#  "uluul"]
# During the step, the part moves along the conveyor to an adjacent cell according to the specified direction.
# For each conveyor cell, it is necessary to calculate the number of steps for which the element will reach the output tile f (-1 if this is not possible). The result is returned as a 2D array of integers.
#
# Example:
#
# ["rfl"]   =>  [[1, 0, 1]]
#
# ["rdfrd", =>  [[-1, -1, 0, -1, -1],
#  "uluul"]      [-1, -1, 1, -1, -1]]
#
# ["lfl"]   =>  [[2, 0, 1]]
# Random test parameters:
#
# 102 small tests where 5 <= width, height < 12
# 125 large tests where 200 <= width, height < 220
# PerformanceFundamentals
# Solution
def dfs(i: int, j: int, grid: list[str], output: list[list[int]]) -> None:
    moves: int = 0
    is_possible: bool = False
    callstack: list[tuple[int, int]] = [(i, j)]
    is_tail_move: bool = False
    while callstack:
        r, c = callstack.pop()
        if is_tail_move:
            output[r][c] = moves if is_possible else -1
            moves += 1
            continue
        if grid[r][c] == 'f':
            output[r][c] = moves
            moves += 1
            is_tail_move = True
            is_possible = True
            continue
        n_r: int = r + (1 if grid[r][c] == 'd' else -1 if grid[r][c] == 'u' else 0)
        n_c: int = c + (-1 if grid[r][c] == 'l' else 1 if grid[r][c] == 'r' else 0)
        if n_r == len(output):
            n_r = 0
        elif n_r == -1:
            n_r = len(output) - 1
        if n_c == len(output[0]):
            n_c = 0
        elif n_c == -1:
            n_c = len(output[0]) - 1
        if output[n_r][n_c] != -2:
            if output[n_r][n_c] >= 0:
                is_possible = True
                moves = output[n_r][n_c] + 1
            is_tail_move = True
            callstack.append((r, c))
            continue
        output[r][c] = -3
        callstack.append((r, c))
        callstack.append((n_r, n_c))


def path_counter(matrix: list[str]) -> list[list[int]]:
    n: int = len(matrix)
    m: int = len(matrix[0])
    output: list[list[int]] = [[-2] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if output[i][j] == -2: dfs(i, j, matrix, output)
    return output