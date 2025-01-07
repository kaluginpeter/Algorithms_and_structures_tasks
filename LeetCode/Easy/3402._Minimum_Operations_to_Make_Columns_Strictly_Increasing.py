# You are given a m x n matrix grid consisting of non-negative integers.
#
# In one operation, you can increment the value of any grid[i][j] by 1.
#
# Return the minimum number of operations needed to make all columns of grid strictly increasing.
#
#
#
# Example 1:
#
# Input: grid = [[3,2],[1,3],[3,4],[0,1]]
#
# Output: 15
#
# Explanation:
#
# To make the 0th column strictly increasing, we can apply 3 operations on grid[1][0], 2 operations on grid[2][0], and 6 operations on grid[3][0].
# To make the 1st column strictly increasing, we can apply 4 operations on grid[3][1].
#
# Example 2:
#
# Input: grid = [[3,2,1],[2,1,0],[1,2,3]]
#
# Output: 12
#
# Explanation:
#
# To make the 0th column strictly increasing, we can apply 2 operations on grid[1][0], and 4 operations on grid[2][0].
# To make the 1st column strictly increasing, we can apply 2 operations on grid[1][1], and 2 operations on grid[2][1].
# To make the 2nd column strictly increasing, we can apply 2 operations on grid[1][2].
#
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 0 <= grid[i][j] < 2500
# Solution
# Python O(MN) O(1) Matrix Greedy
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations: int = 0
        for col in range(len(grid[0])):
            prev_value: int = grid[0][col]
            for row in range(1, len(grid)):
                if grid[row][col] <= prev_value:
                    operations += prev_value - grid[row][col] + 1
                    prev_value += 1
                else:
                    prev_value = grid[row][col]
        return operations

# C++ O(MN) O(1) Matrix Greedy
class Solution {
public:
    int minimumOperations(vector<vector<int>>& grid) {
        int operations = 0;
        for (int col = 0; col < grid[0].size(); ++col) {
            int prevValue = grid[0][col];
            for (int row = 1; row < grid.size(); ++row) {
                if (grid[row][col] <= prevValue) {
                    operations += prevValue - grid[row][col] + 1;
                    ++prevValue;
                } else {
                    prevValue = grid[row][col];
                }
            }
        }
        return operations;
    }
};