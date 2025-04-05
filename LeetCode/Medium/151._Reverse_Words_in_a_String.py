# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
#
#
#
# Example 1:
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
#
#
# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
# Solution
# Python O(N) O(N) Two Pointers String
# Memory Complexity here is O(N), because we transform string to list of strings
# But we do so, for making string in Python kinda "changeable"
class Solution:
    def reverseWords(self, s: str) -> str:
        s: list[str] = list(s)
        n: int = len(s)
        left, right = 0, n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        current: int = 0
        for idx in range(n):
            if s[idx] == ' ':
                if current and s[current - 1] != ' ': current += 1
            else:
                if current < idx:
                    s[current] = s[idx]
                    s[idx] = ' '
                current += 1
        left = 0
        for idx in range(n):
            if s[idx] == ' ':
                right: int = idx - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                left = idx + 1
                current = left
        right = n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        while s and s[-1] == ' ': s.pop()
        return ''.join(s)

# C++ O(N) O(1) TwoPointers String
class Solution {
public:
    string reverseWords(string s) {
        int n = s.size(), left = 0, right = n - 1;
        // Reverse entire string
        while (left < right) {
            swap(s[left], s[right]);
            ++left;
            --right;
        }
        // Shift all words to begging of a string separated by single whitespace
        int current = 0;
        for (int idx = 0; idx < n; ++idx) {
            if (isspace(s[idx])) {
                if (current && !isspace(s[current - 1])) ++current;
            } else {
                if (current < idx) {
                    s[current] = s[idx];
                    s[idx] = ' ';
                }
                ++current;
            }
        }
        // Reverse each word by itself
        left = 0;
        for (int idx = 0; idx < n; ++idx) {
            if (isspace(s[idx])) {
                int right = idx - 1;
                while (left < right) {
                    swap(s[left], s[right]);
                    ++left;
                    --right;
                }
                left = idx + 1;
            }
        }
        right = n - 1;
        while (left < right) {
            swap(s[left], s[right]);
            ++left;
            --right;
        }
        // Delete redundant whitespace at the end of the string
        while (!s.empty() && isspace(s.back())) s.pop_back();
        return s;
    }
};