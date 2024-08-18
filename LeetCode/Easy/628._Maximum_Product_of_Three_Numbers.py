# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: 6
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:
#
# Input: nums = [-1,-2,-3]
# Output: -6
#
#
# Constraints:
#
# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
# Solution O(N) O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float('-inf')
        first_min = second_min = float('inf')
        for i in nums:
            if i > first_max:
                first_max, second_max, third_max = i, first_max, second_max
            elif i > second_max:
                second_max, third_max = i, second_max
            elif i > third_max:
                third_max = i
            if i < first_min:
                first_min, second_min = i, first_min
            elif i < second_min:
                second_min = i
        if second_min != float('inf'):
            return max(first_min * second_min * first_max, first_max * second_max * third_max)
        return first_max * second_max * third_max