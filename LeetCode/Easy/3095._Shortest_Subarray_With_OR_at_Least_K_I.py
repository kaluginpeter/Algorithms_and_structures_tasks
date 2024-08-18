# You are given an array nums of non-negative integers and an integer k.
#
# An array is called special if the bitwise OR of all of its elements is at least k.
#
# Return the length of the shortest special non-empty
# subarray
#  of nums, or return -1 if no special subarray exists.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], k = 2
#
# Output: 1
#
# Explanation:
#
# The subarray [3] has OR value of 3. Hence, we return 1.
#
# Example 2:
#
# Input: nums = [2,1,8], k = 10
#
# Output: 3
#
# Explanation:
#
# The subarray [2,1,8] has OR value of 11. Hence, we return 3.
#
# Example 3:
#
# Input: nums = [1,2], k = 0
#
# Output: 1
#
# Explanation:
#
# The subarray [1] has OR value of 1. Hence, we return 1.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 0 <= k < 64
# Solution O(N**2) O(1)
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            top_or: int = 0
            for j in range(i, len(nums)):
                top_or |= nums[j]
                if top_or >= k:
                    ans = min(ans, j - i + 1)
                    break
        return ans if ans != float('inf') else -1
