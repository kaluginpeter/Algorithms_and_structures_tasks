# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
#
#
#
# Example 1:
#
#
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:
#
#
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
#
#
# Constraints:
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
# Solution Dynamic Programming O(NM) O(1)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] += min(
                    matrix[max(0, row - 1)][max(0, col - 1)],
                    matrix[max(0, row - 1)][col],
                    matrix[max(0, row - 1)][min(len(matrix[row]) - 1, col + 1)]
                )
        return min(matrix[-1])