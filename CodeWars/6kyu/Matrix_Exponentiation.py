# Your task in this kata is to write a function which will take a square matrix and a non-negative integer n as inputs and return a matrix raised to the power n.
#
# Be ready to handle big ns.
#
# Example:
#
# A = [[1, 2], [1, 0]]
# calc(A, 2) = [[3, 2], [1, 2]]
# External aiding modules disabled
#
# ARRAYSMATRIXALGORITHMSLOGIC
# Solution
def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result


def calc(matrix, n):
    if n == 0:
        size = len(matrix)
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    elif n == 1:
        return matrix

    half_power = calc(matrix, n // 2)

    if n % 2 == 0:
        return matrix_multiply(half_power, half_power)
    else:
        return matrix_multiply(matrix, matrix_multiply(half_power, half_power))