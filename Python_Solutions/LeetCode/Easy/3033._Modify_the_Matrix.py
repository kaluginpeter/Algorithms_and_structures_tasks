# Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to matrix, then replace each element with the value -1 with the maximum element in its respective column.
#
# Return the matrix answer.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
# Output: [[1,2,9],[4,8,6],[7,8,9]]
# Explanation: The diagram above shows the elements that are changed (in blue).
# - We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
# - We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.
# Example 2:
#
#
# Input: matrix = [[3,-1],[5,2]]
# Output: [[3,2],[5,2]]
# Explanation: The diagram above shows the elements that are changed (in blue).
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 2 <= m, n <= 50
# -1 <= matrix[i][j] <= 100
# The input is generated such that each column contains at least one non-negative integer.
# Solution Initial O(N**3) O(NM)
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ans: list = []
        for i in range(len(matrix)):
            top: list = []
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    el: int = -1
                    for n in range(len(matrix)):
                        el = max(el, matrix[n][j])
                    top.append(el)
                else:
                    top.append(matrix[i][j])
            ans.append(top)
        return ans
# Solution O(NM) (1)
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for columns in range(len(matrix[0])):
            mx: int = -1
            for rows in range(len(matrix)):
                mx = max(mx, matrix[rows][columns])
            for rows in range(len(matrix)):
                if matrix[rows][columns] == -1:
                    matrix[rows][columns] = mx
        return matrix