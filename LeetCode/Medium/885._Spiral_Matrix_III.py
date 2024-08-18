# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
#
# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
#
# Return an array of coordinates representing the positions of the grid in the order you visited them.
#
#
#
# Example 1:
#
#
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
# Example 2:
#
#
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
#
# Constraints:
#
# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols
# Solution Matrix Simulation O(NM) O(NM)
class Solution:
    def check(self, cur_row: int, cur_col: int, rows: int, cols: int, result: list[list[int]]) -> None:
        if 0 <= cur_row < rows and 0 <= cur_col < cols:
            result.append([cur_row, cur_col])

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        output: list[list[int]] = [[rStart, cStart]]
        cur_row, cur_col = rStart, cStart
        boundary: int = 1
        cur_col += 1
        # Make first move from center to right
        self.check(cur_row, cur_col, rows, cols, output)
        while len(output) < rows * cols:
            # Move from upper right corner to down right corner
            down_boundary: int = cur_row + boundary
            cur_row += 1
            while cur_row < down_boundary:
                self.check(cur_row, cur_col, rows, cols, output)
                cur_row += 1

            boundary += 1
            # Move from down right corner to down left corner
            left_boundary: int = cur_col - boundary
            while cur_col > left_boundary:
                self.check(cur_row, cur_col, rows, cols, output)
                cur_col -= 1
            # Move from down left corner to upper left corner
            upper_boundary: int = cur_row - boundary
            while cur_row > upper_boundary:
                self.check(cur_row, cur_col, rows, cols, output)
                cur_row -= 1
            # Move from upper left corner to upper right corner
            right_boundary: int = cur_col + boundary
            while cur_col <= right_boundary:
                self.check(cur_row, cur_col, rows, cols, output)
                cur_col += 1
            # Check upper right corner + 1
            self.check(cur_row, cur_col, rows, cols, output)

            boundary += 1

        return output