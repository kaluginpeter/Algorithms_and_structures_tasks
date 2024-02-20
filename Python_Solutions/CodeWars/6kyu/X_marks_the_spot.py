# Write a function x(n) that takes in a number n and returns an nxn array with an X in the middle. The X will be represented by 1's and the rest will be 0's.
# E.g.
#
# x(5) ==  [[1, 0, 0, 0, 1],
#           [0, 1, 0, 1, 0],
#           [0, 0, 1, 0, 0],
#           [0, 1, 0, 1, 0],
#           [1, 0, 0, 0, 1]];
#
# x(6) ==  [[1, 0, 0, 0, 0, 1],
#           [0, 1, 0, 0, 1, 0],
#           [0, 0, 1, 1, 0, 0],
#           [0, 0, 1, 1, 0, 0],
#           [0, 1, 0, 0, 1, 0],
#           [1, 0, 0, 0, 0, 1]];
# ARRAYSALGORITHMS
# Solution O(NM) O(NM)
def x(n):
    mtrx: list = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        mtrx[i][i], mtrx[i][-i-1] = 1, 1
    return mtrx