# You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:
#
# Each of the two resulting sections formed by the cut is non-empty.
# The sum of the elements in both sections is equal.
# Return true if such a partition exists; otherwise return false.
#
#
#
# Example 1:
#
# Input: grid = [[1,4],[2,3]]
#
# Output: true
#
# Explanation:
#
#
#
# A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.
#
# Example 2:
#
# Input: grid = [[1,3],[2,4]]
#
# Output: false
#
# Explanation:
#
# No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.
#
#
#
# Constraints:
#
# 1 <= m == grid.length <= 105
# 1 <= n == grid[i].length <= 105
# 2 <= m * n <= 105
# 1 <= grid[i][j] <= 105
#
# Solution
# Python O(NM + 2log2(NM)) O(N) PrefixSum BinarySearch Matrix
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        prefix: list[int] = [0]
        for c in range(m):
            acc: int = 0
            for r in range(n): acc += grid[r][c]
            prefix.append(acc + prefix[-1])
        left: int = 1
        right: int = m
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            x: int = prefix[middle]
            y: int = prefix[m] - prefix[middle]
            if x == y: return True
            elif x > y: right = middle - 1
            else: left = middle + 1
        prefix = [0]
        for r in range(n):
            acc: int = 0
            for c in range(m): acc += grid[r][c]
            prefix.append(prefix[-1] + acc)
        left: int = 1
        right: int = n
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            x: int = prefix[middle]
            y: int= prefix[n] - prefix[middle]
            if x == y: return True
            elif x > y: right = middle - 1
            else: left = middle + 1
        return False

# C++ O(NM + 2log2(NM)) O(N) Matrix BinarySearch PrefixSum
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        size_t n = grid.size(), m = grid[0].size();
        std::vector<size_t> prefix = {0};
        for (size_t j = 0; j < m; ++j) {
            size_t acc = 0;
            for (size_t i = 0; i < n; ++i) acc += grid[i][j];
            prefix.push_back(prefix.back() + acc);
        }
        size_t left = 1, right = m;
        while (left <= right) {
            size_t middle = left + ((right - left) >> 1);
            size_t x = prefix[middle], y = prefix[m] - prefix[middle];
            if (x == y) return true;
            else if (x > y) right = middle - 1;
            else left = middle + 1;
        }
        prefix = {0};
        for (size_t i = 0; i < n; ++i) {
            size_t acc = 0;
            for (size_t j = 0; j < m; ++j) acc += grid[i][j];
            prefix.push_back(prefix.back() + acc);
        }
        left = 1;
        right = n;
        while (left <= right) {
            size_t middle = left + ((right - left) >> 1);
            size_t x = prefix[middle], y = prefix[n] - prefix[middle];
            if (x == y) return true;
            else if (x > y) right = middle - 1;
            else left = middle + 1;
        }
        return false;
    }
};