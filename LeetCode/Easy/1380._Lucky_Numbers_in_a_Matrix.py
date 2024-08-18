# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
#
#
#
# Example 1:
#
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 2:
#
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:
#
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 105.
# All elements in the matrix are distinct.
# Solution
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix[0])):
            top, cop = 0, 0
            for j in range(len(matrix)):
                if matrix[j][i] > cop:
                    cop = matrix[j][i]
                    if matrix[j][i] == min(matrix[j]):
                        top = matrix[j][i]
                    else:
                        top = 0
            if top > 0:
                ans.append(top)
        return ans

# Solution HashSet O(NM) O(N + M)
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_a_row: set[int] = set(min(row) for row in matrix)
        max_in_a_col: set[int] = set(max(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0])))
        return [luck_num for luck_num in min_in_a_row if luck_num in max_in_a_col]