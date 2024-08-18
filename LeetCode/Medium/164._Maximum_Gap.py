# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
#
# You must write an algorithm that runs in linear time and uses linear extra space.
#
#
#
# Example 1:
#
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
# Example 2:
#
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# Solution Bucket Sort O(N) O(N)
class Solution:
    from math import ceil
    def maximumGap(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)
        if len(nums) < 2 or mn == mx:
            return 0
        n: int = ceil((mx - mn) / (len(nums) - 1))
        bucket: list[list[int, int]] = [[None, None] for _ in range((mx - mn) // n + 1)]
        for elmnt in nums:
            current_chunck: list[int, int] = bucket[(elmnt - mn) // n]
            current_chunck[0] = elmnt if current_chunck[0] is None else min(elmnt, current_chunck[0])
            current_chunck[1] = elmnt if current_chunck[1] is None else max(elmnt, current_chunck[1])
        bucket = [chunck for chunck in bucket if chunck[0] if not None]
        return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))