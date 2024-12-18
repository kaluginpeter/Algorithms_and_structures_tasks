# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:
#
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#
# Constraints:
#
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104
# Solution
# Python O(N**2) O(1) Two Pointers Sorting
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff: int = float('-inf')
        nums.sort()
        n: int = len(nums)
        for middle in range(len(nums)):
            sub_target: int = target - nums[middle]
            left = middle + 1
            right = n - 1
            while left < right:
                sub_sum: int = nums[left] + nums[right]
                if abs(sub_target - sub_sum) < abs(target - min_diff):
                    min_diff = nums[left] + nums[middle] + nums[right]
                if sub_sum > sub_target:
                    right -= 1
                else:
                    left += 1
        return min_diff

# C++ O(N**2) O(1) Two Pointers Sorting
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        int minDiff = 1000000;
        int n = nums.size();
        for (int middle = 0; middle < n; ++middle) {
            int subTarget = target - nums[middle];
            int left = middle + 1;
            int right = n - 1;
            while (left < right) {
                int subSum = nums[left] + nums[right];
                if (std::abs(subTarget - subSum) < std::abs(target - minDiff)) {
                    minDiff = nums[left] + nums[middle] + nums[right];
                }
                if (subSum > subTarget) {
                    --right;
                } else {
                    ++left;
                }
            }
        }
        return minDiff;
    }
};