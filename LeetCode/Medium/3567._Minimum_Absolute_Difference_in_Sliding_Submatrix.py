# You are given an m x n integer matrix grid and an integer k.
#
# For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.
#
# Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.
#
# Note: If all elements in the submatrix have the same value, the answer will be 0.
#
# A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
#
#
# Example 1:
#
# Input: grid = [[1,8],[3,-2]], k = 2
#
# Output: [[2]]
#
# Explanation:
#
# There is only one possible k x k submatrix: [[1, 8], [3, -2]].
# Distinct values in the submatrix are [1, 8, 3, -2].
# The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].
# Example 2:
#
# Input: grid = [[3,-1]], k = 1
#
# Output: [[0,0]]
#
# Explanation:
#
# Both k x k submatrix has only one distinct element.
# Thus, the answer is [[0, 0]].
# Example 3:
#
# Input: grid = [[1,-2,3],[2,3,5]], k = 2
#
# Output: [[1,2]]
#
# Explanation:
#
# There are two possible k × k submatrix:
# Starting at (0, 0): [[1, -2], [2, 3]].
# Distinct values in the submatrix are [1, -2, 2, 3].
# The minimum absolute difference in the submatrix is |1 - 2| = 1.
# Starting at (0, 1): [[-2, 3], [3, 5]].
# Distinct values in the submatrix are [-2, 3, 5].
# The minimum absolute difference in the submatrix is |3 - 5| = 2.
# Thus, the answer is [[1, 2]].
#
#
# Constraints:
#
# 1 <= m == grid.length <= 30
# 1 <= n == grid[i].length <= 30
# -105 <= grid[i][j] <= 105
# 1 <= k <= min(m, n)
#
# Solution
# Python O((N - K)(M - K) + NMK) O((N - K)(M - K)) Matrix BruteForce
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n: int = len(grid)
        m: int = len(grid[0])
        output: list[list[int]] = [[0] * (m - k + 1) for _ in range(n - k + 1)]
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                seen: set[int] = set()
                for ix in range(i, i + k):
                    for jx in range(j, j + k): seen.add(grid[ix][jx])
                if len(seen) == 1: continue
                prev: int = float('inf')
                diff: int = float('inf')
                for x in sorted(seen):
                    if prev != float('inf'): diff = min(diff, abs(prev - x))
                    prev = x
                output[i][j] = diff
        return output

# C++ O((N - K)(M - K) + NMK) O((N - K)(M - K)) BruteForce Matrix
class Solution {
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<std::vector<int>> output(n - k + 1, std::vector<int>(m - k + 1, 0));
        for (size_t i = 0; i < n - k + 1; ++i) {
            for (size_t j = 0; j < m - k + 1; ++j) {
                std::set<int> seen;
                for (size_t ix = i; ix < i + k; ++ix) {
                    for (size_t jx = j; jx < j + k; ++jx) seen.insert(grid[ix][jx]);
                }
                if (seen.size() == 1) continue;
                int diff = INT32_MAX, prev = 1e5 + 1;
                for (const int& x : seen) {
                    if (prev < 1e5 + 1) diff = std::min(diff, std::abs(x - prev));
                    prev = x;
                }
                output[i][j] = diff;
            }
        }
        return output;
    }
};