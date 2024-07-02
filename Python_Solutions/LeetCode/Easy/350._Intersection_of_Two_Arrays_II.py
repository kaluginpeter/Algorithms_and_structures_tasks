# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows
# in both arrays and you may return the result in any order.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
#
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk,
# and the memory is limited such that you cannot load all elements into the memory at once?
# Solution O(N**3) O(N)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        while nums1:
            for i in nums1:
                if i in nums2:
                    l.append(i)
                    nums1.remove(i)
                    nums2.remove(i)
                    continue
                nums1.remove(i)
        return l


# Questions:
# What if the given array is already sorted? How would you optimize your algorithm?
# Answer: Insted of using extra space for creation hashmap for each array we can use Two Pointers or Binary Search approaches.
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# Answer: Binary Search approach will works better than Two pointers, because we don't need to traverse between all second array for finding element. We can juse do int in "log time".
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# Answer: So we can use Binary Search approach to be able make more efficient operations on memory disk.

# HashTable Counting
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        boundary_nums1: int = len(nums1)
        boundary_nums2: int = len(nums2)
        storage_nums1: dict[int, int] = defaultdict(int)
        storage_nums2: dict[int, int] = defaultdict(int)
        duplicate: list[int] = []
        idx: int = 0
        while idx < boundary_nums1:
            storage_nums1[nums1[idx]] += 1
            idx += 1
        idx = 0
        while idx < boundary_nums2:
            storage_nums2[nums2[idx]] += 1
            idx += 1
        for num in storage_nums1:
            if num in storage_nums2:
                duplicate.extend([num] * min(storage_nums1[num], storage_nums2[num]))
        return duplicate

# Two Pointers
# Complexity
# Time complexity: O(NlogN), because in problem case arrays not sorted and we need to sort them, if array being already sorted, time complexity equals to O(N)
# Space complexity: O(N), because we use output array to store duplicate numbers
# Code
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        duplicate: list[int] = []
        pointer_nums1 = pointer_nums2 = 0
        while pointer_nums1 < len(nums1) and pointer_nums2 < len(nums2):
            if nums1[pointer_nums1] == nums2[pointer_nums2]:
                duplicate.append(nums1[pointer_nums1])
                pointer_nums1 += 1
                pointer_nums2 += 1
            elif nums1[pointer_nums1] > nums2[pointer_nums2]:
                pointer_nums2 += 1
            else:
                pointer_nums1 += 1
        return duplicate

# Binary Search
# Complexity
# Time complexity: O(NlogN), because in problem case arrays not sorted and we need to sort them, if array being already sorted, time complexity equals to O(N)
# Space complexity: O(N), because we use output array to store duplicate numbers
# Code
class Solution:
    def leftmost_binary_search(self, sequence: list[int], target: int) -> int:
        left_pointer, right_pointer = 0, len(sequence) - 1
        while left_pointer <= right_pointer:
            middle_pointer: int = (left_pointer + right_pointer) >> 1
            if sequence[middle_pointer] >= target:
                right_pointer = middle_pointer - 1
            else:
                left_pointer = middle_pointer + 1
        return right_pointer + 1

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        duplicate: list[int] = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        upper_boundary: int = len(nums1)
        lower_boundary: int = 0
        upper_search_boundary: int = len(nums2)
        while lower_boundary < upper_boundary:
            target: int = nums1[lower_boundary]
            start_pointer: int = self.leftmost_binary_search(nums2, target)
            frequences_in_second_array: int = 0
            while start_pointer < upper_search_boundary and nums2[start_pointer] == target:
                frequences_in_second_array += 1
                start_pointer += 1
            frequences_in_first_array: int = 0
            while lower_boundary < upper_boundary and nums1[lower_boundary] == target:
                frequences_in_first_array += 1
                lower_boundary += 1
            if frequences_in_second_array > 0:
                duplicate.extend([target] * min(frequences_in_first_array, frequences_in_second_array))
        return duplicate