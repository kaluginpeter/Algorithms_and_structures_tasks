# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:
#
# Input: n = 1
# Output: [["Q"]]
#
#
# Constraints:
#
# 1 <= n <= 9
# Solution
# Python O(N * N!) O(N * N * S) Backtracking Memoization
class Solution:
    def add_to_output(self, n: int, placed: list[tuple[int, int]], output: list[list[str]]) -> None:
        board: list[list[str]] = [['.'] * n for _ in range(n)]
        for x, y in placed: board[x][y] = 'Q'
        output.append([''.join(row) for row in board])

    def dfs(self, row: int, n: int, placed: list[tuple[int, int]], output: list[list[str]]) -> None:
        if row == n:
            self.add_to_output(n, placed, output)
            return
        for col in range(n):
            can_place: bool = True
            for x, y in placed:
                if col == y or row == x or (abs(col - y) == abs(row - x)):
                    can_place = False
                    break
            if not can_place: continue
            placed.append((row, col))
            self.dfs(row + 1, n, placed, output)
            placed.pop()

    def solveNQueens(self, n: int) -> List[List[str]]:
        output: list[list[str]] = []
        placed: list[tuple[int, int]] = []
        self.dfs(0, n, placed, output)
        return output

# C++ O(N * N!) O(N * N * S) Backtracking Memoization
class Solution {
public:
    void addToOutput(const int& bound, const std::vector<std::pair<int, int>>& placed, std::vector<std::vector<std::string>>& output) {
        std::vector<std::string> board;
        for (size_t i = 0; i < bound; ++i) {
            std::string row = "";
            for (size_t j = 0; j < bound; ++j) row.push_back('.');
            board.push_back(row);
        }
        for (const std::pair<int, int>& p : placed) board[p.first][p.second] = 'Q';
        output.push_back(board);
    }
    void dfs(int row, const int& n, std::vector<std::pair<int,int>>& placed, std::vector<std::vector<std::string>>& output) {
        if (row == n) {
            addToOutput(n, placed, output);
            return;
        }
        for (int col = 0; col < n; ++col) {
            bool canPlace = true;
            for (const auto& p : placed) {
                if (col == p.second || row == p.first || abs(row - p.first) == abs(col - p.second)) {
                    canPlace = false;
                    break;
                }
            }
            if (!canPlace) continue;
            placed.push_back({row, col});
            dfs(row + 1, n, placed, output);
            placed.pop_back();
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> output;
        std::vector<std::pair<int, int>> placed;
        dfs(0, n, placed, output);
        return output;
    }
};