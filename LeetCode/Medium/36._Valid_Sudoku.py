# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
#
# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
# Solution
# Python O(MN) O(MN) HashMap Matrix
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: dict[int, set[str]] = defaultdict(set)
        cols: dict[int, set[str]] = defaultdict(set)
        squares: dict[tuple[int, int], set[str]] = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

# C++ O(MN) O(MN) HashMap Matrix
struct PairHash {
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2>& pair) const {
        auto hash1 = std::hash<T1>{}(pair.first);
        auto hash2 = std::hash<T2>{}(pair.second);
        return hash1 ^ (hash2 << 1);
    }
};
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_map<int, std::unordered_set<char>> cols;
        std::unordered_map<int, std::unordered_set<char>> rows;
        std::unordered_map<std::pair<int, int>, std::unordered_set<char>, PairHash> squares;
        for (int r = 0; r < board.size(); ++r) {
            for (int c = 0; c < board[0].size(); ++c) {
                if (board[r][c] == '.') {
                    continue;
                }
                if (
                    cols[c].count(board[r][c])
                    || rows[r].count(board[r][c])
                    || squares[{r / 3, c / 3}].count(board[r][c])
                ) {
                    return false;
                }
                cols[c].insert(board[r][c]);
                rows[r].insert(board[r][c]);
                squares[{r / 3, c / 3}].insert(board[r][c]);
            }
        }
        return true;
    }
};



# Python O(N^2) O(N^2) HashMap Matrix
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n: int = 9
        m: int = 9
        row_hash: list[set[str]] = [set() for _ in range(n)]
        col_hash: list[set[str]] = [set() for _ in range(m)]
        square_hash: dict[tuple[int, int], set[str]] = dict()
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.': continue
                elif board[i][j] in row_hash[i] or board[i][j] in col_hash[j]: return False
                square: tuple[int, int] = (i // 3, j // 3)
                if square in square_hash and board[i][j] in square_hash[square]: return False
                row_hash[i].add(board[i][j])
                col_hash[j].add(board[i][j])
                if square not in square_hash: square_hash[square] = set()
                square_hash[square].add(board[i][j])
        return True

# C++ O(N^2) O(N^2) HashMap Matrix
struct TupleHash {
    size_t operator()(const std::tuple<int, int>& t) const noexcept {
        auto [a, b] = t;
        size_t h1 = std::hash<int>()(a);
        size_t h2 = std::hash<int>()(b);
        return h1 ^ (h2 + 0x9e3779b9 + (h1 << 6) + (h1 >> 2));
    }
};

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        size_t n = 9, m = 9;
        std::vector<std::unordered_set<char>> rowHash(n), colHash(m);
        std::unordered_map<std::tuple<int, int>, std::unordered_set<char>, TupleHash> squaresHash;
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                if (board[i][j] == '.') continue;
                if (rowHash[i].count(board[i][j]) || colHash[j].count(board[i][j])) return false;
                std::tuple<int, int> square = std::make_tuple(i / 3, j / 3);
                if (squaresHash[square].count(board[i][j])) return false;
                rowHash[i].insert(board[i][j]);
                colHash[j].insert(board[i][j]);
                squaresHash[square].insert(board[i][j]);
            }
        }
        return true;
    }
};