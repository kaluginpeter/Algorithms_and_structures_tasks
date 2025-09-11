# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#
#
#
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:
#
# Input: n = 1
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= n <= 20
# Solution
# Python O(N^2) O(N^2) Matrix TwoPointers
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output: list[list[int]] = [[0] * n for _ in range(n)]
        number: int = 1
        left: int = 0
        right: int = n - 1
        while left <= right:
            if left == right:
                output[left][left] = number
                break
            # from up to right
            for i in range(left, right):
                output[left][i] = number
                number += 1
            # from right to down
            for i in range(left, right):
                output[i][right] = number
                number += 1
            # from down to left
            for i in range(right, left, -1):
                output[right][i] = number
                number += 1
            # from left to up
            for i in range(right, left, -1):
                output[i][left] = number
                number += 1
            left += 1
            right -= 1
        return output

# C++ O(N^2) O(N^2) Matrix TwoPointers
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        std::vector<std::vector<int>> output = std::vector<std::vector<int>>(n, std::vector<int>(n, 0));
        int number = 1, left = 0, right = n - 1;
        while (left <= right) {
            if (left == right) {
                output[left][left] = number;
                break;
            }
            // from up ro right
            for (size_t i = left; i < right; ++i) {
                output[left][i] = number;
                ++number;
            }
            // from right to down
            for (size_t i = left; i < right; ++i) {
                output[i][right] = number;
                ++number;
            }
            // from down to left
            for (size_t i = right; i > left; --i) {
                output[right][i] = number;
                ++number;
            }
            // from left to up
            for (size_t i = right; i > left; --i) {
                output[i][left] = number;
                ++number;
            }
            ++left;
            --right;
        }
        return output;
    }
};