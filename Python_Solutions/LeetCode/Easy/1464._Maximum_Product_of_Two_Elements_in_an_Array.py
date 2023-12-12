# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
#
# Example 1:
#
# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
# you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
# Example 2:
#
# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
# Example 3:
#
# Input: nums = [3,7]
# Output: 12
#
# Constraints:
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10^3
# Solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = sorted(nums, reverse=True)[:2]
        return (a - 1) * (b - 1)


# Solution 2
class Solution(object):
    def maxProduct(self, nums):
        x, y = min(nums[0], nums[1]), max(nums[1], nums[0])
        for i in range(2, len(nums)):
            if nums[i] >= y:
                y, x = nums[i], y
            elif nums[i] > x:
                x = nums[i]
        return (x - 1) * (y - 1)
