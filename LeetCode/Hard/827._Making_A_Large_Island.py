# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
#
# Return the size of the largest island in grid after applying this operation.
#
# An island is a 4-directionally connected group of 1s.
#
#
#
# Example 1:
#
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:
#
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:
#
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
#
# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.
# Solution
# Python O(NM) O(NM) Depth-First-Search Breadth-First-Search Matrix
class Solution:
    directions: list[tuple[int, int]] = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]

    def dfs(self, row: int, col: int, grid: list[list[int]], seen: list[list[bool]]) -> int:
        n: int = len(grid)
        seen[row][col] = True
        boundaries: list[tuple[int, int]] = []
        call_stack: list[tuple[int, int]] = [(row, col)]
        cur_area: int = 1
        while call_stack:
            row, col = call_stack.pop()
            for x, y in self.directions:
                next_row, next_col = row + x, col + y
                if (
                    (0 <= min(next_row, next_col))
                    and (max(next_row, next_col) < n)
                    and (not seen[next_row][next_col])
                ):
                    seen[next_row][next_col] = True
                    if not grid[next_row][next_col]:
                        boundaries.append((next_row, next_col))
                    else:
                        call_stack.append((next_row, next_col))
                        cur_area += 1
        max_area: int = cur_area
        for boundary in boundaries:
            extra_lands: int = 1
            local_seen: set[tuple[int, int]] = {boundary}
            cur_nodes: list[tuple[int, int]] = [boundary]
            next_nodes: list[tuple[int, int]] = []
            while cur_nodes:
                for cur_row, cur_col in cur_nodes:
                    for x, y in self.directions:
                        next_row, next_col = cur_row + x, cur_col + y
                        if (
                            (0 <= min(next_row, next_col))
                            and (max(next_row, next_col) < n)
                            and (not seen[next_row][next_col])
                            and ((next_row, next_col) not in local_seen)
                            and (grid[next_row][next_col])
                        ):
                            next_nodes.append((next_row, next_col))
                            extra_lands += 1
                            local_seen.add((next_row, next_col))
                cur_nodes = next_nodes
                next_nodes = []
            max_area = max(max_area, cur_area + extra_lands)
        return max_area

    def largestIsland(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        max_area: int = 1
        seen: list[list[bool]] = [[False] * n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                if not seen[row][col] and grid[row][col]:
                    max_area = max(max_area, self.dfs(row, col, grid, seen))
        return max_area

# C++ O(NM) O(NM) Depth-First-Search Breadth-First-Search Matrix
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
    std::vector<std::pair<int, int>> directions = {
        {0, 1}, {0, -1}, {1, 0}, {-1, 0}
    };

    int dfs(int& row, int& col, std::vector<std::vector<int>>& grid, std::vector<std::vector<bool>>& seen) {
        int n = grid.size();

        std::vector<std::vector<int>> boundaries;
        int curArea = 1;
        seen[row][col] = true;
        std::vector<std::pair<int, int>> callStack = {{row, col}};
        while (!callStack.empty()) {
            std::pair<int, int> cell = callStack.back();
            callStack.pop_back();
            for (std::pair<int, int>& move : directions) {
                int nextRow = cell.first + move.first;
                int nextCol = cell.second + move.second;
                if (
                    (0 <= std::min(nextRow, nextCol))
                    && (std::max(nextRow, nextCol) < n)
                    && (!seen[nextRow][nextCol])
                ) {
                    seen[nextRow][nextCol] = true;
                    if (!grid[nextRow][nextCol]) {
                        boundaries.push_back({nextRow, nextCol});
                    } else {
                        callStack.push_back({nextRow, nextCol});
                        ++curArea;
                    }
                }
            }
        }
        int maxConsecutiveArea = curArea;
        for (std::vector<int>& boundary : boundaries) {
            std::unordered_set<std::pair<int, int>, pair_hash, pair_equal> localSeen;
            localSeen.insert({boundary[0], boundary[1]});
            std::vector<std::pair<int, int>> curNodes = {{boundary[0], boundary[1]}};
            std::vector<std::pair<int, int>> nextNodes;
            int extraLands = 1;
            while (!curNodes.empty()) {
                for (std::pair<int, int>& curNode : curNodes) {
                    for (std::pair<int, int>& move : directions) {
                        int nextRow = curNode.first + move.first;
                        int nextCol = curNode.second + move.second;
                        if (
                            (0 <= std::min(nextRow, nextCol))
                            && (std::max(nextRow, nextCol) < n)
                            && (!seen[nextRow][nextCol])
                            && (!localSeen.count({nextRow, nextCol}))
                            && (grid[nextRow][nextCol])
                        ) {
                            ++extraLands;
                            localSeen.insert({nextRow, nextCol});
                            nextNodes.push_back({nextRow, nextCol});
                        }
                    }
                }
                curNodes = nextNodes;
                nextNodes = {};
            }
            maxConsecutiveArea = std::max(maxConsecutiveArea, curArea + extraLands);
        }
        return maxConsecutiveArea;
    }

    int largestIsland(vector<vector<int>>& grid) {
        int maxArea = 1;
        int n = grid.size();
        std::vector<std::vector<bool>> seen (n, std::vector<bool>(n, false));
        for (int row = 0; row < n; ++row) {
            for (int col = 0; col < n; ++col) {
                if (!seen[row][col] && grid[row][col]) {
                    maxArea = std::max(maxArea, dfs(row, col, grid, seen));
                }
            }
        }
        return maxArea;
    };
};