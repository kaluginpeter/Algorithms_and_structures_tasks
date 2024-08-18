# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
#
# Input: nums = [1,1]
# Output: [1,2]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104
# Solution
class Solution(object):
    def findErrorNums(self, nums):
        return [sum(nums) - sum(set(nums)), list(set(range(1, len(nums) + 1)) - set(nums))[0]]


# Solution 2 Math O(N) O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l, x, y = len(nums), sum(nums), sum(set(nums))
        k = (l * (l + 1)) // 2
        return [x-y, k-y]
# Solution 3 HashTable O(N) O(N)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ht: dict = {}
        for i in range(1, len(nums) + 1):
            ht[i] = 0
        for i in nums:
            ht[i] += 1
        missing, dub = 0, 0
        for i in ht:
            if ht[i] == 0:
                missing = i
            elif ht[i] > 1:
                dub = i
        return [dub, missing]