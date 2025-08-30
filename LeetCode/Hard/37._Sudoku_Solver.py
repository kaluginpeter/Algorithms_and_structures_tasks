# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
#
#
#
# Example 1:
#
#
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
#
#
#
#
# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
# Solution
# Python O(9^E) where the E is NM in the worst case. O(NM) Matrix Backtracking HashMap
class Solution:
    def backtrack(self, r: int, c: int, board: list[list[str]], row_hash: list[set[str]], col_hash: list[set[str]], square_hash: list[set[str]], n: int, m: int) -> bool:
        if r == n: return True
        n_r: int = r
        n_c: int = c + 1
        if n_c == m:
            n_c = 0
            n_r += 1
        if board[r][c] != '.': return self.backtrack(n_r, n_c, board, row_hash, col_hash, square_hash, n, m)
        for k in range(1, 10):
            ck: str = str(k)
            square: int = r // 3 * 3 + c // 3
            if ck in row_hash[r] or ck in col_hash[c] or ck in square_hash[square]: continue
            board[r][c] = ck
            row_hash[r].add(ck)
            col_hash[c].add(ck)
            square_hash[square].add(ck)
            if self.backtrack(n_r, n_c, board, row_hash, col_hash, square_hash, n, m): return True
            board[r][c] = '.'
            row_hash[r].remove(ck)
            col_hash[c].remove(ck)
            square_hash[square].remove(ck)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        n: int = len(board)
        m: int = len(board[0])
        row_hash: list[set[int]] = [set() for _ in range(n)]
        col_hash: list[set[int]] = [set() for _ in range(m)]
        square_hash: list[set[int]] = [set() for _ in range((n // 3 + 1) * (m // 3 + 1))]
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.': continue
                row_hash[i].add(board[i][j])
                col_hash[j].add(board[i][j])
                square_hash[i // 3 * 3 + j // 3].add(board[i][j])
        self.backtrack(0, 0, board, row_hash, col_hash, square_hash, n, m)

# C++ O(9^E), where the E is O(NM) in the worst case. O(NM) Matrix Backtracking HashMap
using vusc = std::vector<std::unordered_set<char>>;
using vvc = std::vector<std::vector<char>>;

class Solution {
public:
    bool backtrack(size_t r, size_t c, vvc &board, vusc &rowHash, vusc &colHash, vusc &squareHash, const size_t &n, const size_t &m) {
        if (r == n) return true;
        size_t nR = r, nC = c + 1;
        if (nC == m) {
            nC = 0;
            ++nR;
        }
        if (board[r][c] != '.') return backtrack(nR, nC, board, rowHash, colHash, squareHash, n, m);
        for (int k = 1; k < 10; ++k) {
            char ck = k + '0';
            if (rowHash[r].count(ck) || colHash[c].count(ck)) continue;
            size_t square = r / 3 * 3 + c / 3;
            if (squareHash[square].count(ck)) continue;
            board[r][c] = ck;
            rowHash[r].insert(ck);
            colHash[c].insert(ck);
            squareHash[square].insert(ck);
            if (backtrack(nR, nC, board, rowHash, colHash, squareHash, n, m)) return true;
            board[r][c] = '.';
            rowHash[r].erase(ck);
            colHash[c].erase(ck);
            squareHash[square].erase(ck);
        }
        return false; // there is not possible moves that form correct sudoku
    }

    void solveSudoku(vvc &board) {
        size_t n = 9, m = 9;
        vusc rowHash(n), colHash(m), squareHash(n * m);
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                if (board[i][j] == '.') continue;
                size_t square = i / 3 * 3 + j / 3;
                rowHash[i].insert(board[i][j]);
                colHash[j].insert(board[i][j]);
                squareHash[square].insert(board[i][j]);
            }
        }
        backtrack(0, 0, board, rowHash, colHash, squareHash, n, m);
    }
};