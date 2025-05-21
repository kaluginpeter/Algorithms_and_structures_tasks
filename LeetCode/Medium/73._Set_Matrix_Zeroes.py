# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
#
#
# Follow up:
#
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# Solution
# Python O(NM) O(1) Matrix
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n: int = len(matrix)
        m: int = len(matrix[0])
        is_first_row: bool = False
        is_first_col: bool = False
        for r in range(n):
            for c in range(m):
                if not matrix[r][c]:
                    if not r: is_first_row = True
                    if not c: is_first_col = True
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for r in range(1, n):
            if not matrix[r][0]:
                for c in range(m): matrix[r][c] = 0
        for c in range(1, m):
            if not matrix[0][c]:
                for r in range(n): matrix[r][c] = 0
        if is_first_row:
            for c in range(m): matrix[0][c] = 0
        if is_first_col:
            for r in range(n): matrix[r][0] = 0

# C++ O(NM) O(1) Matrix
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        bool isFirstRow = false, isFirstCol = false;
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {
                if (!matrix[r][c]) {
                    if (!r) isFirstRow = true;
                    if (!c) isFirstCol = true;
                    matrix[r][0] = 0;
                    matrix[0][c] = 0;
                }
            }
        }
        for (int r = 1; r < n; ++r) {
            if (!matrix[r][0]) {
                for (int c = 0; c < m; ++c) matrix[r][c] = 0;
            }
        }
        for (int c = 1; c < m; ++c) {
            if (!matrix[0][c]) {
                for (int r = 0; r < n; ++r) matrix[r][c] = 0;
            }
        }
        if (isFirstRow) for (int c = 0; c < m; ++c) matrix[0][c] = 0;
        if (isFirstCol) for (int r = 0; r < n; ++r) matrix[r][0] = 0;
    }
};