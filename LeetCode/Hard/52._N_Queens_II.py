# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:
#
# Input: n = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 9
# Solution
# Python O(N * N!) O(N) Backtracking Memoization
class Solution:
    output: int = 0
    def dfs(self, row: int, n: int, placed: list[tuple[int, int]]) -> None:
        if row == n:
            self.output += 1
            return
        for col in range(n):
            can_place: bool = True
            for x, y in placed:
                if col == y or row == x or (abs(col - y) == abs(row - x)):
                    can_place = False
                    break
            if not can_place: continue
            placed.append((row, col))
            self.dfs(row + 1, n, placed)
            placed.pop()

    def totalNQueens(self, n: int) -> int:
        self.output = 0
        placed: list[tuple[int, int]] = []
        self.dfs(0, n, placed)
        return self.output

# C++ O(N * N!) O(N) Backtracking Memoization
class Solution {
public:
    void dfs(int row, const int& n, std::vector<std::pair<int,int>>& placed, int& output) {
        if (row == n) {
            ++output;
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
    int totalNQueens(int n) {
        int output = 0;
        std::vector<std::pair<int, int>> placed;
        dfs(0, n, placed, output);
        return output;
    }
};