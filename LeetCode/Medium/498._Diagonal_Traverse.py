# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:
#
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105
# Solution
# Python O(NM) O(NM) Matrix Simulation
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output: list[int] = []
        n: int = len(mat)
        m: int = len(mat[0])
        ui: int = 0
        uj: int = 0
        di: int = 0
        dj: int = 1
        if m == 1:
            di = 1
            dj = 0
        lines = 1
        while lines != n + m:
            if lines & 1:
                i: int = ui
                j: int = uj
                while i >= 0 and j < m:
                    output.append(mat[i][j])
                    i -= 1
                    j += 1
                ui += 2
                if ui >= n:
                    uj += ui - n + 1
                    ui = n - 1
            else:
                i: int = di
                j: int = dj
                while i < n and j >= 0:
                    output.append(mat[i][j])
                    i += 1
                    j -= 1
                dj += 2
                if dj >= m:
                    di += dj - m + 1
                    dj = m - 1
            lines += 1
        return output

# C++ O(NM) O(NM) Matrix Simulation
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        std::vector<int> output;
        int n = mat.size(), m = mat[0].size();
        int ui = 0, uj = 0, di = 0, dj = 1, iter = 1;
        if (m == 1) {
            di = 1;
            dj = 0;
        }
        while (iter != n + m) {
            if (iter & 1) {
                int i = ui, j = uj;
                while (i >= 0 && j < m) {
                    output.push_back(mat[i][j]);
                    --i;
                    ++j;
                }
                ui += 2;
                if (ui >= n) {
                    uj += ui - n + 1;
                    ui = n - 1;
                }
            } else {
                int i = di, j = dj;
                while (i < n && j >= 0) {
                    output.push_back(mat[i][j]);
                    ++i;
                    --j;
                }
                dj += 2;
                if (dj >= m) {
                    di += dj - m + 1;
                    dj = m - 1;
                }
            }
            ++iter;
        }
        return output;
    }
};