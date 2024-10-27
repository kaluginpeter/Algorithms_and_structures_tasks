# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:
#
# Input: matrix = [["0"]]
# Output: 0
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
# Solution
# Python O(NM) O(NM) Dynamic Programming
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS: int = len(matrix) + 1
        COLS: int = len(matrix[0]) + 1
        dp: list[list[int]] = [[0] * COLS for row in range(ROWS)]
        largest_square: int = 0
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row - 1][col - 1] == '0':
                    continue
                dp[row][col] = 1 + min(
                    dp[row - 1][col],
                    dp[row - 1][col - 1],
                    dp[row][col - 1]
                )
                largest_square = max(largest_square, dp[row][col])
        return largest_square**2

# C++ O(NM) O(NM) Dynamic Programming
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int ROWS = matrix.size() + 1;
        int COLS = matrix[0].size() + 1;
        std::vector<std::vector<int>> dp(ROWS, std::vector<int>(COLS));
        int largestSquare = 0;
        for (int row = 1; row < ROWS; ++row) {
            for (int col = 1; col < COLS; ++col) {
                if (!(matrix[row - 1][col - 1] - '0')) {
                    continue;
                }
                dp[row][col] = 1 + std::min({
                    dp[row - 1][col],
                    dp[row - 1][col - 1],
                    dp[row][col - 1]
                });
                largestSquare = std::max(largestSquare, dp[row][col]);
            }
        }
        return largestSquare * largestSquare;
    }
};