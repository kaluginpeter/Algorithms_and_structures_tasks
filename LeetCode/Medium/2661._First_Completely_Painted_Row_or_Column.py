# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
#
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
#
# Return the smallest index i at which either a row or a column will be completely painted in mat.
#
#
#
# Example 1:
#
# image explanation for example 1
# Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
# Output: 2
# Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
# Example 2:
#
# image explanation for example 2
# Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
# Output: 3
# Explanation: The second column becomes fully painted at arr[3].
#
#
# Constraints:
#
# m == mat.length
# n = mat[i].length
# arr.length == m * n
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 1 <= arr[i], mat[r][c] <= m * n
# All the integers of arr are unique.
# All the integers of mat are unique.
# Solution
# Python O(NM) O(NM) Matrix HashMap Counting
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n: int = len(mat)
        m: int = len(mat[0])
        hashmap: dict[int, tuple[int, int]] = dict()
        row_freq: list[int] = [m] * n
        col_freq: list[int] = [n] * m
        for row in range(n):
            for col in range(m):
                hashmap[mat[row][col]] = (row, col)

        for idx in range(n * m):
            row, col = hashmap[arr[idx]]
            row_freq[row] -= 1
            col_freq[col] -= 1
            if not row_freq[row] or not col_freq[col]: return idx

# C++ O(NM) O(NM) Matrix HashMap Counting
class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();
        std::unordered_map<int, std::pair<int, int>> hashmap;
        std::vector<int> rowFreq (n, m);
        std::vector<int> colFreq (m, n);
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < m; ++col) {
                hashmap[mat[row][col]] = {row, col};
            }
        }
        for (int idx = 0; idx < n * m; ++idx) {
            int row = hashmap[arr[idx]].first;
            int col = hashmap[arr[idx]].second;
            --rowFreq[row];
            --colFreq[col];
            if (!rowFreq[row] || !colFreq[col]) return idx;
        }
        return -1;
    }
};