# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.
#
# The following proccess happens k times:
#
# Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
#
#
# Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
#
#
# Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.
#
#
#
# Example 1:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4
#
# Output: false
#
# Explanation:
#
# In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).
#
#
#
# Example 2:
#
# Input: mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2
#
# Output: true
#
# Explanation:
#
#
#
# Example 3:
#
# Input: mat = [[2,2],[2,2]], k = 3
#
# Output: true
#
# Explanation:
#
# As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.
#
#
#
# Constraints:
#
# 1 <= mat.length <= 25
# 1 <= mat[i].length <= 25
# 1 <= mat[i][j] <= 25
# 1 <= k <= 50
# Solution
# Python O(NM) O(1) Matrix Greedy
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n: int = len(mat)
        m: int = len(mat[0])
        k %= m
        return all(mat[i][j] == mat[i][(j + k) % m] for j in range(m) for i in range(n))

# C++ O(NM) O(1) Greedy Matrix
class Solution {
public:
    bool areSimilar(vector<vector<int>>& mat, int k) {
        size_t n = mat.size(), m = mat[0].size();
        k %= m;
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                if (mat[i][j] != mat[i][(j + k) % m]) return 0;
            }
        }
        return 1;
    }
};