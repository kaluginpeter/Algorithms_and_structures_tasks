

# Given an integer array nums, move all the even integers at
# the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
#
# Example 1:
#
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
# Constraints:
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
# Solution
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)

# Solution 2 - Two Pointers
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        x, y = 0, len(nums) - 1
        while x < y:
            while x < y and nums[x] & 0x1 == 0:
                x += 1
            while x < y and nums[y] & 0x1 != 0:
                y -= 1
            nums[x], nums[y] = nums[y], nums[x]
        return nums