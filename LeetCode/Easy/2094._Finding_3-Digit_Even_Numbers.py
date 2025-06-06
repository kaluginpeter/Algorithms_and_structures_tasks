# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
#
# You need to find all the unique integers that follow the given requirements:
#
# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
#
# Return a sorted array of the unique integers.
#
#
#
# Example 1:
#
# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]
# Explanation: All the possible integers that follow the requirements are in the output array.
# Notice that there are no odd integers or integers with leading zeros.
# Example 2:
#
# Input: digits = [2,2,8,8,2]
# Output: [222,228,282,288,822,828,882]
# Explanation: The same digit can be used as many times as it appears in digits.
# In this example, the digit 8 is used twice each time in 288, 828, and 882.
# Example 3:
#
# Input: digits = [3,7,5]
# Output: []
# Explanation: No even integers can be formed using the given digits.
#
#
# Constraints:
#
# 3 <= digits.length <= 100
# 0 <= digits[i] <= 9
# Solution Simulation O(1) O(1)
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output: list[int] = list()
        digits_count: list[int] = [0] * 10
        for digit in digits:
            digits_count[digit] += 1
        even_digits: list[int] = [i for i in range(0, 10, 2) if digits_count[i] > 0]
        if len(even_digits) == 0: return output
        for first_digit in range(10):
            if first_digit != 0 and digits_count[first_digit] > 0:
                digits_count[first_digit] -= 1
                for second_digit in range(10):
                    if digits_count[second_digit] > 0:
                        digits_count[second_digit] -= 1
                        for third_digit in even_digits:
                            if digits_count[third_digit] > 0:
                                digit: int = first_digit * 100 + second_digit * 10 + third_digit
                                output.append(digit)
                        digits_count[second_digit] += 1
                digits_count[first_digit] += 1
        return output

# Python O(N^3) O(N^3) Combinatorics
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        output: list[int] = []
        first, second, third = set(), set(), set()
        n: int = len(digits)
        for i in range(n):
            if not digits[i] or digits[i] in first: continue
            for j in range(n):
                if j == i or digits[j] in second: continue
                for k in range(n):
                    if k in [i, j] or digits[k] & 1 or digits[k] in third: continue
                    output.append(digits[i] * 100 + digits[j] * 10 + digits[k])
                    first.add(digits[i])
                    second.add(digits[j])
                    third.add(digits[k])
                third.clear()
            second.clear()
        return output

# C++ O(N^3) O(N^3) Combinatorics
class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        int n = digits.size();
        sort(digits.begin(), digits.end());
        vector<int> output;
        unordered_set<int> first, second, third;
        for (int i = 0; i < n; ++i) {
            if (!digits[i]) continue;
            else if (first.count(digits[i])) continue;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                else if (second.count(digits[j])) continue;
                for (int k = 0; k < n; ++k) {
                    if ((digits[k] & 1) == 1) continue;
                    else if (k == i || k == j) continue;
                    else if (third.count(digits[k])) continue;
                    output.push_back(digits[i] * 100 + digits[j] * 10 + digits[k]);
                    first.insert(digits[i]);
                    second.insert(digits[j]);
                    third.insert(digits[k]);
                }
                third.clear();
            }
            second.clear();
        }
        return output;
    }
};