# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
#
# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
#
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
#
#
#
# Example 1:
#
#
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
#
# while this one is not:
#
# In total, there is only one magic square inside the given grid.
# Example 2:
#
# Input: grid = [[8]]
# Output: 0
#
#
# Constraints:
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15
# Solution Matrix Simulation Math O(NM) O(1)
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magic_squares: int = 0
        if len(grid) < 3 or len(grid[0]) < 3:
            return magic_squares

        row_rep: int = 0
        while row_rep + 3 <= len(grid):
            col_rep: int = 0
            while col_rep + 3 <= len(grid[0]):
                numbers_in_square: set[int] = set()
                square_sum: int = 0
                valid: bool = True
                for row in range(row_rep, row_rep + 3):
                    for col in range(col_rep, col_rep + 3):
                        ceil: int = grid[row][col]
                        if ceil in numbers_in_square or ceil == 0 or ceil > 9:
                            valid = False
                            break
                        else:
                            numbers_in_square.add(ceil)
                    if not valid: break
                if valid:
                    row_sum: int = sum(grid[row_rep][col_rep:col_rep + 3])
                    diag_sum: int = 0
                    idx: int = 0
                    for row in grid[row_rep:row_rep + 3]:
                        diag_sum += row[col_rep:col_rep + 3][idx]
                        idx += 1
                    reverse_diag_sum: int = 0
                    idx: int = 2
                    for row in grid[row_rep:row_rep + 3]:
                        reverse_diag_sum += row[col_rep:col_rep + 3][idx]
                        idx -= 1
                    if (
                        all(sum(grid[row][col_rep:col_rep + 3]) == row_sum for row in range(row_rep, row_rep + 3))
                        and all(
                            sum(grid[row][col] for row in range(row_rep, row_rep + 3)
                            ) == row_sum for col in range(col_rep, col_rep + 3)
                        ) and diag_sum == row_sum == reverse_diag_sum
                    ):
                        magic_squares += 1
                col_rep += 1
            row_rep += 1
        return magic_squares


# Python O(NM) O(1) Matrix
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        output: int = 0
        n: int = len(grid)
        m: int = len(grid[0])
        for row in range(n - 2):
            for col in range(m - 2):
                seen = [False] * 10
                is_valid: bool = True
                for i in range(3):
                    for j in range(3):
                        num = grid[row + i][col + j]
                        if num < 1 or num > 9:
                            is_valid = False
                            break
                        if seen[num]:
                            is_valid = False
                            break
                        seen[num] = True
                    if not is_valid: break
                if not is_valid: continue
                diagonal1 = (
                    grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
                )
                diagonal2 = (
                    grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]
                )
                if diagonal1 != diagonal2: continue
                row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
                row2 = (
                    grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
                )
                row3 = (
                    grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
                )

                if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1): continue
                col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
                col2 = (
                    grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
                )
                col3 = (
                    grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
                )

                if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1): continue
                output += 1
        return output

# C++ O(NM) O(1) Matrix
class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size(), output = 0;
        for (int i = 0; i < n - 2; ++i) {
            for (int j = 0; j < m - 2; ++j) {
                std::unordered_set<int> contain;
                for (int k = 0; k < 3; ++k) {
                    for (int l = 0; l < 3; ++l) {
                        if (grid[i + k][j + l] > 9 || !grid[i + k][j + l]) break;
                        contain.insert(grid[i + k][j + l]);
                    }
                }
                if (contain.size() != 9) continue;
                contain.clear();
                contain.insert(grid[i][j] + grid[i + 1][j] + grid[i + 2][j]);
                contain.insert(grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]);
                contain.insert(grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]);
                contain.insert(grid[i][j] + grid[i][j + 1] + grid[i][j + 2]);
                contain.insert(grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]);
                contain.insert(grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]);
                contain.insert(grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]);
                contain.insert(grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]);
                if (contain.size() != 1) continue;
                ++output;
            }
        }
        return output;
    }
};