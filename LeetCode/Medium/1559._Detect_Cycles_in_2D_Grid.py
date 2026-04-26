# Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.
#
# A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.
#
# Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.
#
# Return true if any cycle of the same value exists in grid, otherwise, return false.
#
#
#
# Example 1:
#
#
#
# Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the image below:
#
# Example 2:
#
#
#
# Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:
#
# Example 3:
#
#
#
# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid consists only of lowercase English letters.
# Solution
# Python O(NM) O(NM) Matrix Depth-First-Search
class Solution:
    moves: list[tuple[int, int]] = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]
    def check(self, start: int, n: int, m: int, grid: list[list[str]], seen: list[list[bool]]) -> bool:
        st: list[tuple[int, int]] = []
        st.append((start // m, start % m, float('inf')))
        while st:
            i, j, parent = st.pop()
            if not seen[i][j]: seen[i][j] = True
            for dx, dy in self.moves:
                ni: int = i + dx
                nj: int = j + dy
                if not (0 <= ni < n) or not (0 <= nj < m): continue
                if grid[ni][nj] != grid[i][j]: continue
                if ni * m + nj == parent: continue
                if seen[ni][nj]: return True
                st.append((ni, nj, i * m + j))
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        n: int = len(grid)
        m: int = len(grid[0])
        seen: list[list[bool]] = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if seen[i][j]: continue
                if self.check(i * m + j, n, m, grid, seen): return True
        return False

# C++ O(NM) O(NM) Depth-First-Search Matrix
class Solution {
    const std::vector<std::pair<int, int>> moves = {
        {1, 0}, {-1, 0}, {0, 1}, {0, -1}
    };
public:
    bool check(size_t start, const size_t& n, const size_t& m,
        const vector<vector<char>>& grid,
        vector<vector<bool>>& seen
    ) {
        std::vector<std::tuple<size_t,size_t,size_t>> st;
        st.push_back({start / m, start % m, SIZE_MAX});
        while (!st.empty()) {
            auto [i, j, parent] = st.back();
            st.pop_back();
            if (!seen[i][j]) seen[i][j] = true;
            for (auto [dx, dy] : moves) {
                size_t ni = i + dx;
                size_t nj = j + dy;
                if (ni >= n || nj >= m) continue;
                if (grid[ni][nj] != grid[i][j]) continue;
                if (ni * m + nj == parent) continue;
                if (seen[ni][nj]) return true;
                st.push_back({ni, nj, i * m + j});
            }
        }
        return false;
    };

    bool containsCycle(vector<vector<char>>& grid) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<std::vector<bool>> seen(n, std::vector<bool>(m, false));
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                if (seen[i][j]) continue;
                if (check(i * m + j, n, m, grid, seen)) return true;
            }
        }
        return false;
    }
};