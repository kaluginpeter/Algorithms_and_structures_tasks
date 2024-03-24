# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: nums = [3,1,3,4,2]
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
#
#
# Follow up:
#
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
# Solution 1 - HashTable
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                return i
            else:
                d[i] = 1

# Solution 2 - HashSet
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)
# Solution 3 - Floyd Circle Algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        array: list[bool] = [True] * len(nums)
        for i in nums:
            if array[i-1]:
                array[i-1] = False
            else:
                return i