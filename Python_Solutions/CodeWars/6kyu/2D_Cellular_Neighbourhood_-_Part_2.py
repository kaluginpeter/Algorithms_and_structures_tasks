# This kata is the second part of a series: Neighbourhood kata collection. You may want to do the first one before trying this version.
#
# Now we will implement the distance
# The distance extends the reach of the neighbourhood - instead of returning only the closest neighbours, you'll be searching for all neighbours in a given maximum distance.
#
# There are two popular types of cellular neighbourhoods:
#
# Moore neighborhood - the eight cells that surround the given cell
# Von Neumann neighborhood - the four cells that share a border with the given cell
# Task
# Given a neighbourhood type ("moore" or "von_neumann"), a 2D matrix (a list of lists), a pair of coordinates and the distance, return the list of neighbours of the given cell.
#
# Order of the indices: The first index should be applied for the outer/first matrix layer. The last index for the most inner/last layer. coordinates = (m, n) should be applied like mat[m][n]
#
# Note: you should return an empty array if any of these conditions are true:
#
# Matrix is empty
# Coordinates are outside the matrix
# Distance is equal to 0
# Example:
# \ n  0    1    2    3    4
# m  --------------------------
# 0  | 0  | 1  | 2  | 3  | 4  |
# 1  | 5  | 6  | 7  | 8  | 9  |
# 2  | 10 | 11 | 12 | 13 | 14 |
# 3  | 15 | 16 | 17 | 18 | 19 |
# 4  | 20 | 21 | 22 | 23 | 24 |
#    --------------------------
#
# get_neighborhood("moore", arr, (2,2), 1) == [6,7,8,11,13,16,17,18]
# get_neighborhood("moore", arr, (2,2), 2) == [0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24]
#
# get_neighborhood("von_neumann", arr, (2,2), 1) == [7,11,13,17]
# get_neighborhood("von_neumann", arr, (2,2), 2) == [2,6,7,8,10,11,13,14,16,17,18,22]
# Translations are appreciated ^^
#
# If you like chess take a look at Chess Aesthetics
#
# If you like puzzles take a look at Rubik's cube
#
# ALGORITHMSDATA STRUCTURESARRAYSMATRIX
# Solution
def get_neighbourhood(n_type, mat, cor, distance=1):
    if not mat: return []
    if (cor[0] >= len(mat) or cor[0] < 0) or (cor[1] >= len(mat[0]) or cor[1] < 0):
        return []

    ans: set[tuple[int, int]] = set()
    if n_type == 'moore':
        for rows in range(max(0, cor[0] - distance), min(len(mat), cor[0] + distance + 1)):
            for cols in range(max(0, cor[1] - distance), min(len(mat[0]), cor[1] + distance + 1)):
                if (rows, cols) == cor: continue
                if 0 <= rows < len(mat) and 0 <= cols < len(mat[0]):
                    ans.add((rows, cols))
        return [mat[x][y] for x, y in ans]

    idx: int = 1
    for rows in range(cor[0] - 1, max(0, cor[0] - distance) - 1, -1):
        for cols in range(max(0, (cor[1] - distance) + idx), min(len(mat[0]), (cor[1] + distance) - idx + 1)):
            if (rows, cols) == cor: continue
            if 0 <= rows < len(mat) and 0 <= cols < len(mat[0]):
                ans.add((rows, cols))
        idx += 1

    idx: int = -1
    for rows in range(cor[0], min(len(mat), cor[0] + distance + 1)):
        if rows >= cor[0]:
            idx += 1
        for cols in range(max(0, (cor[1] - distance) + idx), min(len(mat[0]), (cor[1] + distance) - idx + 1)):
            if (rows, cols) == cor: continue
            if 0 <= rows < len(mat) and 0 <= cols < len(mat[0]):
                ans.add((rows, cols))
    return [mat[x][y] for x, y in ans]