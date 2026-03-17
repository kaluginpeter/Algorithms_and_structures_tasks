# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
#
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
#
#
#
# Example 1:
#
#
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
# Example 2:
#
#
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
# Example 3:
#
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 105
# matrix[i][j] is either 0 or 1.
#
# Solution
# Python O(NM) O(N) DynamicProgramming Matrix
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n: int = len(matrix)
        m: int = len(matrix[0])
        output: int = 0
        prev_dp: list[tuple[int, int]] = []
        for i in range(n):
            dp: list[tuple[int, int]] = []
            seen: list[bool] = [False] * m
            for height, col in prev_dp:
                if matrix[i][col]:
                    dp.append((height + 1, col))
                    seen[col] = 1
            for j in range(m):
                if not seen[j] and matrix[i][j]: dp.append((1, j))
            for i in range(len(dp)): output = max(output, dp[i][0] * (i + 1))
            prev_dp = dp
        return output

# C++ O(NM) O(N) Matrix DynamicProgramming
class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        size_t n = matrix.size(), m = matrix[0].size(), output = 0;
        std::vector<std::pair<int,int>> prevDp;
        for (int i = 0; i < n; ++i) {
            std::vector<std::pair<int,int>> dp;
            std::vector<bool> seen(m, false);
            for (auto [height, col] : prevDp) {
                if (matrix[i][col] == 1) {
                    dp.push_back({height + 1, col});
                    seen[col] = 1;
                }
            }
            for (int j = 0; j < m; ++j) {
                if (!seen[j] && matrix[i][j] == 1) dp.push_back({1, j});
            }
            for (size_t i = 0; i < dp.size(); ++i) output = std::max(output, dp[i].first * (i + 1));
            prevDp = dp;
        }
        return output;
    }
};