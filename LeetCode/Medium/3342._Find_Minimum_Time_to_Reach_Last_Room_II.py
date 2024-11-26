# There is a dungeon with n x m rooms arranged as a grid.
#
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.
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
# Output: 7
#
# Explanation:
#
# The minimum time required is 7 seconds.
#
# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
# Example 2:
#
# Input: moveTime = [[0,0,0,0],[0,0,0,0]]
#
# Output: 6
#
# Explanation:
#
# The minimum time required is 6 seconds.
#
# At time t == 0, move from room (0, 0) to room (1, 0) in one second.
# At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
# At time t == 3, move from room (1, 1) to room (1, 2) in one second.
# At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
# Example 3:
#
# Input: moveTime = [[0,1],[1,2]]
#
# Output: 4
#
#
#
# Constraints:
#
# 2 <= n == moveTime.length <= 750
# 2 <= m == moveTime[i].length <= 750
# 0 <= moveTime[i][j] <= 109
# Solution
# Python O(ElogE) O(ElogE) Dijkstra
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        pq: list[tuple[int]] = [(0, 0, 0, 0)]
        min_time: list[list[int]] = [[float('inf')] * n for _ in range(m)]
        min_time[0][0] = 0
        directions: list[tuple[int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while pq:
            curr_time, r, c, is_extra = heapq.heappop(pq)
            if r == m - 1 and c == n - 1:
                return max(curr_time, moveTime[r][c])

            if curr_time > min_time[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_time = max(curr_time, moveTime[nr][nc]) + [1, 2][is_extra]
                    if next_time < min_time[nr][nc]:
                        min_time[nr][nc] = next_time
                        heapq.heappush(pq, (next_time, nr, nc, ~is_extra))
        return -1

# C++ O(ElogE) O(ElogE) Dijkstra
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int m = moveTime.size();
        int n = moveTime[0].size();
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, std::greater<std::vector<int>>> pq;
        pq.push({0, 0, 0, 0});
        std::vector<std::vector<int>> minTime(m, std::vector<int>(n, 1100000000));
        std::vector<std::pair<int, int>> directions = {
            {0, 1}, {0, -1}, {1, 0}, {-1, 0}
        };
        while (pq.size()) {
            int currentTime = pq.top()[0];
            int currentRow = pq.top()[1];
            int currentCol = pq.top()[2];
            bool isExtra = pq.top()[3];
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
                    int nextTime = std::max(currentTime, moveTime[nextRow][nextCol]) + (isExtra? 2 : 1);
                    pq.push({nextTime, nextRow, nextCol, !isExtra});
                }
            }
        }
        return -1;
    }
};