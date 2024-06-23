# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
#
#
#
# Example 1:
#
# Input: nums = [8,2,4,7], limit = 4
# Output: 2
# Explanation: All subarrays are:
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4.
# Therefore, the size of the longest subarray is 2.
# Example 2:
#
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:
#
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= limit <= 109
# Solution Monotonic Queue O(N) O(N)
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minimum_item = deque()
        maximum_item = deque()
        left_pointer: int = 0
        max_length_of_subarray: int = 0
        for right_pointer in range(len(nums)):
            while minimum_item and nums[right_pointer] < minimum_item[-1]:
                minimum_item.pop()
            minimum_item.append(nums[right_pointer])
            while maximum_item and nums[right_pointer] > maximum_item[-1]:
                maximum_item.pop()
            maximum_item.append(nums[right_pointer])
            while maximum_item[0] - minimum_item[0] > limit:
                if nums[left_pointer] == minimum_item[0]:
                    minimum_item.popleft()
                if nums[left_pointer] == maximum_item[0]:
                    maximum_item.popleft()
                left_pointer += 1
            max_length_of_subarray = max(max_length_of_subarray, right_pointer - left_pointer + 1)
        return max_length_of_subarray
# Solution Monotonic Queue with more native logic O(N) O(N)
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minimum_item = deque()
        maximum_item = deque()
        left_pointer: int = 0
        max_length_of_subarray: int = 0
        for right_pointer in range(len(nums)):
            while minimum_item and nums[right_pointer] < nums[minimum_item[-1]]:
                minimum_item.pop()
            minimum_item.append(right_pointer)
            while maximum_item and nums[right_pointer] > nums[maximum_item[-1]]:
                maximum_item.pop()
            maximum_item.append(right_pointer)
            while minimum_item and maximum_item and nums[maximum_item[0]] - nums[minimum_item[0]] > limit:
                if left_pointer >= minimum_item[0]:
                    minimum_item.popleft()
                if left_pointer >= maximum_item[0]:
                    maximum_item.popleft()
                left_pointer += 1
            max_length_of_subarray = max(max_length_of_subarray, right_pointer - left_pointer + 1)
        return max_length_of_subarray