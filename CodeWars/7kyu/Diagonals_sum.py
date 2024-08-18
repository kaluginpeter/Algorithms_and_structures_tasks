# Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary)
#
# Matrix = array of n length whose elements are n length arrays of integers.
#
# 3x3 example:
#
# sum_diagonals( [
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
# ] ) == 30 # 1 + 5 + 9 + 3 + 5 + 7
# MATRIXALGORITHMS
# Solution
def sum_diagonals(matrix):
    if not matrix[0]:
        return 0
    total, step = 0, 0
    for i in matrix:
        total += i[step] + i[-step + -1]
        step += 1
    return total