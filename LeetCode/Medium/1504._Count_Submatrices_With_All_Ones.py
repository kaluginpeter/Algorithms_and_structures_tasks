# Given an m x n binary matrix mat, return the number of submatrices that have all ones.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2.
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# Example 2:
#
#
# Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# Output: 24
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3.
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2.
# There are 2 rectangles of side 3x1.
# There is 1 rectangle of side 3x2.
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
#
#
# Constraints:
#
# 1 <= m, n <= 150
# mat[i][j] is either 0 or 1.
# Python O(N(M^2)) O(M) DynamicProgramming Matrix
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n: int = len(mat)
        m: int = len(mat[0])
        height: list[int] = [0] * m
        output: int = 0
        for i in range(n):
            for j in range(m): height[j] = height[j] + 1 if mat[i][j] else 0
            for j in range(m):
                mn: int = height[j]
                for k in range(j, -1, -1):
                    mn = min(mn, height[k])
                    output += mn
                    if not mn: break
        return output

# C++ O(N(M^2)) O(M) DynamicProgramming Matrix
class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size(), output = 0;
        std::vector<int> height(m, 0);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) height[j] = (mat[i][j] ? height[j] + 1 : 0);
            for(int j = 0; j < m; ++j) {
                int mn = height[j];
                for(int k = j; k >= 0 && mn > 0; --k) {
                    mn = std::min(mn, height[k]);
                    output += mn;
                }
            }
        }
        return output;
    }
};