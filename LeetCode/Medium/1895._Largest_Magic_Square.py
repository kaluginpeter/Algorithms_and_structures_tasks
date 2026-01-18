# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.
#
# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.
#
#
#
# Example 1:
#
#
# Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# Output: 3
# Explanation: The largest magic square has a size of 3.
# Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
# - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
# - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
# - Diagonal sums: 5+4+3 = 6+4+2 = 12
# Example 2:
#
#
# Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# Output: 2
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 106
# Solution
# Python O(NMmin(N,M)) O(NM) Matrix PrefixSum
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        rows: list[list[int]] = [[0] * m for _ in range(n)]
        for i in range(n):
            rows[i][0] = grid[i][0]
            for j in range(1, m): rows[i][j] = rows[i][j - 1] + grid[i][j]
        cols: list[list[int]] = [[0] * m for _ in range(n)]
        for j in range(m):
            cols[0][j] = grid[0][j]
            for i in range(1, n): cols[i][j] = cols[i - 1][j] + grid[i][j]
        for size in range(min(n, m), 1, -1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    target: int = rows[i][j + size - 1] - (rows[i][j - 1] if j else 0)
                    is_valid: bool = True
                    for ii in range(i + 1, i + size):
                        if rows[ii][j + size - 1] - (rows[ii][j - 1] if j else 0) != target:
                            is_valid = False
                            break
                    if not is_valid: continue
                    for jj in range(j, j + size):
                        if cols[i + size - 1][jj] - (cols[i - 1][jj] if i else 0) != target:
                            is_valid = False
                            break
                    if not is_valid: continue
                    d1: int = 0
                    d2: int = 0
                    for k in range(size):
                        d1 += grid[i + k][j + k]
                        d2 += grid[i + k][j + size - k - 1]
                    if d1 == d2 == target: return size
        return 1

# C++ O(NMmin(N,M)) O(NM) PrefixSum Matrix
class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        std::vector<std::vector<int>> rows(m, std::vector<int>(n));
        for (int i = 0; i < m; ++i) {
            rows[i][0] = grid[i][0];
            for (int j = 1; j < n; ++j) rows[i][j] = rows[i][j - 1] + grid[i][j];
        }
        std::vector<std::vector<int>> cols(m, std::vector<int>(n));
        for (int j = 0; j < n; ++j) {
            cols[0][j] = grid[0][j];
            for (int i = 1; i < m; ++i) cols[i][j] = cols[i - 1][j] + grid[i][j];
        }
        for (int size = min(m, n); size > 1; --size) {
            for (int i = 0; i + size <= m; ++i) {
                for (int j = 0; j + size <= n; ++j) {
                    int target = rows[i][j + size - 1] - (j ? rows[i][j - 1] : 0);
                    bool isValid = true;
                    for (int ii = i + 1; ii < i + size; ++ii) {
                        if (rows[ii][j + size - 1] - (j ? rows[ii][j - 1] : 0) != target) {
                            isValid = false;
                            break;
                        }
                    }
                    if (!isValid) continue;
                    for (int jj = j; jj < j + size; ++jj) {
                        if (cols[i + size - 1][jj] - (i ? cols[i - 1][jj] : 0) != target) {
                            isValid = false;
                            break;
                        }
                    }
                    if (!isValid) continue;
                    int d1 = 0, d2 = 0;
                    for (int k = 0; k < size; ++k) {
                        d1 += grid[i + k][j + k];
                        d2 += grid[i + k][j + size - 1 - k];
                    }
                    if (d1 == target && d2 == target) return size;
                }
            }
        }
        return 1;
    }
};