# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
#
# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
#
# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
#
# Return an n x m matrix representing the box after the rotation described above.
#
#
#
# Example 1:
#
#
#
# Input: box = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
# Example 2:
#
#
#
# Input: box = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]
# Example 3:
#
#
#
# Input: box = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
#
#
# Constraints:
#
# m == box.length
# n == box[i].length
# 1 <= m, n <= 500
# box[i][j] is either '#', '*', or '.'.
# Solution
# Python O(MN) O(MN) Matrix Two Pointers
class Solution:
    def find_gravity_position(self, cur_idx: int, row: int, matrix: list[list[str]]) -> int:
        while cur_idx >= 0 and matrix[row][cur_idx] != '.':
            cur_idx -= 1
        return cur_idx

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for row in range(m):
            gravity_position: int = self.find_gravity_position(n - 1, row, box)
            col: int = gravity_position - 1
            while col >= 0:
                if box[row][col] == '*':
                    gravity_position = self.find_gravity_position(col - 1, row, box)
                    col = gravity_position
                elif box[row][col] == '#':
                    box[row][gravity_position] = box[row][col]
                    box[row][col] = '.'
                    gravity_position = self.find_gravity_position(gravity_position - 1, row, box)
                    col = gravity_position
                col -= 1
        rotated_matrix: list[list[str]] = []
        for col in range(n):
            rotated_row: list[str] = []
            for row in range(m - 1, -1, -1):
                rotated_row.append(box[row][col])
            rotated_matrix.append(rotated_row)
        return rotated_matrix

# C++ O(MN) O(MN) Matrix Two Pointers
class Solution {
public:
    int findGravityPosition(int curIndex, int row, std::vector<std::vector<char>>& matrix) {
        while (curIndex >= 0 && matrix[row][curIndex] != '.') {
            --curIndex;
        }
        return curIndex;
    }

    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size(), n = box[0].size();
        for (int row = 0; row < m; ++row) {
            int gravityPosition = findGravityPosition(n - 1, row, box);
            int col = gravityPosition - 1;
            while (col >= 0) {
                if (box[row][col] == '*') {
                    gravityPosition = findGravityPosition(col - 1, row, box);
                    col = gravityPosition;
                } else if (box[row][col] == '#') {
                    box[row][gravityPosition] = box[row][col];
                    box[row][col] = '.';
                    gravityPosition = findGravityPosition(gravityPosition - 1, row, box);
                    col = gravityPosition;
                }
                --col;
            }
        }
        std::vector<std::vector<char>> rotatedMatrix;
        for (int col = 0; col < n; ++col) {
            std::vector<char> rotatedRow;
            for (int row = m - 1; row >= 0; --row) {
                rotatedRow.push_back(box[row][col]);
            }
            rotatedMatrix.push_back(rotatedRow);
        }
        return rotatedMatrix;
    }
};