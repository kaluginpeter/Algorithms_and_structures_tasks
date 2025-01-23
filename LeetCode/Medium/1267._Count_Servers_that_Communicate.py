# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
#
# Return the number of servers that communicate with any other server.
#
#
#
# Example 1:
#
#
#
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
# Example 2:
#
#
#
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.
# Example 3:
#
#
#
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
# Solution
# Python O(NM) O(N + M) Matrix Counting
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        rows: list[int] = [0] * n
        cols: list[int] = [0] * m
        for row in range(n):
            for col in range(m):
                if grid[row][col]:
                    rows[row] += 1
                    cols[col] += 1
        communicate: int = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] and (rows[row] > 1 or cols[col] > 1):
                    communicate += 1
        return communicate

# C++ O(NM) O(N + M) Matrix Counting
class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        std::vector<int> rows (n, 0);
        std::vector<int> cols(m, 0);
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < m; ++col) {
                if (grid[row][col]) {
                    ++rows[row];
                    ++cols[col];
                }
            }
        }
        int communicate = 0;
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < m; ++col) {
                if (grid[row][col] && (rows[row] > 1 || cols[col] > 1)) communicate += 1;
            }
        }
        return communicate;
    }
};