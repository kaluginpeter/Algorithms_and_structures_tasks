# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
# HashMap
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache: dict[int, int] = {0: nums[0], 1: nums[1]}
        for idx in range(2, len(nums)):
            cache[idx] = max(cache.get(idx - 2), cache.get(idx - 3, 0)) + nums[idx]
        return max(cache.values())

# Constant Memory Complexity
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums[1] = max(nums[0], nums[1])
        for idx in range(2, len(nums)):
            nums[idx] = max(nums[idx - 1], nums[idx] + nums[idx - 2])
        return nums[-1]