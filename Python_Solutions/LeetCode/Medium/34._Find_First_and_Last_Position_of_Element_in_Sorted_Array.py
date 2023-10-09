# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109
# Solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        pos, left, right = [-1, -1], 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                pos[0], right = mid, mid - 1
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        if pos[0] == -1:
            return pos
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                pos[1], left = mid, mid + 1
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return pos

# Solution 2 - My solution with daily task
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        ans, l, r = [-1, -1], 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans[0] = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if ans[0] == -1:
            return ans
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans[1] = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return ans
