# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
#
# A grid is said to be valid if all the cells above the main diagonal are zeros.
#
# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
#
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).
#
#
#
# Example 1:
#
#
# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
# Example 3:
#
#
# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 1 <= n <= 200
# grid[i][j] is either 0 or 1
# Solution
# Python O(N^2) O(1) InsertionSort Math
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        for i in range(n):
            j: int = len(grid[i])
            while j:
                if grid[i][j - 1]: break
                j -= 1
            grid[i][-1] = len(grid[i]) - j
        output: int = 0
        for i in range(n - 1):
            if grid[i][-1] >= (n - i - 1): continue
            for j in range(i + 1, n):
                if grid[j][-1] >= (n - i - 1):break
            else: return -1 # Can't find valid row
            output += j - i
            while j > i:
                grid[j], grid[j - 1] = grid[j - 1], grid[j]
                j -= 1
        return output

# C++ O(N^2) O(1) Math InsertionSort
class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        size_t n = grid.size();
        for (size_t i = 0; i < n; ++i) {
            size_t j = grid[i].size();
            while (j) {
                if (grid[i][j - 1]) break;
                --j;
            }
            grid[i].back() = grid[i].size() - j;
        }
        uint32_t output = 0;
        for (size_t i = 0; i < n - 1; ++i) {
            if (grid[i].back() >= (n - i - 1)) continue;
            int target = -1;
            for (size_t j = i + 1; j < n; ++j) {
                if (grid[j].back() >= (n - i - 1)) {
                    target = j;
                    break;
                }
            }
            if (target == -1) return -1; // Can't find valid row
            output += target - i;
            while (target > i) std::swap(grid[target], grid[--target]);
        }
        return output;
    }
};