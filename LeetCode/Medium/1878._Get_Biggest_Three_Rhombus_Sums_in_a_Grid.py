# You are given an m x n integer matrix grid​​​.
#
# A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:
#
#
# Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.
#
# Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.
#
#
#
# Example 1:
#
#
# Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
# Output: [228,216,211]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
# - Blue: 20 + 3 + 200 + 5 = 228
# - Red: 200 + 2 + 10 + 4 = 216
# - Green: 5 + 200 + 4 + 2 = 211
# Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [20,9,8]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
# - Blue: 4 + 2 + 6 + 8 = 20
# - Red: 9 (area 0 rhombus in the bottom right corner)
# - Green: 8 (area 0 rhombus in the bottom middle)
# Example 3:
#
# Input: grid = [[7,7,7]]
# Output: [7]
# Explanation: All three possible rhombus sums are the same, so return [7].
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 105
# Solution
# Python O(NM + NMmin(N,M)log2(NMmin(N, M))) O(NM) PrefixSum Matrix
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n: int = len(grid)
        m: int = len(grid[0])
        left_diag: list[list[int]] = [[0] * (m + 2) for _ in range(n + 2)]
        right_diag: list[list[int]] = [[0] * (m + 2) for _ in range(n + 2)]
        i: int = 0
        j: int = 0
        while j < m:
            tmpi: int = 1
            tmpj: int = j + 1
            while tmpi <= n and tmpj > 0:
                left_diag[tmpi][tmpj] += left_diag[tmpi - 1][tmpj + 1] + grid[tmpi - 1][tmpj - 1]
                tmpi += 1
                tmpj -= 1
            j += 1
        i = 1
        j = m - 1
        while i < n:
            tmpi: int = i + 1
            tmpj: int = m
            while tmpi <= n and tmpj > 0:
                left_diag[tmpi][tmpj] += left_diag[tmpi - 1][tmpj + 1] + grid[tmpi - 1][tmpj - 1]
                tmpi += 1
                tmpj -= 1
            i += 1
        i = 0
        j = m
        while j > 0:
            tmpi: int = i + 1
            tmpj: int = j
            while tmpi <= n and tmpj <= m:
                right_diag[tmpi][tmpj] += right_diag[tmpi - 1][tmpj - 1] + grid[tmpi - 1][tmpj - 1]
                tmpi += 1
                tmpj += 1
            j -= 1
        i = 1
        j = 0
        while i < n:
            tmpi: int = i + 1
            tmpj: int = j + 1
            while tmpi <= n and tmpj <= m:
                right_diag[tmpi][tmpj] += right_diag[tmpi - 1][tmpj - 1] + grid[tmpi - 1][tmpj - 1]
                tmpi += 1
                tmpj += 1
            i += 1
        seen: set[int] = set()
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                bound: int = min(j - 1, m - j)
                bound = min(bound, (n - i) >> 1)
                for k in range(bound + 1):
                    rhombus_sum: int = (
                        (left_diag[i + k][j - k] - left_diag[i - 1][j + 1])
                        + (right_diag[i + k][j + k] - right_diag[i - 1][j - 1])
                        - grid[i - 1][j - 1]
                        + (left_diag[i + k + k][j] - left_diag[i + k][j + k])
                        + (right_diag[i + k + k][j] - right_diag[i + k][j - k])
                        - (0 if not k else grid[i - 1 + k + k][j - 1])
                    )
                    seen.add(rhombus_sum)
        return sorted(seen, reverse=True)[:3]

# C++ O(NM + NMmin(N, M)log2(NMmin(N, M))) O(NM) Matrix PrefixSum
class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<std::vector<uint32_t>>
            leftDiag(n + 2, std::vector<uint32_t>(m + 2, 0)),
            rightDiag(n + 2, std::vector<uint32_t>(m + 2, 0));
        size_t i = 0, j = 0;
        while (j < m) {
            size_t tmpi = 1, tmpj = j + 1;
            while (tmpi <= n && tmpj > 0) {
                leftDiag[tmpi][tmpj] += leftDiag[tmpi - 1][tmpj + 1] + grid[tmpi - 1][tmpj - 1];
                ++tmpi; --tmpj;
            }
            ++j;
        }
        i = 1; j = m - 1;
        while (i < n) {
            size_t tmpi = i + 1, tmpj = m;
            while (tmpi <= n && tmpj > 0) {
                leftDiag[tmpi][tmpj] += leftDiag[tmpi - 1][tmpj + 1] + grid[tmpi - 1][tmpj - 1];
                ++tmpi; --tmpj;
            }
            ++i;
        }
        i = 0; j = m;
        while (j > 0) {
            size_t tmpi = i + 1, tmpj = j;
            while (tmpi <= n && tmpj <= m) {
                rightDiag[tmpi][tmpj] += rightDiag[tmpi - 1][tmpj - 1] + grid[tmpi - 1][tmpj - 1];
                ++tmpi; ++tmpj;
            }
            --j;
        }
        i = 1; j = 0;
        while (i < n) {
            size_t tmpi = i + 1, tmpj = j + 1;
            while (tmpi <= n && tmpj <= m) {
                rightDiag[tmpi][tmpj] += rightDiag[tmpi - 1][tmpj - 1] + grid[tmpi - 1][tmpj - 1];
                ++tmpi; ++tmpj;
            }
            ++i;
        }
        std::set<int> seen;
        for (size_t i = 1; i <= n; ++i) {
            for (size_t j = 1; j <= m; ++j) {
                size_t bound = std::min(j - 1, m - j);
                bound = std::min(bound, (n - i) >> 1);
                for (size_t k = 0; k <= bound; ++k) {
                    uint32_t rhombusSum =
                    (leftDiag[i + k][j - k] - leftDiag[i - 1][j + 1])
                    + (rightDiag[i + k][j + k] - rightDiag[i - 1][j - 1])
                    - grid[i - 1][j - 1]
                    + (leftDiag[i + k + k][j] - leftDiag[i + k][j + k])
                    + (rightDiag[i + k + k][j] - rightDiag[i + k][j - k])
                    - (k ? grid[i - 1 + k + k][j - 1] : 0);
                    seen.insert(rhombusSum);
                }
            }
        }
        std::vector<int> output;
        while (!seen.empty() && output.size() < 3) {
            output.push_back(*--seen.end());
            seen.erase(*--seen.end());
        }
        return output;
    }
};