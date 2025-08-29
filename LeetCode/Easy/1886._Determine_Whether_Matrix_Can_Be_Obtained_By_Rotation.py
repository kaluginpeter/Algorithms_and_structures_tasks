# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
#
#
#
# Example 1:
#
#
# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
# Example 2:
#
#
# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.
# Example 3:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
#
#
# Constraints:
#
# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 <= n <= 10
# mat[i][j] and target[i][j] are either 0 or 1.
#
# Solution
# Python O(NM) O(1) Matrix
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

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target: return True
            self.rotate(mat)
        return False

# C++ O(NM) O(1) Matrix
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

    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        for (int i = 0; i < 4; ++i) {
            if (mat == target) return true;
            rotate(mat);
        }
        return false;
    }
};