# You are given an n x n integer matrix. You can do the following operation any number of times:
#
# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.
#
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
# Example 2:
#
#
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
#
#
# Constraints:
#
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105
# Solution
# Python O(MN) O(1) Greedy Matrix
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative: int = 0
        total_sum: int = 0
        min_value: int = float('inf')
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] < 0:
                    negative += 1
                    matrix[row][col] *= -1
                total_sum += matrix[row][col]
                min_value = min(min_value, matrix[row][col])
        return total_sum - min_value * 2 if negative & 1 else total_sum

# C++ O(MN) O(1) Greedy Matrix
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long totalSum = 0;
        int minValue = std::pow(10, 5);
        int negative = 0;
        for (int row = 0; row < matrix.size(); ++row) {
            for (int col = 0; col < matrix[0].size(); ++col) {
                if (matrix[row][col] < 0) {
                    ++negative;
                    matrix[row][col] *= -1;
                }
                totalSum += matrix[row][col];
                minValue = std::min(minValue, matrix[row][col]);
            }
        }
        return (negative % 2? totalSum - minValue * 2 : totalSum);
    }
};

# Python O(NM) O(1) Matrix Greedy
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative: int = 0
        mn: int = float('inf')
        output: int = 0
        for row in matrix:
            for num in row:
                output += abs(num)
                mn = min(mn, abs(num))
                if num < 0: negative += 1
        return output - 2 * (mn if negative & 1 else 0)

# C++ O(NM) O(1) Matrix Greedy
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int negative = 0, mn = INT32_MAX;
        long long output = 0;
        for (std::vector<int>& row : matrix) {
            for (int& num : row) {
                if (num < 0) {
                    ++negative;
                    mn = std::min(mn, -num);
                    output += -num;
                }
                else {
                    output += num;
                    mn = std::min(mn, num);
                }
            }
        }
        return (negative & 1 ? output - mn * 2 : output);
    }
};