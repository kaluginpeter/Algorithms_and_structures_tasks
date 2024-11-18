# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
#
#
#
# Example 1:
#
#
#
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
# Example 2:
#
#
#
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:
#
#
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
#
#
# Constraints:
#
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106
# Solution
# Python O((NM)log(NM)) O(NM) Shortest Path Dijkstra Matrix Priority Queue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        distances: dict[tuple[int, int], int] = dict()
        n: int = len(heights)
        m: int = len(heights[0])
        bound: int = 10**6 * 100 + 1
        for row in range(n):
            for col in range(m):
                distances[(row, col)] = bound
        moves: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap: list[tuple[int, int, int]] = [(0, 0, 0)]
        while min_heap:
            cur_effort, cur_row, cur_col = heapq.heappop(min_heap)
            if distances[(cur_row, cur_col)] != bound:
                continue
            if cur_row == n - 1 and cur_col == m - 1:
                return cur_effort
            distances[(cur_row, cur_col)] = cur_effort
            for move in moves:
                next_row: int = cur_row + move[0]
                next_col: int = cur_col + move[1]
                if min(next_row, next_col) >= 0 and next_row < n and next_col < m:
                    if distances[(next_row, next_col)] == bound:
                        diff: int = abs(heights[next_row][next_col] - heights[cur_row][cur_col])
                        heapq.heappush(min_heap, (max(cur_effort, diff), next_row, next_col))
        return -1

# C++ O((NM)log(NM)) O(NM) Sortest Path Dijkstra Matrix Priority Queue
struct pair_hash {
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2>& pair) const {
        auto hash1 = std::hash<T1>{}(pair.first);
        auto hash2 = std::hash<T2>{}(pair.second);
        return hash1 ^ hash2;
    }
};

struct pair_equal {
    template <class T1, class T2>
    bool operator() (const std::pair<T1, T2>& lhs, const std::pair<T1, T2>& rhs) const {
        return lhs.first == rhs.first && lhs.second == rhs.second;
    }
};
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        std::unordered_map<std::pair<int, int>, int, pair_hash, pair_equal> distances;
        int n = heights.size();
        int m = heights[0].size();
        int bound = 1000000 * 100 + 1;
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < m; ++col) {
                distances[{row, col}] = bound;
            }
        }
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, std::greater<std::vector<int>>> minHeap;
        minHeap.push({0, 0, 0});
        std::vector<std::pair<int, int>> moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (minHeap.size()) {
            int curEffort = minHeap.top()[0];
            int curRow = minHeap.top()[1];
            int curCol = minHeap.top()[2];
            minHeap.pop();
            if (distances[{curRow, curCol}] != bound) {
                continue;
            }
            if (curRow == n - 1 && curCol == m - 1) {
                return curEffort;
            }
            distances[{curRow, curCol}] = curEffort;
            for (std::pair<int, int>& move : moves) {
                int nextRow = curRow + move.first;
                int nextCol = curCol + move.second;
                if (std::min(nextRow, nextCol) >= 0 && nextRow < n && nextCol < m) {
                    if (distances[{nextRow, nextCol}] == bound) {
                        int diff = std::abs(heights[nextRow][nextCol] - heights[curRow][curCol]);
                        minHeap.push({std::max(curEffort, diff), nextRow, nextCol});
                    }
                }
            }
        }
        return distances[{n - 1, m - 1}];
    }
};
