# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
#
# Example 1:
#
# Input: nums = [1,2,2,3]
# Output: true
# Example 2:
#
# Input: nums = [6,5,4,4]
# Output: true
# Example 3:
#
# Input: nums = [1,3,2]
# Output: false
#
# Constraints:
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# Solution
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(i <= j for i,j in zip(nums, nums[1:])) or all(i >= j for i,j in zip(nums, nums[1:]))

# Solution 2
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        cop: int = len(nums) - 1
        count: int = 0
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                count += 1
            else:
                break
        if cop == count:
            return True
        count: int = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                count += 1
        return count == cop
# Solution 3
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        cop: list = nums.copy()
        if nums[0] <= nums[-1]:
            nums.sort()
        else:
            nums.sort(reverse=True)
        for i in range(len(nums)):
            if cop[i] != nums[i]:
                return False
        return True
# Solution 3
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag: int = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if flag == 0:
                    flag = 1
                elif flag == -1:
                    return False
            if nums[i] < nums[i - 1]:
                if flag == 0:
                    flag = -1
                elif flag == 1:
                    return False
        return True