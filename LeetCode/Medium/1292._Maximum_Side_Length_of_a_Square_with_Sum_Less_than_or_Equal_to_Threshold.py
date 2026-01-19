# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:
#
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105
# Solution
# Python O(NM + log2(D)(N - D + 1)(M - D + 1)) O(NM) where D = min(N, M) BinarySearch Matrix PrefixSum
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n: int = len(mat)
        m: int = len(mat[0])
        prefix: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = mat[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
        left: int = 1
        right: int = min(n, m)
        while left <= right:
            sz: int = left + ((right - left) >> 1)
            is_valid: bool = False
            for i in range(sz, n + 1):
                for j in range(sz, m + 1):
                    square_sum: int = prefix[i][j]
                    square_sum -= prefix[i][j - sz] + prefix[i - sz][j]
                    square_sum += prefix[i - sz][j - sz]
                    if square_sum <= threshold:
                        is_valid = True
                        break
                if is_valid: break
            if is_valid: left = sz + 1
            else: right = sz - 1
        return right

# C++ O(NM + log2(D)(N - D + 1)(M - D + 1)) O(NM), where D = min(N, M) PrefixSum Matrix BinarySearch
class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        size_t n = mat.size(), m = mat[0].size(), bound = std::min(n, m);
        std::vector<std::vector<int>> prefix(n + 1, std::vector<int>(m + 1, 0));
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                prefix[i + 1][j + 1] = mat[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j];
            }
        }
        size_t left = 1, right = std::min(n, m);
        while (left <= right) {
            size_t sz = left + ((right - left) >> 1);
            bool isValid = false;
            for (size_t i = sz; i <= n; ++i) {
                for (size_t j = sz; j <= m; ++j) {
                    int squareSum = prefix[i][j];
                    squareSum -= prefix[i][j - sz] + prefix[i - sz][j];
                    squareSum += prefix[i - sz][j - sz];
                    if (squareSum <= threshold) {
                        isValid = true;
                        break;
                    };
                }
                if (isValid) break;
            }
            if (isValid) left = sz + 1;
            else right = sz - 1;
        }
        return right;
    }
};