# You are given an n x n square matrix of integers grid. Return the matrix such that:
#
# The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
# The diagonals in the top-right triangle are sorted in non-decreasing order.
#
#
# Example 1:
#
# Input: grid = [[1,7,3],[9,8,2],[4,5,6]]
#
# Output: [[8,2,3],[9,6,7],[4,5,1]]
#
# Explanation:
#
#
#
# The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:
#
# [1, 8, 6] becomes [8, 6, 1].
# [9, 5] and [4] remain unchanged.
# The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:
#
# [7, 2] becomes [2, 7].
# [3] remains unchanged.
# Example 2:
#
# Input: grid = [[0,1],[1,2]]
#
# Output: [[2,1],[1,0]]
#
# Explanation:
#
#
#
# The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.
#
# Example 3:
#
# Input: grid = [[1]]
#
# Output: [[1]]
#
# Explanation:
#
# Diagonals with exactly one element are already in order, so no changes are needed.
#
#
#
# Constraints:
#
# grid.length == grid[i].length == n
# 1 <= n <= 10
# -105 <= grid[i][j] <= 105
#
# Solution
# Python O(N^2 * logN) O(N) Matrix
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n: int = len(grid)
        i: int = n - 1
        j: int = 0
        while j < n:
            nums: list[int] = []
            pos: int = 0
            while i + pos < n and j + pos < n:
                nums.append(grid[i + pos][j + pos])
                pos += 1
            nums.sort(reverse=not j)
            pos = 0
            while i + pos < n and j + pos < n:
                grid[i + pos][j + pos] = nums[pos]
                pos += 1
            if i: i -= 1
            else: j += 1
        return grid

# C++ O(N^2 * logN) O(N) Matrix
class Solution {
public:
    vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
        size_t n = grid.size(), i = n - 1, j = 0;
        while (j < n) {
            std::vector<int> nums;
            size_t pos = 0;
            while (i + pos < n && j + pos < n) {
                nums.emplace_back(grid[i + pos][j + pos]);
                ++pos;
            }
            if (j) std::sort(nums.begin(), nums.end());
            else std::sort(nums.begin(), nums.end(), std::greater<int>());
            pos = 0;
            while (i + pos < n && j + pos < n) {
                grid[i + pos][j + pos] = nums[pos];
                ++pos;
            }
            if (i) -- i;
            else ++j;
        }
        return grid;
    }
};