# Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.
#
# Return the length of n. If there is no such n, return -1.
#
# Note: n may not fit in a 64-bit signed integer.
#
#
#
# Example 1:
#
# Input: k = 1
# Output: 1
# Explanation: The smallest answer is n = 1, which has length 1.
# Example 2:
#
# Input: k = 2
# Output: -1
# Explanation: There is no such positive integer n divisible by 2.
# Example 3:
#
# Input: k = 3
# Output: 3
# Explanation: The smallest answer is n = 111, which has length 3.
#
#
# Constraints:
#
# 1 <= k <= 105
# Solution
# Python O(K) O(1) Math
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        tmp: int = 1
        output: int = 1
        while tmp % k != 0:
            output += 1
            tmp = (tmp * 10 + 1) % k
            if output >= k: break
        return output if tmp % k == 0 else -1

# C++ O(K) O(1) Math
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        long long tmp = 1;
        int output = 1;
        while (tmp % k != 0) {
            ++output;
            tmp = (tmp * 10 + 1) % k;
            if (output >= k) break;
        }
        return (tmp % k == 0 ? output : -1);
    }
};