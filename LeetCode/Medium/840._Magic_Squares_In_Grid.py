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