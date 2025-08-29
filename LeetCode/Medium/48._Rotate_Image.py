# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:
#
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
# Constraints:
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# Solution
# Python O(N^2) O(1) Matrix
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        square_size: int = len(matrix)
        start_row: int = 0
        start_col: int = 0
        while square_size > 1:
            for i in range(square_size - 1):
                ulr: int = start_row
                ulc: int = start_col + i
                urr: int = start_row + i
                urc: int = start_col + square_size - 1
                llr: int = start_row + square_size - 1 - i
                llc: int = start_col
                lrr: int = start_row + square_size - 1
                lrc: int = start_col + square_size - 1 - i
                matrix[ulr][ulc], matrix[urr][urc] = matrix[urr][urc], matrix[ulr][ulc]
                matrix[ulr][ulc], matrix[llr][llc] = matrix[llr][llc], matrix[ulr][ulc]
                matrix[llr][llc], matrix[lrr][lrc] = matrix[lrr][lrc], matrix[llr][llc]
            start_row += 1
            start_col += 1
            square_size -= 2

# C++ O(N^2) O(1) Matrix
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        size_t squareSize = matrix.size(), startRow = 0, startCol = 0;
        while (squareSize > 1) {
            for (size_t i = 0; i < squareSize - 1; ++i) {
                size_t ulr = startRow, ulc = startCol + i;
                size_t urr = startRow + i, urc = startCol + squareSize - 1;
                size_t llr = startRow + squareSize - 1 - i, llc = startCol;
                size_t lrr = startRow + squareSize - 1, lrc = startCol + squareSize - 1 - i;
                std::swap(matrix[ulr][ulc], matrix[urr][urc]);
                std::swap(matrix[ulr][ulc], matrix[llr][llc]);
                std::swap(matrix[llr][llc], matrix[lrr][lrc]);
            }
            ++startRow;
            ++startCol;
            squareSize -= 2;
        }
    }
};