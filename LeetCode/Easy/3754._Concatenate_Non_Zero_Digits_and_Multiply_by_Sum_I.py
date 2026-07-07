# You are given an integer n.
#
# Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.
#
# Let sum be the sum of digits in x.
#
# Return an integer representing the value of x * sum.
#
#
#
# Example 1:
#
# Input: n = 10203004
#
# Output: 12340
#
# Explanation:
#
# The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
# The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
# Therefore, the answer is x * sum = 1234 * 10 = 12340.
# Example 2:
#
# Input: n = 1000
#
# Output: 1
#
# Explanation:
#
# The non-zero digit is 1, so x = 1 and sum = 1.
# Therefore, the answer is x * sum = 1 * 1 = 1.
#
#
# Constraints:
#
# 0 <= n <= 109
# Solution
# Python O(log10(N)) O(1) Math
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        output: int = 0
        tmp: int = 0
        acc: int = 0
        while n:
            tmp = tmp * 10 + n % 10
            acc += n % 10
            n //= 10
        while tmp:
            if tmp % 10: output = output * 10 + tmp % 10
            tmp //= 10
        return output * acc

# C++ O(log10(N)) O(1) Math
class Solution {
public:
    long long sumAndMultiply(int n) {
        long long output = 0;
        uint8_t acc = 0;
        long long tmp = 0;
        while (n) {
            tmp = tmp * 10 + n % 10;
            acc += n % 10;
            n /= 10;
        }
        while (tmp) {
            if (tmp % 10) output = output * 10 + tmp % 10;
            tmp /= 10;
        }
        return output * acc;
    }
};