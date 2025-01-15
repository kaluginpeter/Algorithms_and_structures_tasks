# Given two positive integers num1 and num2, find the positive integer x such that:
#
# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.
#
# Return the integer x. The test cases are generated such that x is uniquely determined.
#
# The number of set bits of an integer is the number of 1's in its binary representation.
#
#
#
# Example 1:
#
# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
# Example 2:
#
# Input: num1 = 1, num2 = 12
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0001 and 1100, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
#
#
# Constraints:
#
# 1 <= num1, num2 <= 109
# Solution
# Python O(logN) O(1) Bit Manipulation
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_bits: int = num1.bit_count()
        num2_bits: int = num2.bit_count()
        if num1_bits == num2_bits: return num1
        elif num1_bits > num2_bits:
            diff: int = num1_bits - num2_bits
            for _ in range(diff):
                num1 &= (num1 - 1)
        else:
            diff: int = num2_bits - num1_bits
            for _ in range(diff):
                num1 |= (num1 + 1)
        return num1

# C++ O(logN) O(1) Bit Manipulation
class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int num1Bits = __builtin_popcount(num1);
        int num2Bits = __builtin_popcount(num2);
        if (num1Bits == num2Bits) return num1;
        if (num1Bits > num2Bits) {
            int diff = num1Bits - num2Bits;
            for (int i = 0; i < diff; ++i) {
                num1 = num1 & (num1 - 1);
            }
        } else {
            int diff = num2Bits - num1Bits;
            for (int i = 0; i < diff; ++i) {
                num1 = num1 | (num1 + 1);
            }
        }
        return num1;
    }
};