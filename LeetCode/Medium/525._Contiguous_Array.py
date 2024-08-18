# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
#
#
# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Solution HashTable OnePass PrefixSum O(N) O(N)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ht: dict = dict()
        count: int = 0
        ans: int = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count == 0:
                ans = max(ans, i + 1)
            elif count in ht:
                ans = max(ans, i - ht[count])
            else:
                ht[count] = i
        return ans