# You are given a binary string s of length n, where:
#
# '1' represents an active section.
# '0' represents an inactive section.
# You can perform at most one trade to maximize the number of active sections in s. In a trade, you:
#
# Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
# Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
# Return the maximum number of active sections in s after making the optimal trade.
#
# Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.
#
#
#
# Example 1:
#
# Input: s = "01"
#
# Output: 1
#
# Explanation:
#
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.
#
# Example 2:
#
# Input: s = "0100"
#
# Output: 4
#
# Explanation:
#
# String "0100" → Augmented to "101001".
# Choose "0100", convert "101001" → "100001" → "111111".
# The final string without augmentation is "1111". The maximum number of active sections is 4.
# Example 3:
#
# Input: s = "1000100"
#
# Output: 7
#
# Explanation:
#
# String "1000100" → Augmented to "110001001".
# Choose "000100", convert "110001001" → "110000001" → "111111111".
# The final string without augmentation is "1111111". The maximum number of active sections is 7.
# Example 4:
#
# Input: s = "01010"
#
# Output: 4
#
# Explanation:
#
# String "01010" → Augmented to "1010101".
# Choose "010", convert "1010101" → "1000101" → "1111101".
# The final string without augmentation is "11110". The maximum number of active sections is 4.
#
#
# Constraints:
#
# 1 <= n == s.length <= 105
# s[i] is either '0' or '1'
# Solution
# Python O(N) O(1) TwoPointers Prefix Suffix
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        left: int = 0
        middle: int = 0
        right: int = 0
        n: int = len(s)
        prefix: int = 0
        suffix: int = s.count('1')
        output: int = 0
        while middle < n:
            prev_left: int = left
            while left < n and s[left] == '0': left += 1
            left_part: int = left - prev_left
            middle = left
            while middle < n and s[middle] == '1': middle += 1
            middle_part: int = middle - left
            right = middle
            while right < n and s[right] == '0': right += 1
            right_part: int = right - middle
            left = middle
            middle = right
            suffix -= middle_part
            if not left_part or not right_part:
                output = max(output, prefix + middle_part + suffix)
            else:
                output = max(output, prefix + left_part + middle_part + right_part + suffix)
            prefix += middle_part
        return output

# C++ O(N) O(1) Suffix Prefix TwoPointers
class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        size_t left = 0, middle = 0, right = 0;
        size_t n = s.size();
        int output = 0, prefix = 0, suffix = std::count(s.begin(), s.end(), '1');
        while (middle < n) {
            int prevLeft = left;
            while (left < n && s[left] == '0') ++left;
            int leftPart = left - prevLeft;
            middle = left;
            while (middle < n && s[middle] == '1') ++middle;
            int middlePart = middle - left;
            right = middle;
            while (right < n && s[right] == '0') ++right;
            int rightPart = right - middle;
            left = middle;
            middle = right;
            suffix -= middlePart;
            if (!leftPart || !rightPart) output = std::max(output, middlePart + prefix + suffix);
            else output = std::max(output, leftPart + middlePart + rightPart + prefix + suffix);
            prefix += middlePart;
        }
        return output;
    }
};