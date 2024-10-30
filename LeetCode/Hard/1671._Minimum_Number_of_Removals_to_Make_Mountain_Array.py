# You may recall that an array arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1]
# Output: 0
# Explanation: The array itself is a mountain array so we do not need to remove any elements.
# Example 2:
#
# Input: nums = [2,1,1,5,6,2,3,1]
# Output: 3
# Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
#
#
# Constraints:
#
# 3 <= nums.length <= 1000
# 1 <= nums[i] <= 109
# It is guaranteed that you can make a mountain array out of nums.
# Solution
# Python O(N**2) O(N) Dynamic Programming
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N: int = len(nums)
        lis_length: list[int] = [1] * N
        lds_length: list[int] = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis_length[i] = max(lis_length[i], lis_length[j] + 1)
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    lds_length[i] = max(lds_length[i], lds_length[j] + 1)
        min_removals: int = float("inf")
        for i in range(N):
            if lis_length[i] > 1 and lds_length[i] > 1:
                min_removals = min(
                    min_removals, N - lis_length[i] - lds_length[i] + 1
                )
        return min_removals

# C++ O(N**2) O(N) Dynamic Programming
class Solution {
public:
    int minimumMountainRemovals(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> dpLIS(n, 1);
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j] && dpLIS[i] < dpLIS[j] + 1) {
                    dpLIS[i] = dpLIS[j] + 1;
                }
            }
        }
        std::vector<int>dpLDS(n, 1);
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] > nums[j] && dpLDS[i] < dpLDS[j] + 1) {
                    dpLDS[i] = dpLDS[j] + 1;
                }
            }
        }
        int maxSub = 1000000000;
        for (int index = 0; index < n; ++index) {
            if (dpLIS[index] > 1 && dpLDS[index] > 1) {
                maxSub = std::min(maxSub, n - dpLIS[index] - dpLDS[index] + 1);
            }
        }
        return maxSub;
    }
};