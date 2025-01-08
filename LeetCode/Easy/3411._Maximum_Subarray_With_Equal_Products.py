# You are given an array of positive integers nums.
#
# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
#
# prod(arr) is the product of all elements of arr.
# gcd(arr) is the
# GCD
#  of all elements of arr.
# lcm(arr) is the
# LCM
#  of all elements of arr.
# Return the length of the longest product equivalent
# subarray
#  of nums.
#
#
#
# Example 1:
#
# Input: nums = [1,2,1,2,1,1,1]
#
# Output: 5
#
# Explanation:
#
# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.
#
# Example 2:
#
# Input: nums = [2,3,4,5,6]
#
# Output: 3
#
# Explanation:
#
# The longest product equivalent subarray is [3, 4, 5].
#
# Example 3:
#
# Input: nums = [1,2,3,1,4,5,1]
#
# Output: 5
#
#
#
# Constraints:
#
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10
# Solution
# Python O(N**2) O(1) Brute Force
import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_length: int = 0
        n: int = len(nums)
        for i in range(n):
            current_gcd: int = nums[i]
            current_lcm: int = nums[i]
            for j in range(i, n):
                if j > i:
                    current_gcd = math.gcd(current_gcd, nums[j])
                    current_lcm = (current_lcm * nums[j]) // math.gcd(current_lcm, nums[j])
                if current_lcm * current_gcd == math.prod(nums[i:j + 1]):
                    max_length = max(max_length, j - i + 1)
        return max_length

# C++ O(N**2) O(1) Brute Force
class Solution {
public:
    int maxLength(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < nums.size(); ++i) {
            unsigned long long gcdVal = nums[i], lcmVal = nums[i], prod = 1, maxLcm = 100000000000;
            for(int j = i; j < nums.size(); ++j) {
                prod = prod * (long long)nums[j];
                gcdVal = gcd(gcdVal, (long long)nums[j]);
                lcmVal = lcm(lcmVal, (long long)nums[j]);
                if (prod == gcdVal * lcmVal) {
                    ans = max(ans, j - i + 1);
                }
            }
        }
        return ans;
    }
};