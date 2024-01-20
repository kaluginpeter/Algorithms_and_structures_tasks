# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# Solution O(N) O(N) Bucket
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht: dict = {}
        for i in nums:
            ht[i] = ht.get(i, 0) + 1
        bucket: list = [None] * (len(nums) + 1)
        for i in ht:
            if not bucket[ht[i]]:
                bucket[ht[i]] = [i]
            else:
                bucket[ht[i]].extend([i])
        ans: list = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                ans.extend(bucket[i])
                if len(ans) >= k:
                    break
        return ans[:k]
# Solution HashTable O(NK) O(N + K)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht: dict = {}
        for i in nums:
            ht[i] = ht.get(i, 0) + 1
        ans: list = []
        while k > 0:
            top: int = float('-inf')
            top_value: int = None
            for i in ht:
                if ht[i] > top:
                    top, top_value = ht[i], i
            ans.append(top_value)
            del ht[top_value]
            k -= 1
        return ans