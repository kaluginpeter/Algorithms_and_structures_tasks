# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
#
#
#
# Example 1:
#
#
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:
#
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
#
#
# Constraints:
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105
# Solution
# Python O(NM) O(NM) Breadth-First-Search Matrix
class Solution:
    moves: list[tuple[int, int]] = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]
    def bfs(self, dataset: list[tuple[int, int]], visited: list[list[bool]], heights: list[list[int]]) -> None:
        while dataset:
            i, j = dataset.pop()
            for x, y in self.moves:
                ni, nj = i + x, j + y
                if not (0 <= ni < len(heights)) or not (0 <= nj < len(heights[0])) or visited[ni][nj]:
                    continue
                elif heights[i][j] > heights[ni][nj]: continue
                visited[ni][nj] = True
                dataset.append((ni, nj))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n: int = len(heights)
        m: int = len(heights[0])
        q1: list[tuple[int, int]] = []
        q2: list[tuple[int, int]] = []
        atlantic: list[list[bool]] = [[False] * m for _ in range(n)]
        pacific: list[list[bool]] = [[False] * m for _ in range(n)]
        for i in range(n):
            q1.append((i, 0))
            q2.append((i, m - 1))
            pacific[i][0] = atlantic[i][m - 1] = True
        for j in range(m):
            q1.append((0, j))
            q2.append((n - 1, j))
            pacific[0][j] = atlantic[n - 1][j] = True
        self.bfs(q1, pacific, heights)
        self.bfs(q2, atlantic, heights)
        output: list[list[int]] = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]: output.append([i, j])
        return output

# C++ O(NM) O(NM) Matrix Breadth-First-Search
class Solution {
private:
    std::vector<std::pair<int,int>> moves = {{1,0},{-1,0},{0,1},{0,-1}};
    void bfs(std::queue<std::pair<int,int>>& q, std::vector<std::vector<int>>& visited, std::vector<std::vector<int>>& heights) {
        int n = heights.size(), m = heights[0].size();
        while (!q.empty()) {
            auto [i, j] = q.front();
            q.pop();
            for (auto [dx, dy] : moves) {
                int x = i + dx, y = j + dy;
                if (x < 0 || y < 0 || x >= n || y >= m || visited[x][y]) continue;
                if (heights[x][y] < heights[i][j]) continue;
                visited[x][y] = 1;
                q.push({x, y});
            }
        }
    }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int n = heights.size(), m = heights[0].size();
        std::vector<std::vector<int>> pacific(n, vector<int>(m, 0)), atlantic(n, vector<int>(m, 0));
        std::queue<std::pair<int,int>> q1, q2;
        for (int i = 0; i < n; ++i) {
            q1.push({i, 0});
            q2.push({i, m - 1});
            pacific[i][0] = atlantic[i][m - 1] = 1;
        }
        for (int j = 0; j < m; ++j) {
            q1.push({0, j});
            q2.push({n - 1, j});
            pacific[0][j] = atlantic[n - 1][j] = 1;
        }
        bfs(q1, pacific, heights);
        bfs(q2, atlantic, heights);
        std::vector<std::vector<int>> output;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (pacific[i][j] && atlantic[i][j]) output.push_back({i, j});
            }
        }
        return output;
    }
};