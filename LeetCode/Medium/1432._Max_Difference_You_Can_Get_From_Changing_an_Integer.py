# You are given an integer num. You will apply the following steps to num two separate times:
#
# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). Note y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.
#
# Return the max difference between a and b.
#
# Note that neither a nor b may have any leading zeros, and must not be 0.
#
#
#
# Example 1:
#
# Input: num = 555
# Output: 888
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888
# Example 2:
#
# Input: num = 9
# Output: 8
# Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
# The second time pick x = 9 and y = 1 and store the new integer in b.
# We have now a = 9 and b = 1 and max difference = 8
#
#
# Constraints:
#
# 1 <= num <= 108
# Solution
# Python O(log10(N)) O(log10(N)) Math
class Solution:
    def build_number(self, from_: int, to: int, digits: list[int], original: int) -> int:
        number: int = 0
        for i in range(len(digits) - 1, -1, -1):
            if i + 1 == len(digits) and not to and digits[i] == from_: return original
            number = number * 10 + (to if digits[i] == from_ else digits[i])
        return number

    def maxDiff(self, num: int) -> int:
        digits: list[int] = []
        num_: int = num
        while num_:
            digits.append(num_ % 10)
            num_ //= 10
        max_number: int = num
        min_number: int = num
        for x in range(10):
            for y in range(10):
                new_number: int = self.build_number(x, y, digits, num)
                max_number = max(max_number, new_number)
                min_number = min(min_number, new_number)
        return max_number - min_number

# C++ O(log10(N)) O(log10(N)) Math
class Solution {
public:
    int buildNumber(int &from, int &to, std::vector<int> &digits, int &original) {
        int number = 0;
        for (int i = digits.size() - 1; i >= 0; --i) {
            if (!to && i + 1 == digits.size() && digits[i] == from) return original;
            number = number * 10 + (digits[i] == from ? to : digits[i]);
        }
        return number;
    }

    int maxDiff(int num) {
        vector<int> digits;
        int num_ = num;
        while (num_) {
            digits.push_back(num_ % 10);
            num_ /= 10;
        }
        int maxValue = num, minValue = num;
        for (int x = 0; x < 10; ++x) {
            for (int y = 0; y < 10; ++y) {
                int newNumber = buildNumber(x, y, digits, num);
                maxValue = std::max(maxValue, newNumber);
                minValue = std::min(minValue, newNumber);
            }
        }
        return maxValue - minValue;
    }
};