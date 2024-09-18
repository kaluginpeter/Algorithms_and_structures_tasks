# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.
#
#
#
# Example 1:
#
# Input: nums = [10,2]
# Output: "210"
# Example 2:
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109
# Solution
# Python O(NlogN) O(N) Sorting
from functools import cmp_to_key
class Solution:
    def comparison(self, x: str, y: str) -> int:
            """
            For ascending order, ex:
                if x+y > y+x, then y should comes first.
                elif x+y < y+x, then x should comes first.
                else tie, choose any of them.
            """
            if x + y > y + x: return 1
            elif x + y < y + x: return -1
            return 0

    def largestNumber(self, nums: List[int]) -> str:
        answer: str = ''.join(sorted(map(str, nums), reverse=True, key=cmp_to_key(self.comparison)))
        return answer if answer[0] != '0' else '0'