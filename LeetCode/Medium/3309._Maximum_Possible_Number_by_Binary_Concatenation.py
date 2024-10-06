# You are given an array of integers nums of size 3.
#
# Return the maximum possible number whose binary representation can be formed by concatenating the binary representation of all elements in nums in some order.
#
# Note that the binary representation of any number does not contain leading zeros.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
#
# Output: 30
#
# Explanation:
#
# Concatenate the numbers in the order [3, 1, 2] to get the result "11110", which is the binary representation of 30.
#
# Example 2:
#
# Input: nums = [2,8,16]
#
# Output: 1296
#
# Explanation:
#
# Concatenate the numbers in the order [2, 8, 16] to get the result "10100010000", which is the binary representation of 1296.
#
#
#
# Constraints:
#
# nums.length == 3
# 1 <= nums[i] <= 127
# Solution
# Python O(1) O(1) Permutations
class Solution:
    def concatenate(self, a: int, b: int, c: int) -> int:
        return int(bin(a)[2:] + bin(b)[2:] + bin(c)[2:], 2)

    def maxGoodNumber(self, nums: List[int]) -> int:
        a, b, c = nums
        return max(
            self.concatenate(a, b, c),
            self.concatenate(b, a, c),
            self.concatenate(c, b, a),
            self.concatenate(c, a, b),
            self.concatenate(b, c, a),
            self.concatenate(a, c, b),
        )