# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
#
# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.
#
# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
#
#
#
# Example 1:
#
#
# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# Example 2:
#
#
# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
#
#
# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n2
# Each value grid[i][j] is unique.
# Solution
# Python O((NM)log(NM)) O(NM) Shortest Path Dijkstra Priority Queue
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        bound: int = 50 * 50 + 1
        distances: dict[int, int] = dict()
        n: int = len(grid)
        m: int = len(grid[0])
        for row in range(n):
            for col in range(m):
                distances[grid[row][col]] = bound
        min_heap: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        moves: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while min_heap:
            cur_cost, cur_row, cur_col = heapq.heappop(min_heap)
            if distances[grid[cur_row][cur_col]] != bound:
                continue
            distances[grid[cur_row][cur_col]] = cur_cost
            for move in moves:
                next_row: int = cur_row + move[0]
                next_col: int = cur_col + move[1]
                if min(next_row, next_col) >= 0 and next_row < n and next_col < m:
                    if distances[grid[next_row][next_col]] == bound:
                        heapq.heappush(min_heap, (max(cur_cost, grid[next_row][next_col]), next_row, next_col))
        return distances[grid[n - 1][m - 1]]

# C++ O((NM)log(NM)) O(NM) Shortest Path Dijkstra Priority Queue
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        std::unordered_map<int, int> distances;
        int n = grid.size();
        int m  = grid[0].size();
        int bound = 50 * 50 + 1;
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < m; ++col) {
                distances[grid[row][col]] = bound;
            }
        }
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, std::greater<std::vector<int>>> minHeap;
        minHeap.push({grid[0][0], 0, 0});
        std::vector<std::pair<int, int>> moves = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (minHeap.size()) {
            int curCost = minHeap.top()[0];
            int curRow = minHeap.top()[1];
            int curCol = minHeap.top()[2];
            minHeap.pop();
            if (distances[grid[curRow][curCol]] != bound) {
                continue;
            }
            distances[grid[curRow][curCol]] = curCost;
            for (std::pair<int, int>& move : moves) {
                int nextRow = curRow + move.first;
                int nextCol = curCol + move.second;
                if (std::min(nextRow, nextCol) >= 0 && nextRow < n && nextCol < m) {
                    if (distances[grid[nextRow][nextCol]] == bound) {
                        minHeap.push({std::max(curCost, grid[nextRow][nextCol]), nextRow, nextCol});
                    }
                }
            }
        }
        return distances[grid[n - 1][m - 1]];
    }
};