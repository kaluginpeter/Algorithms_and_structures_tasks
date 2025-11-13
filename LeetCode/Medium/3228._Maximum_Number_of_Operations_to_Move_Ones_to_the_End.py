# You are given a
# binary string
#  s.
#
# You can perform the following operation on the string any number of times:
#
# Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
# Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
# Return the maximum number of operations that you can perform.
#
#
#
# Example 1:
#
# Input: s = "1001101"
#
# Output: 4
#
# Explanation:
#
# We can perform the following operations:
#
# Choose index i = 0. The resulting string is s = "0011101".
# Choose index i = 4. The resulting string is s = "0011011".
# Choose index i = 3. The resulting string is s = "0010111".
# Choose index i = 2. The resulting string is s = "0001111".
# Example 2:
#
# Input: s = "00111"
#
# Output: 0
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
# General idea:
# Calculate how many ones you have staring from 0 index to end of string.
# Id current char is "1" - increment ones
# At each iteration mark boolean "move" variable to False
# If you need move to next '1' character, mark boolean "move" variable on True
# If "move" variable is True - add count of ones to total score
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def maxOperations(self, s: str) -> int:
        score: int = 0
        ones: int = 0

        idx: int = 0
        while idx < len(s):
            if s[idx] == '1':
                ones += 1
                idx += 1

            move: bool = False
            while idx < len(s) and s[idx] != '1':
                idx += 1
                move = True

            if move:
                score += ones
        return score


# Python O(N) O(1) TwoPointers
class Solution:
    def maxOperations(self, s: str) -> int:
        output: int = 0
        ones: int = 0
        left: int = 0
        right: int = 0
        n: itn = len(s)
        while right < n:
            while right < n and s[right] == '0': right += 1
            while left < right:
                if s[left] == '1': ones += 1
                left += 1
            output += ones
            while right < n and s[right] == '1': right += 1
        return output

# C++ O(N) O(1) TwoPointers
class Solution {
public:
    int maxOperations(string s) {
        int output = 0, ones = 0;
        size_t left = 0, right = 0, n = s.size();
        while (right < n) {
            while (right < n && s[right] == '0') ++right;
            while (left < right) {
                if (s[left] == '1') ++ones;
                ++left;
            }
            output += ones;
            while (right < n && s[right] == '1') ++right;
        }
        return output;
    }
};