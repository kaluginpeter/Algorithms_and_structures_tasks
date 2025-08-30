# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.
# Example 2:
#
#
# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.
#
#
# Constraints:
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# 1 <= matrix[i][j] <= n
# Solution
# Python O(NM) O(max(N, M)) Matrix HashSet
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n: int = len(matrix)
        m: int = len(matrix[0])
        for i in range(n):
            row: set[int] = set()
            for j in range(m): row.add(matrix[i][j])
            if len(row) != n: return False
        for j in range(m):
            col: set[int] = set()
            for i in range(n): col.add(matrix[i][j])
            if len(col) != m: return False
        return True

# C++ O(NM) O(max(N, M)) Matrix HashSet
class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {
        size_t n = matrix.size(), m = matrix[0].size();
        for (size_t i = 0; i < n; ++i) {
            std::unordered_set<int> row;
            for (size_t j = 0; j < m; ++j) row.insert(matrix[i][j]);
            if (row.size() != n) return false;
        }
        for (size_t j = 0; j < m; ++j) {
            std::unordered_set<int> col;
            for (size_t i = 0; i < n; ++i) col.insert(matrix[i][j]);
            if (col.size() != m) return false;
        }
        return true;
    }
};