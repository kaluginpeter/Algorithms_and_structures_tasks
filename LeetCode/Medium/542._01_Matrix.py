# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two cells sharing a common edge is 1.
#
#
#
# Example 1:
#
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:
#
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
#
#
# Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/
# Solution
# Python O(MN) O(MN) Matrix Breadth-First-Search
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m: int = len(mat[0])
        n: int = len(mat)
        matrix: list[list[int]] = [[float('inf')] * m for _ in range(n)]
        cur_nodes: list[tuple[int, int]] = []
        next_nodes: list[tuple[int, int]] = []
        moves: tuple[tuple[int, int]] = (
            (1, 0), (-1, 0), (0, 1), (0, -1)
        )
        for row in range(n):
            for col in range(m):
                if not mat[row][col]:
                    matrix[row][col] = 0
                    cur_nodes.append((row, col))
        dist: int = 1
        while cur_nodes:
            for cur_row, cur_col in cur_nodes:
                for x, y in moves:
                    next_row, next_col = cur_row + x, cur_col + y
                    if (
                        0 <= min(next_row, next_col)
                        and next_row < len(matrix) and next_col < len(matrix[0])
                        and matrix[next_row][next_col] == float('inf')
                    ):
                        matrix[next_row][next_col] = dist
                        next_nodes.append((next_row, next_col))
            dist += 1
            cur_nodes = next_nodes
            next_nodes = []
        return matrix

# C++ O(MN) O(MN) Breadth-First-Search Matrix
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();
        std::vector<std::vector<int>> output (n, std::vector<int>(m, -1));
        std::vector<std::pair<int, int>> moves = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };
        std::vector<std::pair<int, int>> curNodes;
        std::vector<std::pair<int, int>> nextNodes;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (!mat[i][j]) {
                    output[i][j] = 0;
                    curNodes.push_back({i, j});
                }
            }
        }
        int dist = 1;
        while (curNodes.size() > 0) {
            for (int i = 0; i < curNodes.size(); ++i) {
                for (std::pair<int, int>& move : moves) {
                    int nextRow = curNodes[i].first + move.first;
                    int nextCol = curNodes[i].second + move.second;
                    if (
                        (0 <= std::min(nextRow, nextCol))
                        && (nextRow < n && nextCol < m)
                        && (output[nextRow][nextCol] == -1)
                    ) {
                        output[nextRow][nextCol] = dist;
                        nextNodes.push_back({nextRow, nextCol});
                    }
                }
            }
            ++dist;
            curNodes = nextNodes;
            nextNodes = {};
        }
        return output;
    }
};