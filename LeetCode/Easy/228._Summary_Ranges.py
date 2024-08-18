# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
#
# Example 1:
#
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:
#
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
# Constraints:
# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.
# Solution
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        l, a, b, flag = [], -1, -1, False
        for i in range(len(nums)):
            if not flag:
                a, b = nums[i], nums[i]
            if i + 1 < len(nums):
                if nums[i+1] - nums[i] == 1:
                    b, flag = nums[i+1], True
                    continue
                flag = False
            l.append(str(a) if a == b else str(a) + '->' + str(b))
        return l

# Two Pointers O(N) O(N)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output: list[str] = []
        if not nums: return output
        left = right = 0
        for idx in range(1, len(nums)):
            if nums[idx] - 1 == nums[right]:
                right += 1
            else:
                if left == right:
                    output.append(str(nums[left]))
                else:
                    output.append(f'{nums[left]}->{nums[right]}')
                left = right = idx
        if left == right:
            output.append(str(nums[left]))
        else:
            output.append(f'{nums[left]}->{nums[right]}')
        return output
