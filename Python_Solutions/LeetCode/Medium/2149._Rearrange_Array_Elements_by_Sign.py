# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
#
# You should rearrange the elements of nums such that the modified array follows the given conditions:
#
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
#
#
#
# Example 1:
#
# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.
# Example 2:
#
# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].
#
#
# Constraints:
#
# 2 <= nums.length <= 2 * 105
# nums.length is even
# 1 <= |nums[i]| <= 105
# nums consists of equal number of positive and negative integers.
# Solution Two Pointers O(N) O(N)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        arr_int: list = [0] * n
        left, right = 0, n // 2
        for i in range(n):
            if nums[i] > 0:
                arr_int[left] = nums[i]
                left += 1
            else:
                arr_int[right] = nums[i]
                right += 1
        left, right = 0, n // 2
        for i in range(0, n, 2):
            nums[i] = arr_int[left]
            nums[i+1] = arr_int[right]
            left, right = left + 1, right + 1
        return nums