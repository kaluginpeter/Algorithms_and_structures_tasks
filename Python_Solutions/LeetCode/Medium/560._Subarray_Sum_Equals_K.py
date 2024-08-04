# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
# Solution Prefix Sum Hash Table O(N) O(N)
class Solution(object):
    def subarraySum(self, nums, k):
        count: int = 0
        prefix_sum: int = 0
        prefix_sum_count: dict[int, int] = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
        return count