# You are given an m x n binary matrix grid and an integer health.
#
# You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).
#
# You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.
#
# Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.
#
# Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.
#
#
#
# Example 1:
#
# Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1
#
# Output: true
#
# Explanation:
#
# The final cell can be reached safely by walking along the gray cells below.
#
#
# Example 2:
#
# Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
#
# Output: false
#
# Explanation:
#
# A minimum of 4 health points is needed to reach the final cell safely.
#
#
# Example 3:
#
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5
#
# Output: true
#
# Explanation:
#
# The final cell can be reached safely by walking along the gray cells below.
#
#
#
# Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.
#
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 2 <= m * n
# 1 <= health <= m + n
# grid[i][j] is either 0 or 1.
# Solution Breadth-First-Search
# Python O(MN) O(MN)
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        stack: list[tuple[int, int, int]] = [(0, 0, health)]
        seen: set[tuple[int, int, int]] = set()
        while stack:
            row, col, points = stack.pop()
            if not (0 <= row < m) or not (0 <= col < n) or points <= 0: continue
            if row == m - 1 and col == n - 1 and points - grid[row][col] > 0: return True
            if (row, col, points) in seen: continue
            seen.add((row, col, points))
            next_points: int = points - grid[row][col]
            stack.append((row + 1, col, next_points))
            stack.append((row - 1, col, next_points))
            stack.append((row, col + 1, next_points))
            stack.append((row, col - 1, next_points))
        return False
# C++ O(MNH) O(MN)
#include <vector>
#include <set>
#include <stack>

class Solution {
public:
    bool findSafeWalk(std::vector<std::vector<int>>& grid, int health) {
        int m = grid.size();
        int n = grid[0].size();
        std::stack<std::vector<int>> stack;
        stack.push({0, 0, health});
        std::set<std::tuple<int, int, int>> seen;
        while (!stack.empty()) {
            int row = stack.top()[0];
            int col = stack.top()[1];
            int cur_points = stack.top()[2];
            stack.pop();
            if (row < 0 || row >= m || col < 0 || col >= n) {
                continue;
            }
            if (row == m - 1 && col == n - 1 && cur_points - grid[row][col] > 0) {
                return true;
            }
            if (seen.count({row, col, cur_points})) {
                continue;
            }
            seen.insert({row, col, cur_points});
            int next_points = cur_points - grid[row][col];
            if (next_points > 0) {
                stack.push({row + 1, col, next_points});
                stack.push({row - 1, col, next_points});
                stack.push({row, col + 1, next_points});
                stack.push({row, col - 1, next_points});
            }
        }
        return false;
    }
};


# Python O(NM) O(NM) BreadthFirstSearch
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n: int = len(grid)
        m: int = len(grid[0])
        moves: list[tuple[int, int]] = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]
        cost: list[list[int]] =[[-1] * m for _ in range(n)]
        cost[0][0] = health - grid[0][0]
        cur_nodes: list[tuple[int, int]] = [(0, cost[0][0])]
        next_nodes: list[tuple[int, int]] = []
        while cur_nodes:
            for cell, points in cur_nodes:
                i: int = cell // m
                j: int = cell % m
                for x, y in moves:
                    ni: int = i + x
                    nj: int = j + y
                    if not (0 <= ni < n) or not (0 <= nj < m): continue
                    new_points: int = points - grid[ni][nj]
                    if new_points <= cost[ni][nj]: continue
                    cost[ni][nj] = new_points
                    next_nodes.append((ni * m + nj, new_points))
            cur_nodes = next_nodes.copy()
            next_nodes.clear()
        return cost[n - 1][m - 1] >= 1

# C++ O(NM) O(NM) BreadthFirstSearch
class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<std::pair<int, int>> moves = {
            {0, 1}, {0, -1}, {1, 0}, {-1, 0}
        };
        std::vector<std::vector<int>> cost(n, std::vector<int>(m, -1));
        std::vector<std::pair<int, int>> curNodes = {{0, (grid[0][0] ? health - 1 : health)}}, nextNodes;
        cost[0][0] = (grid[0][0] ? health - 1 : health);
        while (!curNodes.empty()) {
            for (auto [cell, points] : curNodes) {
                int i = cell / m, j = cell % m;
                for (auto [x, y] : moves) {
                    int ni = i + x, nj = j + y;
                    if (!(ni >= 0 && ni < n) || !(nj >= 0 && nj < m)) continue;
                    int newPoints = (grid[ni][nj] ? points - 1 : points);
                    if (newPoints < 1 || newPoints <= cost[ni][nj]) continue;
                    cost[ni][nj] = newPoints;
                    nextNodes.push_back({ni * m + nj, newPoints});
                }
            }
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return cost[n - 1][m - 1] >= 1;
    }
};