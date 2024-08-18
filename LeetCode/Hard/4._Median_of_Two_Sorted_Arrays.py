# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
# Solution 1 My solution - O((m + n)log(m + n)) / O(m + n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        if len(l) % 2 == 0:
            return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
        return l[len(l) // 2]
# Solution 2 Two pointers - O(m + n) / O(m + n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l, x, y = [], 0, 0
        while x < len(nums1) and y < len(nums2):
            if nums1[x] > nums2[y]:
                l.append(nums2[y])
                y += 1
            else:
                l.append(nums1[x])
                x += 1
        while x < len(nums1):
            l.append(nums1[x])
            x += 1
        while y < len(nums2):
            l.append(nums2[y])
            y += 1
        if len(l) % 2 == 0:
            return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
        return l[len(l) // 2]
# Solution 3 Binary Search - O(log(min(m, n))) / O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            middleX = (low + high) // 2
            middleY = (m + n + 1) // 2 - middleX
            maxX = float('-inf') if middleX == 0 else nums1[middleX - 1]
            maxY = float('-inf') if middleY == 0 else nums2[middleY - 1]
            minX = float('inf') if middleX == m else nums1[middleX]
            minY = float('inf') if middleY == n else nums2[middleY]
            if maxX <= minY and maxY <= minX:
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = middleX - 1
            else:
                low = middleX + 1