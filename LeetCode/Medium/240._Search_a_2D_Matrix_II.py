# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
#
# Example 1:
#
#
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:
#
#
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109
# Solution 1 O(m * n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == target:
                    return True
        return False
# Solution 2 O(m * logn)
class Solution(object):
    def searchMatrix(self, matrix, target):
        for m in range(len(matrix)):
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                middle = (left + right) // 2
                if matrix[m][middle] == target:
                    return True
                elif matrix[m][middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
        return False
# Solution 3 O(m + n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False