# Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1,4,1]
#
# Output: 1
#
# Explanation:
#
# Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.
#
# Example 2:
#
# Input: nums = [1,1,1]
#
# Output: 0
#
# Explanation:
#
# [1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.
#
#
#
# Constraints:
#
# 3 <= nums.length <= 100
# -100 <= nums[i] <= 100
# Solution
# Python O(N) O(1) Sliding Window
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count: int = 0
        left: int = 0
        for right in range(2, len(nums)):
            if right - left + 1 > 3:
                left += 1
            if right - left + 1 == 3:
                if nums[left] + nums[right] == nums[left + 1] / 2:
                    count += 1
        return count

# C++ O(N) O(1) Sliding Window
class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        int count = 0;
        int left = 0;
        for (int right = 2; right < nums.size(); ++right) {
            if (right - left + 1 > 3) {
                ++left;
            }
            if (right - left + 1 == 3) {
                double diff = nums[left + 1] / 2.0;
                if (nums[left] + nums[right] == diff) {
                    ++count;
                }
            }
        }
        return count;
    }
};