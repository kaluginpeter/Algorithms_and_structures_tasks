# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
#
# Return the sorted array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
# Example 2:
#
# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
# Example 3:
#
# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
# Solution 1, My solution - HashTable O(N**2) O(N)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d, ans = {}, []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        while d:
            top, rep = 0, float('inf')
            for i in d:
                if d[i] < rep:
                    top, rep = i, d[i]
                elif d[i] == rep:
                    x = max(top, i)
                    top, rep = x, d[x]
            del d[top]
            ans += [top] * rep
        return ans
# Solution 2 - HashTable Optimized O(NlogN) O(N)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return sorted(nums, key=lambda x: (d[x], -x))

# Solution 3 HashTable Sorting O(NlogN) O(N)
from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequence: dict[int, int] = defaultdict(int)
        for num in nums:
            frequence[num] += 1
        nums.sort(key=lambda x: (frequence[x], -x))
        return nums