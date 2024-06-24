# You are given a binary array nums and an integer k.
#
# A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
#
# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0], k = 1
# Output: 2
# Explanation: Flip nums[0], then flip nums[2].
# Example 2:
#
# Input: nums = [1,1,0], k = 2
# Output: -1
# Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
# Example 3:
#
# Input: nums = [0,0,0,1,0,1,1,0], k = 3
# Output: 3
# Explanation:
# Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
# Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
# Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= k <= nums.length
# Solution Sliding Window Deque O(N) O(N)
from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        periods = deque()
        total_flips: int = 0
        for idx in range(len(nums)):
            while periods and idx > periods[0]:
                periods.popleft()
            nums[idx] = [nums[idx], int(not nums[idx])][len(periods) % 2]
            if nums[idx] == 0 and idx < len(nums) - k + 1:
                total_flips += 1
                nums[idx] = 1
                periods.append(idx + k - 1)
            elif nums[idx] == 0:
                return -1
        return total_flips