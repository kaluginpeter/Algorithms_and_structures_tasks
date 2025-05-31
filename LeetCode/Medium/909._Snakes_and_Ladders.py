# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
#
# You start on square 1 of the board. In each move, starting from square curr, do the following:
#
# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.
#
# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.
#
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.
#
#
#
# Example 1:
#
#
# Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation:
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so return 4.
# Example 2:
#
# Input: board = [[-1,-1],[-1,3]]
# Output: 1
#
#
# Constraints:
#
# n == board.length == board[i].length
# 2 <= n <= 20
# board[i][j] is either -1 or in the range [1, n2].
# The squares labeled 1 and n2 are not the starting points of any snake or ladder.
# Solution
# Python O(N^2) O(N^2) Breadth-First-Search Matrix
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n: int = len(board)
        dp: list[list[int]] = [[401] * n for _ in range(n)]
        cur_nodes: list[tuple[int, int]] = [(0, 0)]
        next_nodes: list[tuple[int, int]] = []
        dp[0][0] = 0
        while cur_nodes:
            for row, col in cur_nodes:
                path: int = dp[row][[col, n - col - 1][row & 1]]
                for move in range(1, 7):
                    next_ceil: int = row * n + col + move
                    if next_ceil >= n * n: continue
                    next_row: int = next_ceil // n
                    next_col: int = next_ceil % n
                    if board[next_row][[next_col, n - next_col - 1][next_row & 1]] != -1:
                        next_ceil: int = board[next_row][[next_col, n - next_col - 1][next_row & 1]] - 1
                        next_row_jump: int = next_ceil // n
                        next_col_jump: int = next_ceil % n
                        if path + 1 < dp[next_row_jump][[next_col_jump, n - next_col_jump - 1][next_row_jump & 1]]:
                            dp[next_row_jump][[next_col_jump, n - next_col_jump - 1][next_row_jump & 1]] = path + 1
                            next_nodes.append((next_row_jump, next_col_jump))
                    elif path + 1 < dp[next_row][[next_col, n - next_col - 1][next_row & 1]]:
                        dp[next_row][[next_col, n - next_col - 1][next_row & 1]] = path + 1
                        next_nodes.append((next_row, next_col))
            cur_nodes = next_nodes
            next_nodes = []
        return [dp[n - 1][[n - 1, 0][(n - 1) & 1]], -1][dp[n - 1][[n - 1, 0][(n - 1) & 1]] == 401]

# C++ O(N^2) O(N^2) Breadth-First-Search Matrix
class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        reverse(board.begin(), board.end());
        int n = board.size();
        vector<vector<int>> dp(n, vector<int>(n, 401));
        vector<pair<int, int>> curNodes, nextNodes;
        curNodes.push_back({0, 0});
        dp[0][0] = 0;
        while (!curNodes.empty()) {
            for (pair<int, int> &cell : curNodes) {
                int row = cell.first, col = cell.second;
                int path = dp[row][(row & 1? n - col - 1 : col)];
                for (int move = 1; move <= 6; ++move) {
                    int nextCell = row * n + col + move;
                    if (nextCell >= n * n) continue;
                    int nextRow = nextCell / n;
                    int nextCol = nextCell % n;
                    if (board[nextRow][(nextRow & 1? n - nextCol - 1 : nextCol)] != -1) {
                        int nextCell = board[nextRow][(nextRow & 1? n - nextCol - 1 : nextCol)] - 1;
                        int nextRow = nextCell / n;
                        int nextCol = nextCell % n;
                        if (path + 1 < dp[nextRow][(nextRow & 1? n - nextCol - 1 : nextCol)]) {
                            dp[nextRow][(nextRow & 1? n - nextCol - 1 : nextCol)] = path + 1;
                            nextNodes.push_back({nextRow, nextCol});
                        }
                    } else if (path + 1 < dp[nextRow][(nextRow & 1? n - nextCol - 1 : nextCol)]) {
                        dp[nextRow][(nextRow & 1? n - nextCol - 1 : nextCol)] = path + 1;
                        nextNodes.push_back({nextRow, nextCol});
                    }
                }
            }
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return (dp[n - 1][(n & 1? n - 1 : 0)] == 401? -1 : dp[n - 1][(n & 1? n - 1 : 0)]);
    }
};