# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
#
#
# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#
#
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?
# Solution O(N) O(1) Two Pointers
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        top: int = 0
        while top <= right:
            if nums[top] == 0:
                nums[top], nums[left] = nums[left], nums[top]
                left += 1
            if nums[top] == 2:
                nums[top], nums[right] = nums[right], nums[top]
                right -= 1
            else:
                top += 1
        return nums

# Solution Dutch national flag O(N) O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n: int = len(nums)
        zeros, twos = 0, n - 1
        current_idx: int = 0
        while current_idx <= twos:
            while current_idx <= twos and nums[current_idx] == 0:
                if current_idx <= zeros:
                    current_idx += 1
                else:
                    nums[zeros], nums[current_idx] = nums[current_idx], nums[zeros]
                    zeros += 1
            while current_idx <= twos and nums[current_idx] == 2:
                nums[twos], nums[current_idx] = nums[current_idx], nums[twos]
                twos -= 1
            if current_idx < n and nums[current_idx] == 1:
                current_idx += 1