# You are given a
# binary array
#  nums.
#
# We call a
# subarray
#  alternating if no two adjacent elements in the subarray have the same value.
#
# Return the number of alternating subarrays in nums.
#
#
#
# Example 1:
#
# Input: nums = [0,1,1,1]
#
# Output: 5
#
# Explanation:
#
# The following subarrays are alternating: [0], [1], [1], [1], and [0,1].
#
# Example 2:
#
# Input: nums = [1,0,1,0]
#
# Output: 10
#
# Explanation:
#
# Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Solution o(N) O(1)
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        ans: int = 0
        ln: int = 0
        for i in range(len(nums) - 1):
            ln += 1
            if nums[i] == nums[i + 1]:
                ans += ln * (ln + 1) // 2
                ln = 0
        if len(nums) > 1:
            if nums[-1] != nums[-2]:
                ln += 1
            else:
                ln = 1
            ans += ln * (ln + 1) // 2
        return ans