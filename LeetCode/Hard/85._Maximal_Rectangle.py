# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:
#
# Input: matrix = [["0"]]
# Output: 0
# Example 3:
#
# Input: matrix = [["1"]]
# Output: 1
#
#
# Constraints:
#
# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
# Solution Monotonic Stack O(N**2) O(N)
class Solution:
    def maximalRectangleInHistogram(self, arr: list[int]) -> int:
        arr.append(0)
        stack: list[int] = list()
        ans: int = 0
        for idx in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[idx]:
                h: int = arr[stack.pop()]
                w: int = idx if not stack else idx - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(idx)
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        stack: list[int] = [0] * len(matrix[0])
        ans: int = 0
        for rows in matrix:
            for cols in range(len(rows)):
                stack[cols] = 0 if rows[cols] == '0' else stack[cols] + int(rows[cols])
            ans = max(ans, self.maximalRectangleInHistogram(stack))
        return ans


# Python O(NM) O(M) DynamicProgramming Matrix
class Solution:
    def get_area(self, cols: list[int], m: int) -> int:
        output: int = 0
        prev: list[int] = []
        for i in range(m + 1):
            while prev and cols[prev[-1]] >= cols[i]:
                height: int = cols[prev[-1]]
                width: int = i - (0 if len(prev) == 1 else prev[-2] + 1)
                output = max(output, height * width)
                prev.pop()
            prev.append(i)
        return output

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n: int = len(matrix)
        m: int = len(matrix[0])
        output: int = 0
        cols: list[int] = [0] * (m + 1)
        for i in range(n):
            for j in range(m):
                cols[j] = cols[j] * int(matrix[i][j]) + int(matrix[i][j])
            output = max(output, self.get_area(cols, m))
        return output

# C++ O(NM) O(M) Matrix DynamicProgramming
class Solution {
public:
    int getArea(const std::vector<int>& cols, const int& m) {
        int output = 0;
        std::vector<size_t> prev;
        for (size_t i = 0; i < cols.size(); ++i) {
            while (!prev.empty() && cols[prev.back()] >= cols[i]) {
                int height = cols[prev.back()];
                int width = (prev.size() == 1 ? i : i - prev[prev.size() - 2] - 1);
                output = std::max(output, height * width);
                prev.pop_back();
            }
            prev.push_back(i);
        }
        return output;
    }
    int maximalRectangle(vector<vector<char>>& matrix) {
        int output = 0;
        size_t n = matrix.size(), m = matrix[0].size();
        std::vector<int> cols(m + 1, 0);
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                cols[j] = cols[j] * (matrix[i][j] - '0') + (matrix[i][j] - '0');
            }
            output = std::max(output, getArea(cols, m));
        }
        return output;
    }
};

# C++ O(N^2M) O(NM) DynamicProgramming
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        std::vector<std::vector<int>>dp(n + 1, std::vector<int>(m + 1, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = m - 1; j >= 0; --j) {
                if (matrix[i][j] == '0') dp[i][j] = 0;
                else dp[i][j] = 1 + dp[i][j + 1];
            }
        }
        int output = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int width = m, length = 0;
                for (int k = 0; k < (n - i); ++k) {
                    if (!matrix[i + k][j]) break;
                    ++length;
                    width = std::min(width, dp[i + k][j]);
                    output = std::max(output, length * width);
                }
            }
        }
        return output;
    }
};