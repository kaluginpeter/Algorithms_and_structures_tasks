# Given an integer array nums, move all 0's to the end of
# it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
# Follow up: Could you minimize the total number of operations done?
# Solution
class Solution:
    def moveZeroes(self, nums):
        ls = len(nums)
        n_pos = 0
        for i in range(ls):
            if nums[i] != 0:
                temp = nums[n_pos]
                nums[n_pos] = nums[i]
                nums[i] = temp
                n_pos += 1