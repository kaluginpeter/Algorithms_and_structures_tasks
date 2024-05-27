

# You are given an array nums of non-negative integers. nums is considered special if
# there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1. It can be proven
# that if nums is special, the value for x is unique.
#
# Example 1:
#
# Input: nums = [3,5]
# Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
# Example 2:
#
# Input: nums = [0,0]
# Output: -1
# Explanation: No numbers fit the criteria for x.
# If x = 0, there should be 0 numbers >= x, but there are 2.
# If x = 1, there should be 1 number >= x, but there are 0.
# If x = 2, there should be 2 numbers >= x, but there are 0.
# x cannot be greater since there are only 2 numbers in nums.
# Example 3:
#
# Input: nums = [0,4,3,0,4]
# Output: 3
# Explanation: There are 3 values that are greater than or equal to 3.
#
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
# Solution
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            c = 0
            for num in nums:
                if num >= i: c += 1
            if c == i: return i
        return -1

# Solution Bucket Sort + Double Binary Search O(N) O(N)
class Solution:
    def bucket_sort(self, arr):
        bucket = [0 for _ in range(max(arr) + 1)]
        for i in arr:
            bucket[i] += 1
        idx: int = 0
        for chunk in range(len(bucket)):
            if bucket[chunk] > 0:
                for _ in range(bucket[chunk]):
                    arr[idx] = chunk
                    idx += 1

    def leftmost_binary_search(self, arr, target, n):
        left, right = 0, n - 1
        while left <= right:
            middle = (left + right) >> 1
            if arr[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        return right + 1

    def specialArray(self, nums: List[int]) -> int:
        self.bucket_sort(nums)
        n: int = len(nums)
        left, right = 0, n
        while left <= right:
            middle = (left + right) >> 1
            idx = self.leftmost_binary_search(nums, middle, n)
            items_ge = n - idx
            if items_ge == middle: return middle
            elif items_ge > middle: left = middle + 1
            else: right = middle - 1
        return -1