# This kata is the third part of a series: Neighbourhood kata collection. You may want to do the first two before trying this version.
#
# Now we are ready for higher dimensions
# We add one dimension. You should have good spatial thinking to solve this kata.
#
# There are two popular types of cellular neighbourhoods:
#
# Moore neighborhood - cells that shape a 'square' around the given cell
# Von Neumann neighborhood - cells that shape a 'diamond' around the given cell
# Task
# Given a neighbourhood type ("moore" or "von_neumann"), a MxNxK 3D matrix (list of lists of lists), a 3-tuple of coordinates and the distance, return the list of neighbours of the given cell.
#
# Order of the indices: The first index should be applied for the outer/first matrix layer. The last index for the most inner/last layer. coordinates = (i, j, k) should be applied like mat[i][j][k]
#
# Note: you should return an empty array if any of these conditions are true:
#
# Matrix is empty
# Coordinates are outside the matrix
# Distance is equal to 0
# Example:
# I have tried my best to represent a 3D matrix.
#
# It would be very difficult to represent distances higher than 1 in the example. But you already know what to do with the distance from the previous kata.
#
# (i==0) k 0    1    2
#     j  ----------------  (i==1)
#     0  | 0  | 1  | 2  | ---------------- (i==2)
#     1  | 3  | 4  | 5  | | 9  | 10 | 11 | ----------------
#     2  | 6  | 7  | 8  | | 12 | 13 | 14 | | 18 | 19 | 20 |
#        ---------------- | 15 | 16 | 17 | | 21 | 22 | 23 |
#                         ---------------- | 24 | 25 | 26 |
#                                          ----------------
#
#
# get_neighbourhood("moore", mat, (2,2,2), 1) == [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26]
#
# get_neighbourhood("von_neumann", mat, (2,2,2), 1) == [10,12,14,16,4,22]
#
# get_neighbourhood("moore", mat, (100,100,100), 1) == []
# get_neighbourhood("moore", [[[]]], (0,0,0), 1) == []
# get_neighbourhood("moore", mat, (0,0,0), 0) == []
# Translations are appreciated ^^
#
# If you like chess take a look at Chess Aesthetics
#
# If you like puzzles take a look at Rubik's cube
#
# AlgorithmsData StructuresArraysListsMatrix
# Solution
def get_3Dneighbourhood(
    n_type: str,
    matrix: list[list[list[int]]],
    coordinates: tuple[int, int, int],
    distance: int = 1
) -> list[int]:
    if not matrix or not matrix[0] or not matrix[0][0]: return []
    if distance == 0: return []
    x, y, z = coordinates
    M, N, K = len(matrix), len(matrix[0]), len(matrix[0][0])
    if not (0 <= x < M and 0 <= y < N and 0 <= z < K): return []
    result = []
    for dx in range(-distance, distance + 1):
        for dy in range(-distance, distance + 1):
            for dz in range(-distance, distance + 1):
                if dx == 0 and dy == 0 and dz == 0: continue
                if n_type == "moore":
                    if max(abs(dx), abs(dy), abs(dz)) > distance: continue
                elif n_type == "von_neumann":
                    if abs(dx) + abs(dy) + abs(dz) > distance: continue
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < M and 0 <= ny < N and 0 <= nz < K:
                    result.append(matrix[nx][ny][nz])
    return result