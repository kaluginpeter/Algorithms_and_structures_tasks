# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
#
# Each queries[i] represents the following action on nums:
#
# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.
#
# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.
#
#
#
# Example 1:
#
# Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
#
# Output: 2
#
# Explanation:
#
# For i = 0 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [1, 0, 1].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
# Example 2:
#
# Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
#
# Output: -1
#
# Explanation:
#
# For i = 0 (l = 1, r = 3, val = 2):
# Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
# The array will become [4, 1, 0, 0].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
# The array will become [3, 0, 0, 0], which is not a Zero Array.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 5 * 105
# 1 <= queries.length <= 105
# queries[i].length == 3
# 0 <= li <= ri < nums.length
# 1 <= vali <= 5
# Solution
# Python O(NlogN) O(N) Sweep Line Binary Search
class Solution:
    def sweep_line(self, bound: int, nums: list[int], queires: list[list[int]]) -> bool:
        n: int = len(nums)
        diff_arr: list[int] = [0] * n
        for idx in range(bound):
            left, right, val = queires[idx]
            diff_arr[left] += val
            if right + 1 < n:
                diff_arr[right + 1] -= val
        counter: int = 0
        for idx in range(n):
            counter += diff_arr[idx]
            if counter < nums[idx]:
                return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left: int = 0
        right: int = len(queries) + 1
        result: int = -1
        while left < right:
            middle: int = left + (right - left) // 2
            if self.sweep_line(middle, nums, queries):
                result = middle
                right = middle
            else:
                left = middle + 1
        return result

# C++ O(NlogN) O(N) Sweep Line Binary Search
class Solution {
public:
    bool sweepLine(int bound, std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = nums.size();
        std::vector<int> diffArr(n, 0);
        for (int index = 0; index < bound; ++index) {
            std::vector<int>& query = queries[index];
            int left = query[0];
            int right = query[1];
            int val = query[2];
            diffArr[left] += val;
            if (right + 1 < n) {
                diffArr[right + 1] -= val;
            }
        }
        int counter = 0;
        for (int index = 0; index < n; ++index) {
            counter += diffArr[index];
            if (counter < nums[index]) {
                return false;
            }
        }
        return true;
    }

    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int left = 0;
        int right = queries.size() + 1;
        int result = -1;
        while (left < right) {
            int middle = left + (right - left) / 2;
            if (sweepLine(middle, nums, queries)) {
                result = middle;
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return result;
    }
};