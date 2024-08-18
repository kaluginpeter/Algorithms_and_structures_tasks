# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
#
# The value of |x| is defined as:
#
# x if x >= 0.
# -x if x < 0.
#
#
# Example 1:
#
# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# Example 2:
#
# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.
# Example 3:
#
# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 1 <= k <= 99
# Solution 1 - Brute Force - Nested loops. Speed O(N**2) and Memory O(1)
# Note: if we should find a differences by absolute (abs) method, we can nof check i < j, but in the end, we have pairs*2
# variations of multiplicate numbers. And then we just should divide answer on 2
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count: int = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count // 2
# Solution 2 HashTable. Speed O(N) and Memory O(N)
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hm: dict = {}
        for i in nums:
            hm[i] = hm.get(i, 0) + 1
        count: int = 0
        for i in nums:
            if k + i in hm:
                count += hm[k + i]
        return count