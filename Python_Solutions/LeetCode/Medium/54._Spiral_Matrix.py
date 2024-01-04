# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# Solution O(M * (M + N)) O(M + N)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l: list = []
        for k in range(len(matrix)):
            if matrix:
                for i in range(len(matrix[0]) - 1):
                    if matrix[0]:
                        l.append(matrix[0].pop(0))
            for i in range(len(matrix) - 1):
                if matrix[i]:
                    l.append(matrix[i].pop())
            if matrix:
                for i in range(len(matrix[-1]) - 1, 0, -1):
                    if matrix[-1]:
                        l.append(matrix[-1].pop(i))
            for i in range(len(matrix) - 1, 0, -1):
                if matrix[i]:
                    l.append(matrix[i].pop(0))
            for i in matrix:
                if not i:
                    matrix.remove(i)
        return l + matrix[0] if matrix else l