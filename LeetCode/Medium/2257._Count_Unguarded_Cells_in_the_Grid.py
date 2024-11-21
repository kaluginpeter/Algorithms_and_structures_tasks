# You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
#
# A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
#
# Return the number of unoccupied cells that are not guarded.
#
#
#
# Example 1:
#
#
# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
# Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
# There are a total of 7 unguarded cells, so we return 7.
# Example 2:
#
#
# Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
# Output: 4
# Explanation: The unguarded cells are shown in green in the above diagram.
# There are a total of 4 unguarded cells, so we return 4.
#
#
# Constraints:
#
# 1 <= m, n <= 105
# 2 <= m * n <= 105
# 1 <= guards.length, walls.length <= 5 * 104
# 2 <= guards.length + walls.length <= m * n
# guards[i].length == walls[j].length == 2
# 0 <= rowi, rowj < m
# 0 <= coli, colj < n
# All the positions in guards and walls are unique.
# Solution
# Python O(MN + G(MN)) O(MN), where G is number of guards. Simulation Matrix
class Solution:
    def fill_matrix(self, row: int, col: int, matrix: list[list[str]], m: int, n: int) -> None:
        up_row: int = row - 1
        while up_row >= 0 and matrix[up_row][col] != 'W' and matrix[up_row][col] != 'X':
            matrix[up_row][col] = 'G'
            up_row -= 1
        down_row: int = row + 1
        while down_row < m and matrix[down_row][col] != 'W' and matrix[down_row][col] != 'X':
            matrix[down_row][col] = 'G'
            down_row += 1
        right_col: int = col + 1
        while right_col < n and matrix[row][right_col] != 'W' and matrix[row][right_col] != 'X':
            matrix[row][right_col] = 'G'
            right_col += 1
        left_col: int = col - 1
        while left_col >= 0 and matrix[row][left_col] != 'W' and matrix[row][left_col] != 'X':
            matrix[row][left_col] = 'G'
            left_col -= 1

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix: list[list[str]] = [['F'] * n for row in range(m)]
        for wall in walls:
            row, col = wall
            matrix[row][col] = 'W'
        for guard in guards:
            row, col = guard
            matrix[row][col] = 'X'
        for guard in guards:
            row, col = guard
            self.fill_matrix(row, col, matrix, m, n)
        freedom: int = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 'F':
                    freedom += 1
        return freedom

# C++ O(MN + G(MN)) O(MN), where G is number of guards. Matrix Simulation
class Solution {
public:
    void fillMatrix(int row, int col, std::vector<std::vector<char>>& matrix, int m, int n) {
        int upRow = row - 1;
        while (upRow >= 0 && matrix[upRow][col] != 'W' && matrix[upRow][col] != 'X') {
            matrix[upRow][col] = 'G';
            --upRow;
        }
        int downRow = row + 1;
        while (downRow < m && matrix[downRow][col] != 'W' && matrix[downRow][col] != 'X') {
            matrix[downRow][col] = 'G';
            ++downRow;
        }
        int rightCol = col + 1;
        while (rightCol < n && matrix[row][rightCol] != 'W' && matrix[row][rightCol] != 'X') {
            matrix[row][rightCol] = 'G';
            ++rightCol;
        }
        int leftCol = col - 1;
        while (leftCol >= 0 && matrix[row][leftCol] != 'W' && matrix[row][leftCol] != 'X') {
            matrix[row][leftCol] = 'G';
            --leftCol;
        }
    }
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        std::vector<std::vector<char>>matrix(m, std::vector<char>(n, 'F'));
        for (std::vector<int>& wall : walls) {
            int row = wall[0];
            int col = wall[1];
            matrix[row][col] = 'W';
        }
        for (std::vector<int>& guard : guards) {
            int row = guard[0];
            int col = guard[1];
            matrix[row][col] = 'X';
        }
        for (std::vector<int>& guard : guards) {
            int row = guard[0];
            int col = guard[1];
            fillMatrix(row, col, matrix, m, n);
        }
        int freedom = 0;
        for (int row = 0; row < m; ++row) {
            for (int col = 0; col < n; ++col) {
                if (matrix[row][col] == 'F') {
                    ++freedom;
                }
            }
        }
        return freedom;
    }
};