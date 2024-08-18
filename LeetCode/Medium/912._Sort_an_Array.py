# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
# and with the smallest space complexity possible.
#
# Example 1:
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
# while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#
# Constraints:
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
# Solution
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(l, r):
            if l >= r:
                return
            x = nums[randint(l, r)]
            i, j, k = l - 1, r + 1, l
            while k < j:
                if nums[k] < x:
                    nums[i + 1], nums[k] = nums[k], nums[i + 1]
                    i, k = i + 1, k + 1
                elif nums[k] > x:
                    j -= 1
                    nums[j], nums[k] = nums[k], nums[j]
                else:
                    k = k + 1
            quick_sort(l, i)
            quick_sort(j, r)
        quick_sort(0, len(nums) - 1)
        return nums

# Merge Sort
# Complexity
# Time complexity: O(NlogN)
# Space complexity: O(N)
# Code
class Solution:
    def merge_sort(self, arr: list[int]) -> list[int]:
        n: int = len(arr)
        if n <= 1:
            return arr
        middle: int = n >> 1
        left_part: list[int] = self.merge_sort(arr[:middle])
        right_part: list[int] = self.merge_sort(arr[middle:])
        output: list[int] = []
        n_left, n_right = len(left_part), len(right_part)
        left_idx = right_idx = 0
        while left_idx < n_left and right_idx < n_right:
            if left_part[left_idx] < right_part[right_idx]:
                output.append(left_part[left_idx])
                left_idx += 1
            else:
                output.append(right_part[right_idx])
                right_idx += 1
        return output + left_part[left_idx:] + right_part[right_idx:]

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

# Counting Sort
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
class Solution:
    def counting_sort(self, arr: list[int]) -> list[int]:
        storage: list[int] = [0] * 100_001
        for num in arr:
            storage[num + 50_000] += 1
        output: list[int] = []
        for num in range(100_001):
            if storage[num]:
                output.extend([num - 50_000] * storage[num])
        return output

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.counting_sort(nums)