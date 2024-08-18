# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# Follow-up: Could you solve the problem in linear time and in O(1) space?
# Solution
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

# Solution O(N) O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht: dict = dict()
        n: int = len(nums) // 2
        for i in nums:
            ht[i] = ht.get(i, 0) + 1
            if ht[i] > n:
                return i
# Solution O(N) O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count: int = 0
        ans: int = 0
        for i in nums:
            if count == 0:
                ans = i
            if i == ans:
                count += 1
            else:
                count -= 1
        return ans