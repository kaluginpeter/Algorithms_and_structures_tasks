# Given a m x n matrix grid which is sorted in non-increasing order
# both row-wise and column-wise, return the number of negative numbers in grid.
#
# Example 1:
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
# Follow up: Could you find an O(n + m) solution?
# Solution
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for i in grid:
            for j in i:
                if j < 0:
                    c += 1
        return c


# Python O(N + M) O(1) Greedy Matrix
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        output: int = 0
        m: int = len(grid[0])
        hor: int = m - 1
        for i in range(len(grid)):
            while hor >= 0 and grid[i][hor] < 0: hor -= 1
            output += m - hor - 1
        return output

# C++ O(N + M) O(1) Matrix Greedy
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        int output = 0, hor = m - 1;
        for (int i = 0; i < n; ++i) {
            while (hor >= 0 && grid[i][hor] < 0) --hor;
            output += m - hor - 1;
        }
        return output;
    }
};