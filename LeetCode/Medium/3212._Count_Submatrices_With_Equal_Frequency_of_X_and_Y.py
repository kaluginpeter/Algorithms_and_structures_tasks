# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of
# submatrices
#  that contains:
#
# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.
#
#
# Example 1:
#
# Input: grid = [["X","Y","."],["Y",".","."]]
#
# Output: 3
#
# Explanation:
#
#
#
# Example 2:
#
# Input: grid = [["X","X"],["X","Y"]]
#
# Output: 0
#
# Explanation:
#
# No submatrix has an equal frequency of 'X' and 'Y'.
#
# Example 3:
#
# Input: grid = [[".","."],[".","."]]
#
# Output: 0
#
# Explanation:
#
# No submatrix has at least one 'X'.
#
#
#
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.
# Solution O(N) O(N)
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        prefix_x: list[int] = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefix_y: list[int] = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_x[i][j] = prefix_x[i-1][j] + prefix_x[i][j-1] - prefix_x[i-1][j-1] + (grid[i-1][j-1] == 'X')
                prefix_y[i][j] = prefix_y[i-1][j] + prefix_y[i][j-1] - prefix_y[i-1][j-1] + (grid[i-1][j-1] == 'Y')
        valid_submatrices: int = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                count_x = prefix_x[i][j] - prefix_x[0][j] - prefix_x[i][0] + prefix_x[0][0]
                count_y = prefix_y[i][j] - prefix_y[0][j] - prefix_y[i][0] + prefix_y[0][0]
                if count_x == count_y and count_x > 0: valid_submatrices += 1
        return valid_submatrices


# Python O(NM) O(M) PrefixSum Matrix
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        output: int = 0
        prefix: list[list[int]] = [[0, 0] for _ in range(m)]
        for i in range(n):
            x: int = 0
            y: int = 0
            for j in range(m):
                if grid[i][j] == 'X': prefix[j][0] += 1
                elif grid[i][j] == 'Y': prefix[j][1] += 1
                x += prefix[j][0]
                y += prefix[j][1]
                if x and x == y: output += 1
        return output

# C++ O(NM) O(M) Matrix PrefixSum
class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        size_t n = grid.size(), m = grid[0].size();
        uint32_t output = 0;
        std::vector<std::pair<uint32_t, uint32_t>> prefix(m, std::pair<uint32_t, uint32_t>());
        for (size_t i = 0; i < n; ++i) {
            uint32_t x = 0, y = 0;
            for (size_t j = 0; j < m; ++j) {
                if (grid[i][j] == 'X') ++prefix[j].first;
                else if (grid[i][j] == 'Y') ++prefix[j].second;
                x += prefix[j].first;
                y += prefix[j].second;
                if (x && x == y) ++output;
            }
        }
        return output;
    }
};