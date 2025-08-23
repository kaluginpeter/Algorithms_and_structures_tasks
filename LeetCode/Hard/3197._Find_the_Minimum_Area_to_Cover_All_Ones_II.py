# You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.
#
# Return the minimum possible sum of the area of these rectangles.
#
# Note that the rectangles are allowed to touch.
#
#
#
# Example 1:
#
# Input: grid = [[1,0,1],[1,1,1]]
#
# Output: 5
#
# Explanation:
#
#
#
# The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
# The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
# The 1 at (1, 1) is covered by a rectangle of area 1.
# Example 2:
#
# Input: grid = [[1,0,1,0],[0,1,0,1]]
#
# Output: 5
#
# Explanation:
#
#
#
# The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
# The 1 at (1, 1) is covered by a rectangle of area 1.
# The 1 at (1, 3) is covered by a rectangle of area 1.
#
#
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 30
# grid[i][j] is either 0 or 1.
# The input is generated such that there are at least three 1's in grid.
# Solution
# Python O(N^2 * M^2) O(NM) Matrix
class Solution:
    def rectangle_area(self, left: int, right: int, up: int, down: int, grid: list[list[int]]) -> int:
        ur: int = len(grid)
        dr: int = 0
        lc: int = len(grid[0])
        rc: int = 0
        for i in range(up, down + 1):
            for j in range(left, right + 1):
                if not grid[i][j]: continue
                ur = min(ur, i)
                dr = max(dr, i)
                lc = min(lc, j)
                rc = max(rc, j)
        if lc > rc: return int(7e5)
        return (dr - ur + 1) * (rc - lc + 1)

    def check_positions(self, grid: list[list[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        output: int = n * m
        for i in range(n - 1):
            for j in range(m - 1):
                output = min(
                    output,
                    self.rectangle_area(0, m - 1, 0, i, grid) + self.rectangle_area(0, j, i + 1, n - 1,
                                                                                    grid) + self.rectangle_area(j + 1,
                                                                                                                m - 1,
                                                                                                                i + 1,
                                                                                                                n - 1,
                                                                                                                grid)
                )
                output = min(
                    output,
                    self.rectangle_area(0, j, 0, i, grid) + self.rectangle_area(j + 1, m - 1, 0, i,
                                                                                grid) + self.rectangle_area(0, m - 1,
                                                                                                            i + 1,
                                                                                                            n - 1, grid)
                )
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                output = min(
                    output,
                    self.rectangle_area(0, m - 1, 0, i, grid) + self.rectangle_area(0, m - 1, i + 1, j,
                                                                                    grid) + self.rectangle_area(0,
                                                                                                                m - 1,
                                                                                                                j + 1,
                                                                                                                n - 1,
                                                                                                                grid)
                )
        return output

    def rotate(self, grid: list[list[int]]) -> list[list[int]]:
        return list(zip(*reversed(grid)))

    def minimumSum(self, grid: List[List[int]]) -> int:
        rotated_grid: list[list[int]] = self.rotate(grid)
        return min(self.check_positions(grid), self.check_positions(rotated_grid))

# C++ O(N^2 * M^2) O(NM) Matrix

class Solution {
public:
    int rectangleArea(int left, int right, int up, int down, const std::vector<std::vector<int>> &grid) {
        int ur = grid.size(), dr = 0, lc = grid[0].size(), rc = 0;
        for (int i = up; i <= down; ++i) {
            for (int j = left; j <= right; ++j) {
                if (!grid[i][j]) continue;
                ur = std::min(ur, i);
                dr = std::max(dr, i);
                lc = std::min(lc, j);
                rc = std::max(rc, j);
            }
        }
        if (lc > rc) return INT32_MAX / 3; // didn't find any rectangle
        return (dr - ur + 1) * (rc - lc + 1);
    }

    std::vector<std::vector<int>> rotate(std::vector<std::vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();
        std::vector<std::vector<int>> output(m, std::vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                output[m - j - 1][i] = grid[i][j];
            }
        }
        return output;
    }

    int checkPositions(std::vector<std::vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();
        int output = n * m;
        for (int i = 0; i + 1 < n; ++i) {
            for (int j = 0; j + 1 < m; ++j) {
                output = std::min(
                    output,
                    rectangleArea(0, m - 1, 0, i, grid) +
                    rectangleArea(0, j, i + 1, n - 1, grid) +
                    rectangleArea(j + 1, m - 1, i + 1, n - 1, grid)
                );
                output = std::min(
                    output,
                    rectangleArea(0, j, 0, i, grid) +
                    rectangleArea(j + 1, m - 1, 0, i, grid) +
                    rectangleArea(0, m - 1, i + 1, n - 1, grid)
                );
            }
        }
        for (int i = 0; i + 2 < n; ++i) {
            for (int j = i + 1; j + 1 < n; ++j) {
                output = std::min(
                    output,
                    rectangleArea(0, m - 1, 0, i, grid) +
                    rectangleArea(0, m - 1, i + 1, j, grid) +
                    rectangleArea(0, m - 1, j + 1, n - 1, grid)
                );
            }
        }
        return output;
    }

    int minimumSum(vector<vector<int>> &grid) {
        std::vector<std::vector<int>> rotatedGrid = rotate(grid);
        return std::min(checkPositions(grid), checkPositions(rotatedGrid));
    }
};