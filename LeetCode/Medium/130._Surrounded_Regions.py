# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#
# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
#
#
#
# Example 1:
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Explanation:
#
#
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
#
# Example 2:
#
# Input: board = [["X"]]
#
# Output: [["X"]]
#
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# Solution
# Python O(NM) O(NM) Matrix Depth-First-Search
class Solution:
    move: tuple[tuple[int, int]] = (
        (1, 0), (-1, 0), (0, 1), (0, -1)
    )

    def dfs(self, i: int, j: int, board: list[list[str]], seen: list[list[bool]], n: int, m: int) -> None:
        seen[i][j] = True
        for x, y in self.move:
            n_i: int = i + x
            n_j: int = j + y
            if not (0 <= n_i < n) or not (0 <= n_j < m) or board[n_i][n_j] == 'X' or seen[n_i][n_j]: continue
            self.dfs(n_i, n_j, board, seen, n, m)

    def solve(self, board: List[List[str]]) -> None:
        n: int = len(board)
        m: int = len(board[0])
        seen: list[list[bool]] = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X': continue
                elif not i or i == n - 1 or not j or j == m - 1: self.dfs(i, j, board, seen, n, m)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' or seen[i][j]: continue
                board[i][j] = 'X'

# C++ O(NM) O(NM) Depth-First-Search Matrix
class Solution {
public:
    std::vector<std::pair<int, int>> moves = {
        {1, 0}, {-1, 0}, {0, 1}, {0, -1}
    };
    void removeRegion(size_t i, size_t j, std::vector<std::vector<char>>& board, std::vector<std::vector<bool>>& seen, const size_t& n, const size_t& m) {
        seen[i][j] = true;
        for (const std::pair<int, int>& p : moves) {
            if ((!i && p.first == -1) || (i + p.first == n) || (!j && p.second == -1) || (j + p.second == m)) continue;
            if (board[i + p.first][j + p.second] == 'X' || seen[i + p.first][j + p.second]) continue;
            removeRegion(i + p.first, j + p.second, board, seen, n, m);
        }
    }
    void solve(vector<vector<char>>& board) {
        size_t n = board.size(), m = board[0].size();
        std::vector<std::vector<bool>> seen(n, std::vector<bool>(m, false));
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                if (board[i][j] == 'X') continue;
                if (!i || i == n - 1 || !j || j == m - 1) removeRegion(i, j, board, seen, n, m);
            }
        }
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                if (board[i][j] == 'X' || seen[i][j]) continue;
                board[i][j] = 'X';
            }
        }
    }
};