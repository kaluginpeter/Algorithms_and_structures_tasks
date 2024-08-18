# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
#
#
#
# Example 1:
#
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:
#
# Input: arr = [1,1]
# Output: 1
#
#
# Constraints:
#
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 105
# Solution
class Solution(object):
    def findSpecialInteger(self, arr):
        val, top, n = arr[0], 0, len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == val:
                top += 1
                if top > n:
                    return  val
            else:
                val, top = arr[i], 1