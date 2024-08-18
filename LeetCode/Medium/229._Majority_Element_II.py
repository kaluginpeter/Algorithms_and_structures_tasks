# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: [3]
# Example 2:
#
# Input: nums = [1]
# Output: [1]
# Example 3:
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# Follow up: Could you solve the problem in linear time and in O(1) space?
# Solution - HashTable Speed O(N) Memory O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d, x = {}, len(nums) // 3
        for i in nums:
            d[i] = d.get(i, 0) + 1
        count = []
        for i in d:
            if d[i] > x:
                count += [i]
        return count