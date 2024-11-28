# You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
#
# 0 represents an empty cell,
# 1 represents an obstacle that may be removed.
# You can move up, down, left, or right from and to an empty cell.
#
# Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
# Output: 2
# Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
# It can be shown that we need to remove at least 2 obstacles, so we return 2.
# Note that there may be other ways to remove 2 obstacles to create a path.
# Example 2:
#
#
# Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
# Output: 0
# Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 2 <= m * n <= 105
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
# Solution
# Python O(ElogE) O(ElogE) Dijkstra Shortest Path Matrix Priority Queue
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq: list[tuple[int]] = []
        seen: set[tuple[int]] = set()
        seen.add((0, 0))
        moves: list[tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        heapq.heappush(pq, (grid[0][0], 0, 0))
        while pq:
            cur_removes, cur_row, cur_col = heapq.heappop(pq)
            if cur_row == m - 1 and cur_col == n - 1:
                return cur_removes
            seen.add((cur_row, cur_col))
            for move in moves:
                next_row, next_col = cur_row + move[0], cur_col + move[1]
                if 0 <= min(next_row, next_col) and next_row < m and next_col < n and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    heapq.heappush(pq, (cur_removes + grid[next_row][next_col], next_row, next_col))
        return -1

# C++ O(ElogE) O(ElogE) Dijkstra Shortest Path Matrix Priority Queue
class Solution {
public:
    int minimumObstacles(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        using State = std::tuple<int, int, int>; // (current number of obstacles removed, row, col)
        auto cmp = [](const State& a, const State& b) {
            return std::get<0>(a) > std::get<0>(b); // Min-heap based on obstacles removed
        };
        std::priority_queue<State, std::vector<State>, decltype(cmp)> pq(cmp);
        // 2D vector to track visited cells
        std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));
        pq.push({grid[0][0], 0, 0}); // Start from the top-left corner
        visited[0][0] = true;
        std::vector<std::pair<int, int>> moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!pq.empty()) {
            auto [curRemoves, curRow, curCol] = pq.top();
            pq.pop();

            if (curRow == m - 1 && curCol == n - 1) {
                return curRemoves;
            }
            for (const auto& move : moves) {
                int nextRow = curRow + move.first;
                int nextCol = curCol + move.second;
                if (nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n && !visited[nextRow][nextCol]) {
                    visited[nextRow][nextCol] = true;
                    pq.push({curRemoves + grid[nextRow][nextCol], nextRow, nextCol});
                }
            }
        }
        return -1;
    }
};