# You are given an integer array nums with the following properties:
#
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,1,2,5,3,2]
# Output: 2
# Example 3:
#
# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5
#
#
# Constraints:
#
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 104
# nums contains n + 1 unique elements and one of them is repeated exactly n times.
# Solution HashTable O(N) O(N)
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n: int = 0
        ht: dict[int, int] = dict()
        for i in nums:
            ht[i] = ht.get(i, 0) + 1
            n += 1
        n //= 2
        for i in ht:
            if ht[i] == n:
                return i
# Solution OnePass O(N) O(1)
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] or nums[i] == nums[i - 2]:
                return nums[i]
        return nums[0]