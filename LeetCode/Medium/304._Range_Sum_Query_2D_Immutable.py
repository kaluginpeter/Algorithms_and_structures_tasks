# Given a 2D matrix matrix, handle multiple queries of the following type:
#
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.
#
#
#
# Example 1:
#
#
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]
#
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -104 <= matrix[i][j] <= 104
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 104 calls will be made to sumRegion.
# Solution
# C++ O(NM) O(NM) Prefix Sum Matrix, each query will be have O(1) time complexity
class NumMatrix {
public:
    NumMatrix(vector<vector<int>>& matrix) {

        for (int row = 0; row < matrix.size(); ++row) {
            std::vector<int> currentRowPrefixSum;
            int currentRowSum = 0;
            for (int col = 0; col < matrix[row].size(); ++col) {
                currentRowSum += matrix[row][col];
                int previousRow = (row > 0 ? prefixSum[row - 1][col] : 0);
                currentRowPrefixSum.push_back(currentRowSum + previousRow);
            }
            prefixSum.push_back(currentRowPrefixSum);
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int lower_right_part = prefixSum[row2][col2];
        int lower_left_part = (col1 > 0 ? prefixSum[row2][col1 - 1] : 0);
        int upper_right_part = (row1 > 0 ? prefixSum[row1 - 1][col2] : 0);
        if (row1 > 0 && col1 > 0) { // Subtract common part
            lower_left_part -= prefixSum[row1 - 1][col1 - 1];
        }
        return lower_right_part - lower_left_part - upper_right_part;
    }
private:
    std::vector<std::vector<int>> prefixSum;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */

# Python O(NM) O(NM) Prefix Sum Matrix, each query will be have O(1) time complexity
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum: list[list[int]] = []
        for row in range(len(matrix)):
            current_row_prefix_sum: list[int] = []
            current_row_sum: int = 0
            for col in range(len(matrix[0])):
                current_row_sum += matrix[row][col]
                previous_row_prefix_sum: int = self.prefix_sum[row - 1][col] if row > 0 else 0
                current_row_prefix_sum.append(current_row_sum + previous_row_prefix_sum)
            self.prefix_sum.append(current_row_prefix_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        lower_right_part: int = self.prefix_sum[row2][col2]
        lower_left_part: int = self.prefix_sum[row2][col1 - 1] if col1 > 0 else 0
        upper_right_part: int = self.prefix_sum[row1 - 1][col2] if row1 > 0 else 0
        if row1 > 0 and col1 > 0: # Subtract common part
            lower_left_part -= self.prefix_sum[row1 - 1][col1 - 1]
        return lower_right_part - lower_left_part - upper_right_part


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)