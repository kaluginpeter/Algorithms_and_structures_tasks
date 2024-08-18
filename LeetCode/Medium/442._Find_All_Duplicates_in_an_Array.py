# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
#
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
#
# Input: nums = [1]
# Output: []
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.
# Solution HashTable O(N) O(N)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ht: dict = dict()
        for i in nums:
            ht[i] = ht.get(i, 0) + 1
        return [i for i in ht if ht[i] > 1]
# Solution OnePass O(N) O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans: list = list()
        for i in nums:
            if nums[abs(i) - 1] < 0:
                ans.append(abs(i))
            else:
                nums[abs(i) - 1] *= -1
        return ans