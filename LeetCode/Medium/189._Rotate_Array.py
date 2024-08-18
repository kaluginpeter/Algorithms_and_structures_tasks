# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
#
#
# Follow up:
#
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# Solution Two Pointers O(N) O(1)
class Solution:
    def vice_versa(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
        return arr
    def rotate(self, nums: List[int], k: int) -> None:
        n: int = len(nums)
        k %= n
        self.vice_versa(nums, 0, n - 1)
        self.vice_versa(nums, 0, k - 1)
        self.vice_versa(nums, k, n - 1)