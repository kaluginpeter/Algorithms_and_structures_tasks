# You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.
#
# A V-shaped diagonal segment is defined as:
#
# The segment starts with 1.
# The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
# The segment:
# Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
# Continues the sequence in the same diagonal direction.
# Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.
#
#
# Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.
#
#
#
# Example 1:
#
# Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
#
# Output: 5
#
# Explanation:
#
#
#
# The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).
#
# Example 2:
#
# Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
#
# Output: 4
#
# Explanation:
#
#
#
# The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).
#
# Example 3:
#
# Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
#
# Output: 5
#
# Explanation:
#
#
#
# The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).
#
# Example 4:
#
# Input: grid = [[1]]
#
# Output: 1
#
# Explanation:
#
# The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).
#
#
#
# Constraints:
#
# n == grid.length
# m == grid[i].length
# 1 <= n, m <= 500
# grid[i][j] is either 0, 1 or 2.
#
# Solution
# Python O(NM) O(NM) Depth-First-Search Matrix Memoization
class Solution:
    def dfs(self, cx: int, cy: int, direction: int, turn: bool, target: int, dirs: list[tuple[int, int]], memo: list[list[list[list[int]]]], grid: list[list[int]], n: int, m: int) -> int:
        nx: int = cx + dirs[direction][0]
        ny: int = cy + dirs[direction][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or grid[nx][ny] != target: return 0
        elif memo[nx][ny][direction][turn] != -1: return memo[nx][ny][direction][turn]
        max_step: int = self.dfs(nx, ny, direction, turn, 2 - target, dirs, memo, grid, n, m)
        if turn:
            max_step = max(max_step, self.dfs(nx, ny, (direction + 1) % 4, False, 2 - target, dirs, memo, grid, n, m))
        max_step += 1
        memo[nx][ny][direction][turn] = max_step
        return max_step

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        dirs: list[tuple[int, int]] = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        memo: list[list[list[list[int]]]] = [[[[-1] * 2 for _ in range(4)] for _ in range(m)] for _ in range(n)]
        output: int = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1: continue
                for direction in range(4):
                    output = max(output, self.dfs(i, j, direction, True, 2, dirs, memo, grid, n, m) + 1)
        return output

# C++ O(NM) O(NM) Depth-First-Search Matrix Memoization
using a2i = std::array<int, 2>;
using a4a2i = std::array<a2i, 4>;
using a501a501a4a2i = std::array<std::array<a4a2i, 501>, 501>;

class Solution {
public:
    int dfs(int cx, int cy, int direction, bool turn, int target, const a4a2i &dirs, a501a501a4a2i &memo, const std::vector<std::vector<int>> &grid, const int &n, const int &m) {
        int nx = cx + dirs[direction][0];
        int ny = cy + dirs[direction][1];
        if (nx < 0 || ny < 0 || nx >= n || ny >= m || grid[nx][ny] != target) return 0;
        if (memo[nx][ny][direction][turn] != -1) return memo[nx][ny][direction][turn];
        int maxStep = dfs(nx, ny, direction, turn, 2 - target, dirs, memo, grid, n, m);
        if (turn) {
            maxStep = std::max(maxStep, dfs(nx, ny, (direction + 1) % 4, false, 2 - target, dirs, memo, grid, n, m));
        }
        ++maxStep;
        memo[nx][ny][direction][turn] = maxStep;
        return maxStep;
    };

    int lenOfVDiagonal(std::vector<std::vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        a4a2i dirs = {a2i{1, 1}, a2i{1, -1}, a2i{-1, -1}, a2i{-1, 1}};
        a501a501a4a2i memo = {};
        for (auto &a : memo)
            for (auto &b : a)
                for (auto &c : b)
                    c.fill(-1);
        int output = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    for (int direction = 0; direction < 4; ++direction) {
                        output = std::max(output, dfs(i, j, direction, true, 2, dirs, memo, grid, n, m) + 1);
                    }
                }
            }
        }
        return output;
    }
};