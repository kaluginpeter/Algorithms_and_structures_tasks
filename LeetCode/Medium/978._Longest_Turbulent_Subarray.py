# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
#
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
#
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
#
# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
#
#
# Example 1:
#
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# Example 2:
#
# Input: arr = [4,8,12,16]
# Output: 2
# Example 3:
#
# Input: arr = [100]
# Output: 1
#
#
# Constraints:
#
# 1 <= arr.length <= 4 * 104
# 0 <= arr[i] <= 109
# Solution Two Pointers
# General idea
# We only have to cases:
# Case 1:
# <><><><><>
# Case 2
# ><><><><><
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_length: int = 1
        left: int = 0
        # Case 1
        for right in range(1, len(arr)):
            if (right - 1) & 1:
                if arr[right - 1] <= arr[right]:
                    left = right
            else:
                if arr[right - 1] >= arr[right]:
                    left = right

            max_length = max(max_length, right - left + 1)
        # Case 2
        left: int = 0
        for right in range(1, len(arr)):
            if (right - 1) & 1 == 0:
                if arr[right - 1] <= arr[right]:
                    left = right
            else:
                if arr[right - 1] >= arr[right]:
                    left = right

            max_length = max(max_length, right - left + 1)

        return max_length