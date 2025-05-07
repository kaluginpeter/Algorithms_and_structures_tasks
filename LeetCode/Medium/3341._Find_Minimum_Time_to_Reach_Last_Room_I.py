# There is a dungeon with n x m rooms arranged as a grid.
#
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
#
# Return the minimum time to reach the room (n - 1, m - 1).
#
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.
#
#
#
# Example 1:
#
# Input: moveTime = [[0,4],[4,4]]
#
# Output: 6
#
# Explanation:
#
# The minimum time required is 6 seconds.
#
# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in one second.
# Example 2:
#
# Input: moveTime = [[0,0,0],[0,0,0]]
#
# Output: 3
#
# Explanation:
#
# The minimum time required is 3 seconds.
#
# At time t == 0, move from room (0, 0) to room (1, 0) in one second.
# At time t == 1, move from room (1, 0) to room (1, 1) in one second.
# At time t == 2, move from room (1, 1) to room (1, 2) in one second.
# Example 3:
#
# Input: moveTime = [[0,1],[1,2]]
#
# Output: 3
#
#
#
# Constraints:
#
# 2 <= n == moveTime.length <= 50
# 2 <= m == moveTime[i].length <= 50
# 0 <= moveTime[i][j] <= 109
# Solution
# Python O(ElogE) O(ElogE) Dijkstra
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        pq: list[tuple[int]] = [(0, 0, 0)]
        min_time: list[list[int]] = [[float('inf')] * n for _ in range(m)]
        min_time[0][0] = 0
        directions: list[tuple[int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while pq:
            curr_time, r, c = heapq.heappop(pq)
            if r == m - 1 and c == n - 1:
                return max(curr_time, moveTime[r][c])

            if curr_time > min_time[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_time = max(curr_time, moveTime[nr][nc]) + 1
                    if next_time < min_time[nr][nc]:
                        min_time[nr][nc] = next_time
                        heapq.heappush(pq, (next_time, nr, nc))
        return -1

# C++ O(ElogE) O(ElogE) Dijkstra
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int m = moveTime.size();
        int n = moveTime[0].size();
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, std::greater<std::vector<int>>> pq;
        pq.push({0, 0, 0});
        std::vector<std::vector<int>> minTime(m, std::vector<int>(n, 1100000000));
        std::vector<std::pair<int, int>> directions = {
            {0, 1}, {0, -1}, {1, 0}, {-1, 0}
        };
        while (pq.size()) {
            int currentTime = pq.top()[0];
            int currentRow = pq.top()[1];
            int currentCol = pq.top()[2];
            pq.pop();
            if (currentRow == m - 1 && currentCol == n - 1) {
                return std::max(currentTime, moveTime[m - 1][n - 1]);
            }
            if (currentTime >= minTime[currentRow][currentCol]) {
                continue;
            }
            minTime[currentRow][currentCol] = currentTime;
            for (std::pair<int, int> direction : directions) {
                int nextRow = currentRow + direction.first;
                int nextCol = currentCol + direction.second;
                if (0 <= std::min(nextRow, nextCol) && nextRow < m && nextCol < n) {
                    int nextTime = std::max(currentTime, moveTime[nextRow][nextCol]) + 1;
                    pq.push({nextTime, nextRow, nextCol});
                }
            }
        }
        return -1;
    }
};


# Python O(NM + ElogV) O(NM + E) Dijkstra Matrix ShortestPath Graph PriorityQueue
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n: int = len(moveTime)
        m: int = len(moveTime[0])
        min_heap: list[tuple[int, tuple[int, int]]] = [(0, (0, 0))]
        seen: list[list[bool]] = [[False] * m for _ in range(n)]
        cost: list[list[int]] = [[float('inf')] * m for _ in range(n)]
        seen[0][0] = True
        cost[0][0] = 0
        moves: list[tuple[int, int]] = [
            (-1, 0), (0, 1), (1, 0), (0, -1)
        ]
        while min_heap:
            cell: tuple[int, int] = min_heap[0][1]
            time: int = min_heap[0][0]
            heapq.heappop(min_heap)
            if cell == (n - 1, m - 1): return time
            for x, y in moves:
                next_row, next_col = cell[0] + x, cell[1] + y
                if not (0 <= next_row < n) or not (0 <= next_col < m): continue
                next_time: int = max(time, moveTime[next_row][next_col]) + 1
                if not seen[next_row][next_col] or next_time < cost[next_row][next_col]:
                    seen[next_row][next_col] = True
                    cost[next_row][next_col] = next_time
                    heapq.heappush(min_heap, (next_time, (next_row, next_col)))
        return -1

# C++ O(NM + ElogV) O(NM + E) Dijkstra ShortestPath Matrix PriorityQueue Graph
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size(), m = moveTime[0].size();
        priority_queue<tuple<int, pair<int, int>>, vector<tuple<int, pair<int, int>>>, greater<tuple<int, pair<int, int>>>> minHeap;
        vector<pair<int, int>> moves = {
            {-1, 0}, {0, 1}, {1, 0}, {0, -1}
        };
        vector<vector<bool>> seen (n, vector<bool>(m, false));
        vector<vector<int>> cost(n, vector<int>(m, INT32_MAX));
        cost[0][0] = 0;
        seen[0][0] = true;
        minHeap.push({0, {0, 0}});
        while (!minHeap.empty()) {
            pair<int, int> cell = get<1>(minHeap.top());
            int time = get<0>(minHeap.top());
            minHeap.pop();
            if (cell.first == n - 1 && cell.second == m - 1) return time;
            for (const pair<int, int> &move : moves) {
                int nextRow = cell.first + move.first;
                int nextCol = cell.second + move.second;
                if (nextRow < 0 || nextRow == n || nextCol < 0 || nextCol == m) continue;
                int nextTime = max(time, moveTime[nextRow][nextCol]) + 1;
                if (!seen[nextRow][nextCol] || nextTime < cost[nextRow][nextCol]) {
                    minHeap.push({nextTime, {nextRow, nextCol}});
                    seen[nextRow][nextCol] = true;
                    cost[nextRow][nextCol] = nextTime;
                }
            }
        }
        return -1;
    }
};