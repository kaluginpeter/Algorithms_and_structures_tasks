# Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.
#
# The rules of the game are:
#
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any dead cell with exactly three live neighbours becomes a live cell.
# Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)
#
# For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively (PHP: plain black and white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:
#
# print(htmlize(cells))
# GamesArraysPuzzlesCellular Automata
# Solution
from preloaded import htmlize # this can help you debug your code
from itertools import product

def f(x):
    ni, nj = len(x), len(x[0])
    output = set()
    for i in range(ni):
        for j in range(nj):
            if x[i][j]: output.add((i, j))
    return output

def g(x):
    if not x: mi = mj = ni = nj = 0
    else:
        min_i = min(map(lambda x: x[0], x))
        min_j = min(map(lambda x: x[1], x))
        max_i = max(map(lambda x: x[0], x))
        max_j = max(map(lambda x: x[1], x))
    range_i = max_i - min_i + 1
    range_j = max_j - min_j + 1
    output = [[False for j in range(range_j)] for i in range(range_i)]
    for (i, j) in x: output[i - min_i][j - min_j] = True
    return output

def get_generation(cells, generations):
    dp = f(cells)
    for n in range(generations):
        neighs = set()
        next_dp = set()
        for (i, j) in dp:
            for (di, dj) in product((-1, 0, 1), (-1, 0, 1)):
                neighs.add((i + di, j + dj))
        for (i, j) in neighs:
            neighbours = 0
            for (di, dj) in product((-1, 0, 1), (-1, 0, 1)):
                if (i + di, j + dj) in dp and (di, dj) != (0, 0):
                    neighbours += 1
            if neighbours == 3: next_dp.add((i, j))
            elif neighbours == 2 and (i, j) in dp: next_dp.add((i, j))
        dp = next_dp
    return g(dp)