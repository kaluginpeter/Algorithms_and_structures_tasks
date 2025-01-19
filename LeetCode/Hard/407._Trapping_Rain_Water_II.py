# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
#
#
#
# Example 1:
#
#
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.
# Example 2:
#
#
# Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
#
#
# Constraints:
#
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 104
# Solution
# Python O( (MN)log(MN) ) O(MN) Matrix Breadth-First-Search PriorityQueue
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n: int = len(heightMap)
        m: int = len(heightMap[0])
        min_heap: list[tuple[int, int, int]] = []
        seen: list[list[bool]] = [[False] * m for row in range(n)]
        for row in range(n):
            for col in range(m):
                if (row == 0 or row == n -1) or (col == 0 or col == m - 1):
                    heapq.heappush(min_heap, (heightMap[row][col], row, col))
                    seen[row][col] = True
        moves: tuple[tuple[int, int]] = (
            (1, 0), (-1, 0), (0, 1), (0, -1)
        )
        total_volume: int = 0
        max_height: int = 0
        while min_heap:
            height, row, col = heapq.heappop(min_heap)
            max_height = max(max_height, height)
            total_volume += max_height - height
            for x, y in moves:
                next_row, next_col = row + x, col + y
                if (
                    (0 <= min(next_row, next_col))
                    and (next_row < n and next_col < m)
                    and (not seen[next_row][next_col])
                ):
                    heapq.heappush(min_heap, (heightMap[next_row][next_col], next_row, next_col))
                    seen[next_row][next_col] = True
        return total_volume

# C++ O( (MN)log(MN) ) O(MN) Matrix, Breadth-First-Search PriorityQueue
class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        int n = heightMap.size();
        int m = heightMap[0].size();
        std::vector<std::vector<bool>> seen (n, std::vector<bool>(m, false));
        std::priority_queue<
            std::tuple<int, int, int>,
            std::vector<std::tuple<int, int, int>>,
            std::greater<std::tuple<int, int, int>>
        > minHeap;
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < m; ++col) {
                if (
                    (row == 0 || row == n - 1)
                    || (col == 0 || col == m - 1)
                ) {
                    minHeap.push({heightMap[row][col], row, col});
                    seen[row][col] = true;
                }
            }
        }
        std::vector<std::tuple<int, int>> moves = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };
        int totalVolume = 0;
        int maxHeight = 0;
        while (minHeap.size()) {
            int height = std::get<0>(minHeap.top());
            int row = std::get<1>(minHeap.top());
            int col = std::get<2>(minHeap.top());
            minHeap.pop();
            maxHeight = std::max(maxHeight, height);
            totalVolume += maxHeight - height;
            for (std::tuple<int, int>& move : moves) {
                int nextRow = row + std::get<0>(move);
                int nextCol = col + std::get<1>(move);
                if (
                    (0 <= std::min(nextRow, nextCol))
                    && (nextRow < n && nextCol < m)
                    && (!seen[nextRow][nextCol])
                ) {
                    minHeap.push({heightMap[nextRow][nextCol], nextRow, nextCol});
                    seen[nextRow][nextCol] = true;
                }
            }
        }
        return totalVolume;
    }
};