# You are given an array of integers nums. Return the length of the longest
# subarray
#  of nums which is either
# strictly increasing
#  or
# strictly decreasing
# .
#
#
#
# Example 1:
#
# Input: nums = [1,4,3,3,2]
#
# Output: 2
#
# Explanation:
#
# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
#
# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
#
# Hence, we return 2.
#
# Example 2:
#
# Input: nums = [3,3,3,3]
#
# Output: 1
#
# Explanation:
#
# The strictly increasing subarrays of nums are [3], [3], [3], and [3].
#
# The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
#
# Hence, we return 1.
#
# Example 3:
#
# Input: nums = [3,2,1]
#
# Output: 3
#
# Explanation:
#
# The strictly increasing subarrays of nums are [3], [2], and [1].
#
# The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
#
# Hence, we return 3.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
# Solution O(N) O(1)
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans, top = 1, 0
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[prev]:
                prev = i
                continue
            else:
                ans = max(ans, i - top)
                top, prev = i, i
        ans = max(ans, len(nums) - top)
        top, prev = 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[prev]:
                prev = i
            else:
                ans = max(ans, i - top)
                top, prev = i, i
        ans = max(ans, len(nums) - top)
        return ans