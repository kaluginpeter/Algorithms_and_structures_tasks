# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
#
# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:
#
# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
#
# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
# Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
# Example 2:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
# Output: 1
# Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# 0 <= grid[i][j] <= 10
# Solution
# Python O(NM) O(NM) Depth-First-Search Matrix
class Solution:
    moves: list[tuple[int, int]] = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]
    def dfs(self, r: int, c: int, grid: list[list[int]], seen: list[list[bool]]) -> int:
        fish: int = 0
        n: int = len(grid)
        m: int = len(grid[0])
        seen[r][c] = True
        stack: list[tuple[int, int]] = [(r, c)]
        while stack:
            cur_row, cur_col = stack.pop()
            fish += grid[cur_row][cur_col]
            for x, y in self.moves:
                next_row, next_col = cur_row + x, cur_col + y
                if (
                    (0 <= min(next_row, next_col))
                    and (next_row < n and next_col < m)
                    and (grid[next_row][next_col])
                    and (not seen[next_row][next_col])
                ):
                    stack.append((next_row, next_col))
                    seen[next_row][next_col] = True
        return fish

    def findMaxFish(self, grid: List[List[int]]) -> int:
        max_fish: int = 0
        n: int = len(grid)
        m: int = len(grid[0])
        seen: list[list[bool]] = [[False] * m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if grid[row][col] and not seen[row][col]:
                    max_fish = max(max_fish, self.dfs(row, col, grid, seen))
        return max_fish

# C++ O(NM) O(NM) Depth-First-Search Matrix
class Solution {
public:
    std::vector<std::pair<int, int>> moves = {
        {1, 0}, {-1, 0}, {0, 1}, {0, -1}
    };

    int dfs(int r, int c, std::vector<std::vector<int>>& grid, std::vector<std::vector<bool>>& seen) {
        int fish = 0;
        int n = grid.size();
        int m = grid[0].size();
        seen[r][c] = true;
        std::vector<std::tuple<int, int>> stack = {{r, c}};
        while (!stack.empty()) {
            std::tuple<int, int> cell = stack[stack.size() - 1];
            stack.pop_back();
            int& curRow = std::get<0>(cell);
            int& curCol = std::get<1>(cell);
            fish += grid[curRow][curCol];
            for (std::pair<int, int>& move : moves) {
                int nextRow = curRow + move.first;
                int nextCol = curCol + move.second;
                if (
                    (0 <= std::min(nextRow, nextCol))
                    && (nextRow < n && nextCol < m)
                    && (!seen[nextRow][nextCol])
                    && (grid[nextRow][nextCol] > 0)
                ) {
                    stack.push_back({nextRow, nextCol});
                    seen[nextRow][nextCol] = true;
                }
            }
        }
        return fish;
    }

    int findMaxFish(vector<vector<int>>& grid) {
        int maxFish = 0;
        int n = grid.size();
        int m = grid[0].size();
        std::vector<std::vector<bool>> seen (n, std::vector<bool>(m, false));
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < m; ++col) {
                if (grid[row][col] && !seen[row][col]) maxFish = std::max(maxFish, dfs(row, col, grid, seen));
            }
        }
        return maxFish;
    }
};