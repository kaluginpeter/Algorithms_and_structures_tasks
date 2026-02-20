# Special binary strings are binary strings with the following two properties:
#
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# You are given a special binary string s.
#
# A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.
#
# Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.
#
#
#
# Example 1:
#
# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.
# Example 2:
#
# Input: s = "10"
# Output: "10"
#
#
# Constraints:
#
# 1 <= s.length <= 50
# s[i] is either '0' or '1'.
# s is a special binary string.
#
# Solution
# Python O(N^2) O(N^2) String
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        n: int = len(s)
        one: int = 0
        zero: int = 0
        i: int = 0
        build: list[str] = []
        for j in range(n):
            if s[j] == '1': one += 1
            else: zero += 1
            if one == zero:
                build.append('1' + self.makeLargestSpecial(s[i + 1: j]) + '0')
                i = j + 1
        build.sort(reverse=True)
        return ''.join(build)

# C++ O(N^2) O(N^2) Sorting
class Solution {
public:
    string makeLargestSpecial(string s) {
        int i = 0, one = 0, zero = 0;
        int n = s.size();
        std::vector<std::string> build;
        for (int j = 0; j < n; ++j) {
            if (s[j] == '1') ++one;
            else ++zero;
            if (one == zero) {
                build.push_back('1' + makeLargestSpecial(s.substr(i + 1, j - i - 1)) + '0');
                i = j + 1;
            }
        }
        std::sort(build.rbegin(), build.rend());
        std::string output = "";
        for (auto& str : build) output += str;
        return output;
    }
};