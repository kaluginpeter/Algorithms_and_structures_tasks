# You are given an m x n integer matrix grid and an array queries of size k.
#
# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:
#
# If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
#
# Return the resulting array answer.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# Output: [5,8,1]
# Explanation: The diagrams above show which cells we visit to get points for each query.
# Example 2:
#
#
# Input: grid = [[5,2,1],[1,1,2]], queries = [3]
# Output: [0]
# Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 1000
# 4 <= m * n <= 105
# k == queries.length
# 1 <= k <= 104
# 1 <= grid[i][j], queries[i] <= 106
# Solution
# Python O(QlogQ + NM) O(Q + NM) Breadth-First-Search Memoization Matrix
class Solution:
    moves: list[tuple[int, int]] = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]

    def get_path(self, bound: int, grid: list[list[int]], seen: list[list[bool]], last: list[tuple[int, int]]) -> int:
        n, m = len(grid), len(grid[0])
        cells: int = 0
        q: list[tuple[int, int]] = []
        i, k = 0, len(last) - 1
        while i <= k:
            if grid[last[i][0]][last[i][1]] < bound:
                q.append(last[i])
                last[i] = last[k]
                last.pop()
                k -= 1
                cells += 1
            else: i += 1
        while q:
            cur_row, cur_col = q.pop()
            for x, y in self.moves:
                next_row, next_col = cur_row + x, cur_col + y
                if (
                    (0 <= next_row < n) and (0 <= next_col < m)
                    and (not seen[next_row][next_col])
                ):
                    if grid[next_row][next_col] >= bound:
                        last.append((next_row, next_col))
                    else:
                        q.append((next_row, next_col))
                        cells += 1
                    seen[next_row][next_col] = True
        return cells

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        q: int = len(queries)
        query_to_index: dict[int, list[int]] = dict()
        for i in range(q):
            if queries[i] not in query_to_index:
                query_to_index[queries[i]] = []
            query_to_index[queries[i]].append(i)
        queries.sort()
        seen: list[list[bool]] = [[False] * len(grid[0]) for _ in range(len(grid))]
        last: list[tuple[int, int]] = []
        capacity: int = len(grid) * len(grid[0])
        prev: int = 0
        output: list[int] = [0] * q
        i: int = 0
        while i < q:
            if not seen[0][0] and grid[0][0] < queries[i]:
                seen[0][0] = True
                last.append((0, 0))
            result = self.get_path(queries[i], grid, seen, last)
            output[query_to_index[queries[i]][-1]] = result + prev
            query_to_index[queries[i]].pop()
            i += 1
            while i < q and ((queries[i] == queries[i - 1]) or (result + prev == capacity)):
                output[query_to_index[queries[i]][-1]] = result + prev
                query_to_index[queries[i]].pop()
                i += 1
            prev += result
        return output

# C++ O(QlogQ + NM) O(Q + NM) Matrix Memoization Breadth-First-Search
class Solution {
private:
    vector<pair<int, int>> moves = {
        {1, 0}, {0, 1}, {0, -1}, {-1, 0}
    };
public:
    int getPath (int& bound, vector<vector<int>>& grid, vector<vector<bool>>& seen, vector<tuple<int, int>>& last) {
        int n = grid.size(), m = grid[0].size();
        vector<tuple<int, int>> q;
        int cells = 0;
        int k = last.size() - 1;
        int i = 0;
        while (i <= k) {
            if (grid[get<0>(last[i])][get<1>(last[i])] < bound) {
                q.push_back(tuple<int, int>(last[i]));
                ++cells;
                last[i] = last[k];
                last.pop_back();
                --k;
            } else ++i;
        }
        while (!q.empty()) {
            int curRow = get<0>(q.back());
            int curCol = get<1>(q.back());
            q.pop_back();
            for (pair<int, int>& move : moves) {
                int nextRow = curRow + move.first;
                int nextCol = curCol + move.second;
                if (
                    (nextRow >= 0 && nextRow < n)
                    && (nextCol >= 0 && nextCol < m)
                    && (!seen[nextRow][nextCol])
                ) {
                    if (grid[nextRow][nextCol] >= bound) {
                        last.push_back({nextRow, nextCol});
                        seen[nextRow][nextCol] = true;
                        continue;
                    }
                    ++cells;
                    seen[nextRow][nextCol] = true;
                    q.push_back({nextRow, nextCol});
                }
            }
        }
        return cells;
    }
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        int q = queries.size();
        unordered_map<int, vector<int>> queryIndex;
        for (int i = 0; i < q; ++i) {
            queryIndex[queries[i]].push_back(i);
        }
        sort(queries.begin(), queries.end());
        int capacity = grid.size() * grid[0].size();
        vector<vector<bool>> seen (grid.size(), vector<bool>(grid[0].size(), false));
        vector<int> output (q, 0);
        vector<tuple<int, int>> last;
        size_t i = 0;
        int prev = 0;
        while (i < q) {
            if (!seen[0][0] && grid[0][0] < queries[i]) {
                seen[0][0] = true;
                last.push_back({0, 0});
            }
            int result = getPath(queries[i], grid, seen, last);
            output[queryIndex[queries[i]].back()] = result + prev;
            queryIndex[queries[i]].pop_back();
            ++i;
            while (i < q && ((queries[i] == queries[i - 1]) || (result + prev == capacity))) {
                output[queryIndex[queries[i]].back()] = result + prev;
                queryIndex[queries[i]].pop_back();
                ++i;
            }
            prev += result;
        }
        return output;
    }
};