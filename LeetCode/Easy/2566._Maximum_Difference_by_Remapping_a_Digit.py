# You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
#
# Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.
#
# Notes:
#
# When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
# Bob can remap a digit to itself, in which case num does not change.
# Bob can remap different digits for obtaining minimum and maximum values respectively.
# The resulting number after remapping can contain leading zeroes.
#
#
# Example 1:
#
# Input: num = 11891
# Output: 99009
# Explanation:
# To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
# To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
# The difference between these two numbers is 99009.
# Example 2:
#
# Input: num = 90
# Output: 99
# Explanation:
# The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
# Thus, we return 99.
#
#
# Constraints:
#
# 1 <= num <= 108
# Solution
# Python O(log10(N)) O(log10(N)) Greedy
class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits: list[int] = []
        while num:
            digits.append(num % 10)
            num //= 10
        max_value: int = 0
        min_value: int = 0
        n: int = len(digits)
        right: int = n - 1
        while right >= 0 and digits[right] == 9: right -= 1
        target: int = digits[right] if right >= 0 else 9
        for i in range(n - 1, -1, -1):
            max_value = max_value * 10 + (9 if digits[i] == target else digits[i])
        target = digits[n - 1]
        for i in range(n - 1, -1, -1):
            min_value = min_value * 10 + (0 if digits[i] == target else digits[i])
        return max_value - min_value

# C++ O(log10(N)) O(log10(N)) Greedy
class Solution {
public:
    int minMaxDifference(int num) {
        std::vector<int> digits;
        while (num) {
            digits.push_back(num % 10);
            num /= 10;
        }
        int maxValue = 0, minValue = 0;
        int n = digits.size(), right = n - 1;
        while (right >= 0 && digits[right] == 9) --right;
        int target = (right >= 0 ? digits[right] : 9);
        for (int i = n - 1; i >= 0; --i) {
            maxValue = maxValue * 10 + (digits[i] == target ? 9 : digits[i]);
        }
        target = digits[n - 1];
        for (int i = n - 1; i >= 0; --i) {
            minValue = minValue * 10 + (digits[i] == target ? 0 : digits[i]);
        }
        return maxValue - minValue;
    }
};