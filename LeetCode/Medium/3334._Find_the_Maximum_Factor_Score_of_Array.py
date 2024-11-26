# You are given an integer array nums.
#
# The factor score of an array is defined as the product of the LCM and GCD of all elements of that array.
#
# Return the maximum factor score of nums after removing at most one element from it.
#
# Note that both the
# LCM
#  and
# GCD
#  of a single number are the number itself, and the factor score of an empty array is 0.
#
#
#
# Example 1:
#
# Input: nums = [2,4,8,16]
#
# Output: 64
#
# Explanation:
#
# On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of 4 * 16 = 64.
#
# Example 2:
#
# Input: nums = [1,2,3,4,5]
#
# Output: 60
#
# Explanation:
#
# The maximum factor score of 60 can be obtained without removing any elements.
#
# Example 3:
#
# Input: nums = [3]
#
# Output: 9
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 30
# Solution
# Python O(N**2) O(N) Math
def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def gcd_of_list(numbers):
    return reduce(gcd, numbers)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] * nums[0]
        max_output: int = gcd_of_list(nums) * lcm_of_list(nums)
        for idx in range(len(nums)):
            second = nums[:idx] + nums[idx + 1:]
            max_output = max(max_output, gcd_of_list(second) * lcm_of_list(second))
        return max_output