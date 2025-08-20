# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
#
#
#
# Example 1:
#
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:
#
# Input: matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.
#
#
# Constraints:
#
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1
# Solution
# Python O(NM) O(NM) Depth-First-Search
class Solution:
    def dfs(self, r: int, c: int, matrix: list[list[int]], seen: dict[tuple[int, int], int]) -> int:
        if r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == 0:
            return 0
        if (r, c) in seen:
            return seen[(r, c)]
        max_square: int = 1 + min(
            self.dfs(r + 1, c, matrix, seen),
            self.dfs(r + 1, c + 1, matrix, seen),
            self.dfs(r, c + 1, matrix, seen)
        )
        seen[(r, c)] = max_square
        return max_square

    def countSquares(self, matrix: List[List[int]]) -> int:
        memo: dict[tuple[int, int], int] = dict()
        count_squares: int = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                count_squares += self.dfs(r, c, matrix, memo)
        return count_squares

# C++ O(NM) O(NM) Depth-First-Search
struct pairHash {
    template <class T1, class T2>
    std::size_t operator()(const std::pair<T1, T2>& p) const {
        auto hash1 = std::hash<T1>{}(p.first);
        auto hash2 = std::hash<T2>{}(p.second);
        return hash1 ^ (hash2 << 1); // Combine the two hash values
    }
};
class Solution {
public:
    int dfs(int r, int c, std::vector<std::vector<int>>& matrix, std::unordered_map<std::pair<int, int>, int, pairHash>& seen) {
        if (r >= matrix.size() || c >= matrix[0].size() || !matrix[r][c]) {
            return 0;
        }
        if (seen.count({r, c})) {
            return seen[{r, c}];
        }
        int largestSquare = 1 + std::min(
            {dfs(r + 1, c, matrix, seen),
            dfs(r + 1, c + 1, matrix, seen),
            dfs(r, c + 1, matrix, seen)}
        );
        seen[{r, c}] = largestSquare;
        return largestSquare;
    }

    int countSquares(vector<vector<int>>& matrix) {
        std::unordered_map<std::pair<int, int>, int, pairHash> memo;
        int countSquares = 0;
        for (int row = 0; row < matrix.size(); ++row) {
            for (int col = 0; col < matrix[0].size(); ++col) {
                countSquares += dfs(row, col, matrix, memo);
            }
        }
        return countSquares;
    }
};

# Python O(NM) O(NM) Dynamic Programming
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS: int = len(matrix) + 1
        COLS: int = len(matrix[0]) + 1
        dp: list[list[int]] = [[0] * COLS for row in range(ROWS)]
        count_squares: int = 0
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row - 1][col - 1] == 0:
                    continue
                dp[row][col] = 1 + min(
                    dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1]
                )
                count_squares += dp[row][col]
        return count_squares

# C++ O(NM) O(NM) Dynamic Programming
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int ROWS = matrix.size() + 1;
        int COLS = matrix[0].size() + 1;
        std::vector<std::vector<int>> dp(ROWS, std::vector<int>(COLS));
        int countSquares = 0;
        for (int row = 1; row < ROWS; ++row) {
            for (int col = 1; col < COLS; ++col) {
                if (!matrix[row - 1][col - 1] ) {
                    continue;
                }
                dp[row][col] = 1 + std::min({dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1]});
                countSquares += dp[row][col];
            }
        }
        return countSquares;
    }
};



# Python O(NM) O(NM) DynamicProgramming Matrix
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n: int = len(matrix)
        m: int = len(matrix[0])
        dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not matrix[i - 1][j - 1]: continue
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        return sum(sum(row) for row in dp)

# C++ O(NM) O(NM) DynamicProgramming Matrix
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (!matrix[i - 1][j - 1]) continue;
                dp[i][j] = matrix[i - 1][j - 1] + std::min({
                    dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]
                });
            }
        }
        int output = 0;
        for (int i = 1; i <= n; ++i) {
            output += std::accumulate(dp[i].begin(), dp[i].end(), 0);
        }
        return output;
    }
};