# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# Solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# Solution HashTable O(N) O(N)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht1, ht2 = dict(), dict()
        ans: list = list()
        for i in nums1:
            ht1[i] = ht1.get(i, 0) + 1
        for i in nums2:
            ht2[i] = ht2.get(i, 0) + 1
        for i in ht1:
            if i in ht2:
                ans.append(i)
        return ans