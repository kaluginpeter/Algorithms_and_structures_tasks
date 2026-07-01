# You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
#
# A cell containing a thief if grid[r][c] = 1
# An empty cell if grid[r][c] = 0
# You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.
#
# The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.
#
# Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).
#
# An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.
#
# The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
# Output: 0
# Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
# Example 2:
#
#
# Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.
# Example 3:
#
#
# Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# Output: 2
# Explanation: The path depicted in the picture above has a safeness factor of 2 since:
# - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
# - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
# It can be shown that there are no other paths with a higher safeness factor.
#
#
# Constraints:
#
# 1 <= grid.length == n <= 400
# grid[i].length == n
# grid[i][j] is either 0 or 1.
# There is at least one thief in the grid.
# Solution
# C++ O(N^2logN) O(N^2) MaxHeap Dijkstra Matrix
class Solution {
private:
    const std::vector<std::pair<int, int>> moves {
        {-1, 0}, {0, -1}, {1, 0}, {0, 1}
    };
public:
    void bfs(const std::vector<std::vector<int>>& grid, std::vector<std::vector<int>>& dist, size_t n) {
        std::queue<std::pair<int, int>> q;
        // All thieves are sources.
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < n; ++j) {
                if (!grid[i][j]) continue;
                dist[i][j] = 0;
                q.push({static_cast<int>(i), static_cast<int>(j)});
            }
        }
        while (!q.empty()) {
            auto [i, j] = q.front();
            q.pop();
            for (auto [x, y] : moves) {
                int ni = i + x;
                int nj = j + y;
                if (ni < 0 || ni >= static_cast<int>(n) ||
                    nj < 0 || nj >= static_cast<int>(n))
                    continue;
                if (dist[ni][nj] != INT32_MAX) continue;
                dist[ni][nj] = dist[i][j] + 1;
                q.push({ni, nj});
            }
        }
    }
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        size_t n = grid.size();
        std::vector<std::vector<int>> cost(n, std::vector<int>(n, 0));
        std::vector<std::vector<int>> dist(n, std::vector<int>(n, INT32_MAX));
        // Precalculate minimum distance to each cell
        bfs(grid, dist, n);
        // Simulate path processing
        std::priority_queue<
            std::pair<int, int>,
            std::vector<std::pair<int, int>>
        > maxHeap;
        cost[0][0] = dist[0][0];
        maxHeap.push({dist[0][0], 0});
        while (!maxHeap.empty()) {
            auto [bound, curCell] = maxHeap.top();
            maxHeap.pop();
            int i = curCell / n, j = curCell % n;
            if (bound < cost[i][j]) continue; // don't need to make a move
            for (auto& [x, y] : moves) {
                int ni = i + x, nj = j + y;
                if (!(ni >= 0 && ni < n) || !(nj >= 0 && nj < n)) continue;
                int newBound = std::min(bound, dist[ni][nj]);
                if (newBound <= cost[ni][nj]) continue;
                cost[ni][nj] = newBound;
                maxHeap.push({newBound, ni * n + nj});
            }
        }
        return cost[n - 1][n - 1];
    }
};

# Python O(N^2logN) O(N^2) Matrix BinarySearch DepthFirstSearch
from collections import deque

moves: tuple[tuple[int, int], ...] = (
    (-1, 0), (0, 1), (1, 0), (0, -1)
)


class Solution:
    def bfs(self, grid: List[List[int]], dist: list[list[int]], n: int) -> None:
        queue: deque[tuple[int, int]] = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j] = 0
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for x, y in moves:
                ni: int = i + x
                nj: int = j + y
                if not (0 <= ni < n) or not (0 <= nj < n): continue
                if dist[ni][nj] != float("inf"): continue
                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni, nj))

    def check(self, bound: int, dist: list[list[int]], n: int) -> bool:
        if dist[0][0] < bound: return False

        seen: list[list[bool]] = [[False] * n for _ in range(n)]
        seen[0][0] = True
        cur_nodes: list[int] = [0]
        while cur_nodes:
            cell: int = cur_nodes.pop()
            i: int = cell // n
            j: int = cell % n
            if (i == n - 1) and (j == n - 1): return True
            for x, y in moves:
                ni: int = i + x
                nj: int = j + y
                if not (0 <= ni < n) or not (0 <= nj < n): continue
                if seen[ni][nj]: continue
                if dist[ni][nj] < bound: continue
                seen[ni][nj] = True
                cur_nodes.append(ni * n + nj)
        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        dist: list[list[int]] = [[float("inf")] * n for _ in range(n)]
        self.bfs(grid, dist, n)
        left: int = 0
        right: int = dist[0][0]
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if self.check(middle, dist, n): left = middle + 1
            else: right = middle - 1
        return right