# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# If multiple answers are possible, return any of them.
#
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
#
#
#
# Example 1:
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
#
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
#
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
#
#
# Constraints:
#
# -231 <= numerator, denominator <= 231 - 1
# denominator != 0
# Solution
# Python O(logN) O(logN) HashMap
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator: return '0'
        fraction: list[str] = []
        if (numerator < 0) ^ (denominator < 0): fraction.append('-')
        dividend: int = abs(numerator)
        divisor: int = abs(denominator)
        fraction.append(str(dividend // divisor))
        remainder: int = dividend % divisor
        if not remainder: return ''.join(fraction)
        fraction.append('.')
        seen: dict[int, int] = dict()
        while remainder:
            if remainder in seen:
                fraction.insert(seen[remainder], '(')
                fraction.append(')')
                break
            else:
                seen[remainder] = len(fraction)
                remainder *= 10
                fraction.append(str(remainder // divisor))
                remainder %= divisor
        return ''.join(fraction)

# C++ O(logN) O(logN) HashMap
class Solution {
public:
    std::string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        std::string fraction = "";
        if ((numerator < 0) ^ (denominator < 0)) fraction.push_back('-');
        long long dividend = std::llabs(static_cast<long long>(numerator));
        long long divisor = std::llabs(static_cast<long long>(denominator));
        fraction += std::to_string(dividend / divisor);
        long long remainder = dividend % divisor;
        if (remainder == 0) return fraction;
        fraction.push_back('.');
        std::unordered_map<long long, int> seen;
        while (remainder) {
            if (seen.count(remainder)) {
                fraction.insert(seen[remainder], "(");
                fraction.push_back(')');
                break;
            }
            seen[remainder] = fraction.size();
            remainder *= 10;
            fraction += std::to_string(remainder / divisor);
            remainder %= divisor;
        }
        return fraction;
    }
};