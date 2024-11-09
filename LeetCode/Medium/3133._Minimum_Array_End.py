# You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.
#
# Return the minimum possible value of nums[n - 1].
#
#
#
# Example 1:
#
# Input: n = 3, x = 4
#
# Output: 6
#
# Explanation:
#
# nums can be [4,5,6] and its last element is 6.
#
# Example 2:
#
# Input: n = 2, x = 7
#
# Output: 15
#
# Explanation:
#
# nums can be [7,15] and its last element is 15.
#
#
#
# Constraints:
#
# 1 <= n, x <= 108
# Solution
# Python O(logN) O(1) Bit Manipulation
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result: int = x
        n -= 1
        mask: int = 1
        while n:
            if mask & x == 0:
                result |= (n & 1) * mask
                n >>= 1
            mask <<= 1
        return result

# C++ O(logN) O(1) Bit Manipulation
class Solution {
public:
    long long minEnd(int n, long long x) {
        long long result = x;
        --n;
        for (long long mask = 1; n > 0; mask <<= 1) {
            if ((mask & x) == 0) {
                result |= (n & 1) * mask;
                n >>= 1;
            }
        }
        return result;
    }
};