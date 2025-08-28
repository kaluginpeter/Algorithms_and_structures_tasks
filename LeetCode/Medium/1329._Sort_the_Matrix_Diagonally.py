# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
#
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
#
#
#
# Example 1:
#
#
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# Example 2:
#
# Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100
# Solution
# Python O((N + M)log(min(N, M))) O(min(N, M)) Matrix
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n: int = len(mat)
        m: int = len(mat[0])
        i: int = n - 1
        j: int = 0
        while j < m:
            nums: list[int] = []
            pos: int = 0
            while i + pos < n and j + pos < m:
                nums.append(mat[i + pos][j + pos])
                pos += 1
            nums.sort()
            pos = 0
            while i + pos < n and j + pos < m:
                mat[i + pos][j + pos] = nums[pos]
                pos += 1
            if i: i -= 1
            else: j += 1
        return mat

# C++ O((N + M)log(min(N, M))) O(min(N, M)) Matrix
class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        size_t n = mat.size(), m = mat[0].size(), i = n - 1, j = 0;
        while (j < m) {
            std::vector<int> nums;
            size_t pos = 0;
            while (i + pos < n && j + pos < m) {
                nums.emplace_back(mat[i + pos][j + pos]);
                ++pos;
            }
            std::sort(nums.begin(), nums.end());
            pos = 0;
            while (i + pos < n && j + pos < m) {
                mat[i + pos][j + pos] = nums[pos];
                ++pos;
            }
            if (i) --i;
            else ++j;
        }
        return mat;
    }
};