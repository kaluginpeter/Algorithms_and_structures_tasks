# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
# Constraints:
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
# Follow up: Could you use search pruning to make your solution faster with a larger board?
# Solution
# Python O(NMK) O(K) Depth-First-Search Matrix String
class Solution:
    def dfs(self, i: int, j: int, board: list[list[str]], path: list[str], word: str, n: int, m: int) -> bool:
        path.append(board[i][j])
        if len(path) == len(word) and path[-1] == word[-1]: return True
        board[i][j] = '.'

        if j and board[i][j - 1] == word[len(path)]:
            if self.dfs(i, j - 1, board, path, word, n, m): return True
        if i and board[i - 1][j] == word[len(path)]:
            if self.dfs(i - 1, j, board, path, word, n, m): return True
        if j + 1 < m and board[i][j + 1] == word[len(path)]:
            if self.dfs(i, j + 1, board, path, word, n, m): return True
        if i + 1 < n and board[i + 1][j] == word[len(path)]:
            if self.dfs(i + 1, j, board, path, word, n, m): return True

        board[i][j] = path.pop()
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        n: int = len(board)
        m: int = len(board[0])
        path: list[str] = []
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]: continue
                if self.dfs(i, j, board, path, word, n, m): return True
        return False

# C++ O(NMK) O(K) Depth-First-Search Matrix String
class Solution {
public:
    bool dfs(size_t i, size_t j, std::vector<std::vector<char>> &board, std::string &path, std::string &word, size_t n, size_t m) {
        path.push_back(board[i][j]);
        if (path.size() == word.size() && path.back() == word.back()) return true;
        board[i][j] = '.';

        if (j && board[i][j - 1] == word[path.size()]) {
            if (dfs(i, j - 1, board, path, word, n, m)) return true;
        }
        if (i && board[i - 1][j] == word[path.size()]) {
            if (dfs(i - 1, j, board, path, word, n, m)) return true;
        }
        if (j + 1 < m && board[i][j + 1] == word[path.size()]) {
            if (dfs(i, j + 1, board, path, word, n, m)) return true;
        }
        if (i + 1 < n && board[i + 1][j] == word[path.size()]) {
            if (dfs(i + 1, j, board, path, word, n, m)) return true;
        }

        board[i][j] = path.back();
        path.pop_back();
        return false;
    }
    bool exist(vector<vector<char>>& board, string word) {
        size_t n = board.size(), m = board[0].size();
        std::string path = "";
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                if (board[i][j] != word[0]) continue;
                if (dfs(i, j, board, path, word, n, m)) return true;
            }
        }
        return false;
    }
};