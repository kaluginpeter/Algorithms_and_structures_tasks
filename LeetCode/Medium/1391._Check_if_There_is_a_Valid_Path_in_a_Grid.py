# You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:
#
# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.
#
# You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.
#
# Notice that you are not allowed to change any street.
#
# Return true if there is a valid path in the grid or false otherwise.
#
#
#
# Example 1:
#
#
# Input: grid = [[2,4,3],[6,5,2]]
# Output: true
# Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
# Example 2:
#
#
# Input: grid = [[1,2,1],[1,2,1]]
# Output: false
# Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
# Example 3:
#
# Input: grid = [[1,1,2]]
# Output: false
# Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# 1 <= grid[i][j] <= 6
# Solution
# Python O(NM) O(NM) Matrix Depth-First-Search
from copy import deepcopy
class Solution:
    def make_move(self, state: list[int], n: int, m: int, grid: list[list[int]]) -> None:
        i: int = state[0] // m
        j: int = state[0] % m
        node: int = grid[i][j]
        grid[i][j] = -1
        match node:
            case 1:
                if state[1] == 2:
                    if not j: return
                    street: int = grid[i][j - 1]
                    if street != 1 and street != 4 and street != 6: return
                    state[0] = i * m + j - 1
                else:
                    if j + 1 == m: return
                    street: int = grid[i][j + 1]
                    if street != 1 and street != 3 and street != 5: return
                    state[0] = i * m + j + 1
            case 2:
                if state[1] == 1:
                    if not i: return
                    street: int = grid[i - 1][j]
                    if street != 2 and street != 3 and street != 4: return
                    state[0] = (i - 1) * m + j
                else:
                    if i + 1 == n: return
                    street: int = grid[i + 1][j]
                    if street != 2 and street != 5 and street != 6: return
                    state[0] = (i + 1) * m + j
            case 3:
                if state[1] == 3:
                    if i + 1 == n: return
                    street: int = grid[i + 1][j]
                    if street != 2 and street != 5 and street != 6: return
                    state[0] = (i + 1) * m + j
                    state[1] = 0
                else:
                    if not j: return
                    street: int = grid[i][j - 1]
                    if street != 1 and street != 4 and street != 6: return
                    state[0] = (i * m) + j - 1
                    state[1] = 2
            case 4:
                if state[1] == 1:
                    if j + 1 == m: return
                    street: int = grid[i][j + 1]
                    if street != 1 and street != 3 and street != 5: return
                    state[0] = i * m + j + 1
                    state[1] = 3
                else:
                    if i + 1 == n: return
                    street: int = grid[i + 1][j]
                    if street != 2 and street != 5 and street != 6: return
                    state[0] = (i + 1) * m + j
                    state[1] = 0
            case 5:
                if state[1] == 3:
                    if not i: return
                    street: int = grid[i - 1][j]
                    if street != 2 and street != 3 and street != 4: return
                    state[0] = (i - 1) * m + j
                    state[1] = 1
                else:
                    if not j: return
                    street: int = grid[i][j - 1]
                    if street != 1 and street != 4 and street != 6: return
                    state[0] = i * m + j - 1
                    state[1] = 2
            case 6:
                if state[1] == 0:
                    if j + 1 == m: return
                    street: int = grid[i][j + 1]
                    if street != 1 and street != 3 and street != 5: return
                    state[0] = i * m + j + 1
                    state[1] = 3
                else:
                    if not i: return
                    street: int = grid[i - 1][j]
                    if street != 2 and street != 3 and street != 4: return
                    state[0] = (i - 1) * m + j
                    state[1] = 1

    def f(self, grid: list[list[int]]) -> bool:
        n: int = len(grid)
        m: int = len(grid[0])
        cur_node: list[int] = [0, 0]
        if grid[0][0] == 1 or grid[0][0] == 3 or grid[0][0] == 4: cur_node[1] = 3
        while grid[cur_node[0] // m][cur_node[0] % m] != -1:
            self.make_move(cur_node, n, m, grid)
        return grid[n - 1][m - 1] == -1

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if grid[0][0] == 4:
            first: bool = self.f(deepcopy(grid))
            grid[0][0] = 1
            return first or self.f(grid)
        return self.f(grid)

# C++ O(NM) O(NM) DepthFirstSearch Matrix
class Solution {
public:
    void makeMove(std::pair<size_t, int>& state, const size_t& n, const size_t& m, std::vector<std::vector<int>>& grid) {
        const size_t i = state.first / m, j = state.first % m;
        int node = grid[i][j];
        grid[i][j] = -1;
        switch (node) {
            case 1:
                if (state.second == 2) { // moving to left
                    if (!j) return;
                    int& street = grid[i][j - 1];
                    if (street != 1 && street != 4 && street != 6) return;
                    state.first = i * m + j - 1;
                } else { // moving to right
                    if (j + 1 == m) return;
                    int& street = grid[i][j + 1];
                    if (street != 1 && street != 3 && street != 5) return;
                    state.first = i * m + j + 1;
                }
                break;
            case 2:
                if (state.second == 1) { // moving up
                    if (!i) return;
                    int& street = grid[i - 1][j];
                    if (street != 2 && street != 3 && street != 4) return;
                    state.first = (i - 1) * m + j;
                } else { // moving down
                    if (i + 1 == n) return;
                    int& street = grid[i + 1][j];
                    if (street != 2 && street != 5 && street != 6) return;
                    state.first = (i + 1) * m + j;
                }
                break;
            case 3:
                if (state.second == 3) { // moving right to down
                    if (i + 1 == n) return;
                    int& street = grid[i + 1][j];
                    if (street != 2 && street != 5 && street != 6) return;
                    state.first = (i + 1) * m + j;
                    state.second = 0;
                } else { // moving up to left
                    if (!j) return;
                    int& street = grid[i][j - 1];
                    if (street != 1 && street != 4 && street != 6) return;
                    state.first = (i * m) + j - 1;
                    state.second = 2;
                }
                break;
            case 4:
                if (state.second == 1) { // moving up to right
                    if (j + 1 == m) return;
                    int& street = grid[i][j + 1];
                    if (street != 1 && street != 3 && street != 5) return;
                    state.first = i * m + j + 1;
                    state.second = 3;
                } else { // moving left to down
                    if (i + 1 == n) return;
                    int& street = grid[i + 1][j];
                    if (street != 2 && street != 5 && street != 6) return;
                    state.first = (i + 1) * m + j;
                    state.second = 0;
                }
                break;
            case 5:
                if (state.second == 3) { // moving right to up
                    if (!i) return;
                    int& street = grid[i - 1][j];
                    if (street != 2 && street != 3 && street != 4) return;
                    state.first = (i - 1) * m + j;
                    state.second = 1;
                } else { // moving down to left
                    if (!j) return;
                    int& street = grid[i][j - 1];
                    if (street != 1 && street != 4 && street != 6) return;
                    state.first = i * m + j - 1;
                    state.second = 2;
                }
                break;
            case 6:
                if (state.second == 0) { // moving down to right
                    if (j + 1 == m) return;
                    int& street = grid[i][j + 1];
                    if (street != 1 && street != 3 && street != 5) return;
                    state.first = i * m + j + 1;
                    state.second = 3;
                } else { // moving left to up
                    if (!i) return;
                    int& street = grid[i - 1][j];
                    if (street != 2 && street != 3 && street != 4) return;
                    state.first = (i - 1) * m + j;
                    state.second = 1;
                }
                break;
        }
    }
    bool f(std::vector<std::vector<int>> grid) {
        size_t n = grid.size(), m = grid[0].size();
        std::pair<size_t, int> curNode = {0, 0};
        if (grid[0][0] == 1 || grid[0][0] == 3 || grid[0][0] == 4) curNode.second = 3;
        // <curCell, direction(<0: Down>, <1: Up>, <2: Left>, <3: Right>)
        while (grid[curNode.first / m][curNode.first % m] != -1) {
            makeMove(curNode, n, m, grid);
        }
        return grid[n - 1][m - 1] == -1;
    }

    bool hasValidPath(vector<vector<int>>& grid) {
        if (grid[0][0] == 4) {
            bool first = f(grid);
            grid[0][0] = 1;
            return first || f(grid);
        }
        return f(grid);
    }
};