# An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. For example:
#
# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].
#
#
#
# Example 1:
#
# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Example 2:
#
# Input: n = 1
# Output: 0
# Example 3:
#
# Input: n = 2
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 104
# Solution
# Python O(NlogN) O(1) Math
class Solution:
    def rotatedDigits(self, n: int) -> int:
        output: int = 0
        repeated: set[int] = {0, 1, 8}
        accepted: set[int] = repeated | {2, 5, 6, 9}
        for X in range(1, n + 1):
            x: int = X
            is_valid: bool = True
            different: bool = False
            while x:
                if x % 10 not in repeated: different = True
                if x % 10 not in accepted:
                    is_valid = False
                    break
                x //= 10
            if is_valid and different: output += 1
        return output

# C++ O(NlogN) O(1) Math
class Solution {
public:
    int rotatedDigits(int n) {
        int output = 0;
        for (int X = 1; X <= n; ++X) {
            int x = X;
            bool isValid = true, different = false;
            while (x) {
                if (x % 10 != 0 && x % 10 != 1 && x % 10 != 8) different = true;
                if (x % 10 != 0 && x % 10 != 1 && x % 10 != 8 && x % 10 != 2 && x % 10 != 5 && x % 10 != 6 && x % 10 != 9) {
                    isValid = false;
                    break;
                }
                x /= 10;
            }
            if (isValid && different) ++output;
        }
        return output;
    }
};