# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
#
# A uni-value grid is a grid where all the elements of it are equal.
#
# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
#
#
#
# Example 1:
#
#
# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following:
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.
# Example 2:
#
#
# Input: grid = [[1,5],[2,3]], x = 1
# Output: 5
# Explanation: We can make every element equal to 3.
# Example 3:
#
#
# Input: grid = [[1,2],[3,4]], x = 2
# Output: -1
# Explanation: It is impossible to make every element equal.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 1 <= x, grid[i][j] <= 104
# Solution
# Python O(NM + L + NM) O(L + NM) Sorting Matrix Greedy
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        hashmap: list[int] = [0] * (10000 + 1)
        for row in grid:
            for num in row: hashmap[num] += 1
        nums: list[int] = []
        for num in range(1, len(hashmap)):
            for j in range(hashmap[num]): nums.append(num)
        median: int = nums[len(nums) // 2]
        operations: int = 0
        for num in nums:
            diff: int = abs(num - median)
            if diff % x != 0: return -1
            operations += diff // x
        return operations

# C++ O(NM + L + NM) O(L + NM) Matrix Greedy Sorting
class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> hashmap (1e4 + 1, 0);
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                ++hashmap[grid[i][j]];
            }
        }
        vector<int> nums;
        for (int num = 1; num < hashmap.size(); ++num) {
            for (int i = 0; i < hashmap[num]; ++i) nums.push_back(num);
        }
        int median = nums[nums.size() / 2];
        int operations = 0;
        for (int& num : nums) {
            int diff = abs(num - median);
            if (diff % x != 0) return -1;
            operations += diff / x;
        }
        return operations;
    }
};