# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
#
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.
#
# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
#
# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
#
# Return the minimum cost to make the grid have at least one valid path.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.
# Example 2:
#
#
# Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).
# Example 3:
#
#
# Input: grid = [[1,2],[4,3]]
# Output: 1
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# 1 <= grid[i][j] <= 4
# Solution
# Python O(NM + ElogV) O(NM + ElogV) Graph Shortest Path Dijkstra
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        moves: tuple[tuple[int, int, int]] = (
            (0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)
        )
        min_heap: list[tuple[int, int, int]] = [(0, 0, 0)]
        seen: list[list[int]] = [[float('inf')] * m for row in range(n)]
        seen[0][0] = 0
        while min_heap:
            cur_cost, cur_row, cur_col = heapq.heappop(min_heap)
            if cur_row == n - 1 and cur_col == m - 1:
                return cur_cost

            for x, y, direction in moves:
                next_row, next_col = cur_row + x, cur_col + y
                weight: int = int(grid[cur_row][cur_col] != direction)
                if (
                        0 <= min(next_row, next_col)
                        and next_row < n and next_col < m
                        and (next_row, next_col) not in seen
                        and cur_cost + weight < seen[next_row][next_col]
                ):
                    heapq.heappush(min_heap, (cur_cost + weight, next_row, next_col))
                    seen[next_row][next_col] = cur_cost + weight

# C++ O(NM + ElogV) O(NM + ElogV) Graph Shortest Path Dijkstra
class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        std::vector<std::tuple<int, int, int>> moves {
            {0, 1, 1}, {0, -1, 2}, {1, 0, 3}, {-1, 0, 4}
        };
        int n = grid.size();
        int m =  grid[0].size();
        std::vector<std::vector<int>> seen (n, std::vector<int>(m, INT32_MAX));
        seen[0][0] = 0;
        std::priority_queue<
            std::tuple<int, int, int>,
            std::vector<std::tuple<int, int, int>>,
            std::greater<std::tuple<int, int, int>>
        > minHeap;
        minHeap.push({0, 0, 0});
        while (!minHeap.empty()) {
            auto [curCost, curRow, curCol] = minHeap.top();
            minHeap.pop();
            if (curRow == n - 1 && curCol == m - 1) return curCost;
            for (auto& move : moves) {
                auto [x, y, direction] = move;
                int nextRow = curRow + x;
                int nextCol = curCol + y;
                int weight = grid[curRow][curCol] != direction;
                if (
                    0 <= std::min(nextRow, nextCol)
                    && nextRow < n && nextCol < m
                    && curCost + weight < seen[nextRow][nextCol]
                ) {
                    minHeap.push(
                        {curCost + weight, nextRow, nextCol}
                    );
                    seen[nextRow][nextCol] = curCost + weight;
                }
            }
        }
        return -1;
    }
};