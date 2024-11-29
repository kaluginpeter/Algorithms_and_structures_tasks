# You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].
#
# You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.
#
# Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.
#
#
#
# Example 1:
#
#
#
# Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
# Output: 7
# Explanation: One of the paths that we can take is the following:
# - at t = 0, we are on the cell (0,0).
# - at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
# - at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
# - at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
# - at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
# - at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
# - at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
# - at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
# The final time is 7. It can be shown that it is the minimum time possible.
# Example 2:
#
#
#
# Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
# Output: -1
# Explanation: There is no path from the top left to the bottom-right cell.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# 0 <= grid[i][j] <= 105
# grid[0][0] == 0
#
# Solution
# Python O(ElogE) O(ElogE) Matrix Shortest Path Dijkstra
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        min_heap: list[tuple[int, int, int]] = [(0, 0, 0)]
        seen: set[tuple[int, int]] = set()
        seen.add((0, 0, 0))
        moves: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        have_move: bool = False
        while min_heap:
            cur_time, cur_row, cur_col = heapq.heappop(min_heap)
            if cur_row == m - 1 and cur_col == n - 1:
                return cur_time
            for move in moves:
                next_row, next_col = cur_row + move[0], cur_col + move[1]
                if 0 <= min(next_row, next_col) and next_row < m and next_col < n:
                    if cur_time + 1 < grid[next_row][next_col] and not have_move:
                        continue
                    if (next_row, next_col) in seen:
                        continue
                    next_time: int = 0
                    if cur_time >= grid[next_row][next_col]:
                        next_time = cur_time + 1
                    else:
                        diff: int = grid[next_row][next_col] - cur_time
                        next_time = grid[next_row][next_col] + (0 if diff & 1 else 1)
                    have_move = True
                    seen.add((next_row, next_col))
                    heapq.heappush(min_heap, (next_time, next_row, next_col))
        return -1

# C++ O(ElogE) O(ElogE) Matrix Shortest Path Dijkstra
class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        std::priority_queue<std::tuple<int, int, int>, std::vector<std::tuple<int, int, int>>, std::greater<std::tuple<int, int, int>>> minHeap;
        minHeap.push({0, 0, 0});
        int m = grid.size();
        int n = grid[0].size();
        std::vector<std::vector<int>> minTime(m, std::vector<int>(n, 100000000));
        std::vector<std::pair<int, int>> moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        bool haveMove = false;
        while (minHeap.size()) {
            auto [curTime, curRow, curCol] = minHeap.top();
            minHeap.pop();
            if (curRow == m - 1 && curCol == n - 1) {
                return curTime;
            }
            for (std::pair<int, int> move : moves) {
                int nextRow = curRow + move.first;
                int nextCol = curCol + move.second;
                if (
                    0 <= std::min(nextRow, nextCol)
                    && nextRow < m && nextCol < n
                ) {
                    if (curTime + 1 < grid[nextRow][nextCol] && !haveMove) {
                        continue;
                    }
                    int nextTime = 0;
                    if (curTime >= grid[nextRow][nextCol]) {
                        nextTime = curTime + 1;
                    } else {
                        int diff = grid[nextRow][nextCol] - curTime;
                        nextTime = (diff % 2? grid[nextRow][nextCol] : grid[nextRow][nextCol] + 1);
                    }
                    if (nextTime < minTime[nextRow][nextCol]) {
                        minTime[nextRow][nextCol] = nextTime;
                        haveMove = true;
                        minHeap.push({nextTime, nextRow, nextCol});
                    }

                }
            }
        }
        return -1;
    }
};