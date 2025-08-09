# Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
#
# i - k <= r <= i + k,
# j - k <= c <= j + k, and
# (r, c) is a valid position in the matrix.
#
#
# Example 1:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# Example 2:
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n, k <= 100
# 1 <= mat[i][j] <= 100
# Solution
# Python O(NM) O(NM) Matrix PrefixSum
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n: int = len(mat)
        m: int = len(mat[0])
        prefix_sum: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]
        output: list[list[int]] = [[0] * m for _ in range(n)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                output[i - 1][j - 1] = prefix_sum[min(n, i + k)][min(m, j + k)] - prefix_sum[min(n, i + k)][max(0, j - k - 1)] - prefix_sum[max(0, i - k - 1)][min(m, j + k)] + prefix_sum[max(0, i - k - 1)][max(0, j - k - 1)]
        return output

# C++ O(NM) O(NM) Matrix PrefixSum
class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
        int n = mat.size(), m = mat[0].size();
        std::vector<std::vector<int>> prefixSum(n + 1, std::vector<int>(m + 1, 0));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                prefixSum[i][j] = prefixSum[i][j - 1] + prefixSum[i - 1][j] - prefixSum[i - 1][j - 1] + mat[i - 1][j - 1];
            }
        }
        std::vector<std::vector<int>> output(n, std::vector<int>(m, 0));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                output[i - 1][j - 1] = prefixSum[std::min(n, i + k)][std::min(m, j + k)] - prefixSum[std::min(n, i + k)][std::max(0, j - k - 1)] - prefixSum[std::max(0, i - k - 1)][std::min(m, j + k)] + prefixSum[std::max(0, i - k - 1)][std::max(0, j - k - 1)];
            }
        }
        return output;
    }
};