# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.
#
# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
#
# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
#
#
#
# Example 1:
#
#
# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]
# Explanation: The constructed 2D array should contain 2 rows and 2 columns.
# The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
# The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
# Example 2:
#
# Input: original = [1,2,3], m = 1, n = 3
# Output: [[1,2,3]]
# Explanation: The constructed 2D array should contain 1 row and 3 columns.
# Put all three elements in original into the first row of the constructed 2D array.
# Example 3:
#
# Input: original = [1,2], m = 1, n = 1
# Output: []
# Explanation: There are 2 elements in original.
# It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
#
#
# Constraints:
#
# 1 <= original.length <= 5 * 104
# 1 <= original[i] <= 105
# 1 <= m, n <= 4 * 104
# Solutions Simulation Matrix Array
# Note:
# We can consider that output answer memory don't count as "computated" memory.
# In this case in both solutions memory will be O(1)
# Complexity
# Time complexity: O(MN)
# Space complexity: O(MN)
# Code
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        main_idx: int = 0
        output: list[list[int]] = []
        for row in range(m):
            cur_row: list[int] = []
            for col in range(n):
                cur_row.append(original[main_idx])
                main_idx += 1
            output.append(cur_row)
        return output

# C++
# Complexity
# Time complexity: O(MN)
# Space complexity: O(MN)
# Code
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        vector<vector<int>> output = {};
        if (m * n != original.size()) {
            return output;
        }
        int main_idx = 0;
        for (int row = 0; row < m; row++) {
            vector<int> cur_row = {};
            for (int col = 0; col < n; col++) {
                cur_row.push_back(original[main_idx]);
                main_idx += 1;
            }
            output.push_back(cur_row);
        }
        return output;
    }
};