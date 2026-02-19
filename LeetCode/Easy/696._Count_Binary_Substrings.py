# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
#
#
#
# Example 1:
#
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
#
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
# Solution
# Python O(N) O(1) SlidingWindow
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n: int = len(s)
        left: int = 0
        right: int = 0
        zeros: int = 0
        ones: int = 0
        output: int = 0
        while right < n:
            while right < n and s[left] == s[right]: right += 1
            if s[left] == '1': ones = right - left
            else: zeros = right - left
            output += min(zeros, ones)
            left = right
        return output

# C++ O(N) O(1) SlidingWindow
class Solution {
public:
    int countBinarySubstrings(string s) {
        int n = s.size(), output = 0;
        int left = 0, right = 0;
        int ones = 0, zeros = 0;
        while (right < n) {
            while (right < n && s[left] == s[right]) ++right;
            if (s[left] == '1') ones = right - left;
            else zeros = right - left;
            output += std::min(zeros, ones);
            left = right;
        }
        return output;
    }
};