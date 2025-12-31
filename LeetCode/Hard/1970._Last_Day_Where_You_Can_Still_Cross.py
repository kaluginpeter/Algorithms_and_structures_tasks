# There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.
#
# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).
#
# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).
#
# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.
#
#
#
# Example 1:
#
#
# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.
# Example 2:
#
#
# Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
# Output: 1
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 1.
# Example 3:
#
#
# Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
# Output: 3
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 3.
#
#
# Constraints:
#
# 2 <= row, col <= 2 * 104
# 4 <= row * col <= 2 * 104
# cells.length == row * col
# 1 <= ri <= row
# 1 <= ci <= col
# All the values of cells are unique.
# Solution
# Python O(NMlog(NM)) O(NM) BinarySearch Matrix Depth-First-Search
moves: list[tuple[int, int]] = [
    (1, 0), (-1, 0), (0, 1), (0, -1)
]
class Solution:
    def check(self, middle: int, row: int, col: int, cells: list[list[int]]) -> bool:
        matrix: list[list[int]] = [[True] * (col + 1) for _ in range(row + 1)]
        for i in range(middle):
            matrix[cells[i][0]][cells[i][1]] = False
        cur_nodes: list[tuple[int, int]] = [(1, j) for j in range(1, col + 1) if matrix[1][j]]
        while cur_nodes:
            i, j = cur_nodes.pop()
            if i == row: return True
            for x, y in moves:
                ni: int = i + x
                nj: int = j + y
                if not (0 < ni <= row) or not (0 < nj <= col) or not matrix[ni][nj]:
                    continue
                matrix[ni][nj] = False
                cur_nodes.append((ni, nj))
        return False
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left: int = 0
        right: int = row * col
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if self.check(middle, row, col, cells): left = middle + 1
            else: right = middle - 1
        return right

# C++ O(NMlog(NM)) O(NM) Depth-First-Search BinarySearch Matrix
const std::vector<std::pair<int, int>> moves = {
    {1, 0}, {-1, 0}, {0, 1}, {0, -1}
};
class Solution {
public:
    bool check(int& middle, int& row, int& col, std::vector<std::vector<int>>& cells) {
        std::vector<std::vector<bool>> matrix(row + 1, std::vector<bool>(col + 1, true));
        for (int i = 0; i < middle; ++i) {
            matrix[cells[i][0]][cells[i][1]] = false;
        }
        std::vector<std::pair<int, int>> curNodes;
        for (int j = 1; j <= col; ++j) {
            if (matrix[1][j]) curNodes.push_back({1, j});
        }
        while (!curNodes.empty()) {
            auto [i, j] = curNodes.back();
            curNodes.pop_back();
            if (i == row) return true;
            for (auto& [x, y] : moves) {
                int nI = i + x, nJ = j + y;
                if (!nI || nI > row || !nJ || nJ > col || !matrix[nI][nJ]) continue;
                matrix[nI][nJ] = false;
                curNodes.push_back({nI, nJ});
            }
        }
        return false;
    }
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        int left = 0, right = row * col;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (check(middle, row, col, cells)) left = middle + 1;
            else right = middle - 1;
        }
        return right;
    }
};