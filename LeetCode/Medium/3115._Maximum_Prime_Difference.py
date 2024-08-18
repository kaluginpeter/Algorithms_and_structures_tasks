# You are given an integer array nums.
#
# Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.
#
#
#
# Example 1:
#
# Input: nums = [4,2,9,5,3]
#
# Output: 3
#
# Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.
#
# Example 2:
#
# Input: nums = [4,8,2,8]
#
# Output: 0
#
# Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 105
# 1 <= nums[i] <= 100
# The input is generated such that the number of prime numbers in the nums is at least one.
# Solution Straight Forward Checking Math O(NlogN) O(1)
class Solution:
    from math import sqrt
    def isPrime(self, n: int) -> bool:
        prime_flag = 0
        if (n > 1):
            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return True
            else:
                return False
        return False

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        x, y = None, None
        for i in range(len(nums)):
            if self.isPrime(nums[i]):
                if x is None:
                    x = i
                else:
                    y = i
        return 0 if y is None else y - x