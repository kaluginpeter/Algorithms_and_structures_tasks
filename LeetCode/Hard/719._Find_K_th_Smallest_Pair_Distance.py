# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
#
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Example 2:
#
# Input: nums = [1,1,1], k = 2
# Output: 0
# Example 3:
#
# Input: nums = [1,6,1], k = 3
# Output: 5
#
#
# Constraints:
#
# n == nums.length
# 2 <= n <= 104
# 0 <= nums[i] <= 106
# 1 <= k <= n * (n - 1) / 2
# Solution Two Pointers Sliding Window Binary Search O(NlogN + NlogMaxAbs) (1)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid: int = low + (high - low) // 2
            # Case if pairs less that k on middle difference
            if self.count_pairs(nums, mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

    def count_pairs(self, nums: List[int], distance: int) -> int:
        count = left = 0
        for right in range(1, len(nums)):
            while nums[right] - nums[left] > distance:
                left += 1
            count += right - left
        return count