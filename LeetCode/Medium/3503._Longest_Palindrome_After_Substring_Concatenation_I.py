# You are given two strings, s and t.
#
# You can create a new string by selecting a substring from s (possibly empty) and a substring from t (possibly empty), then concatenating them in order.
#
# Return the length of the longest palindrome that can be formed this way.
#
# A substring is a contiguous sequence of characters within a string.
#
# A palindrome is a string that reads the same forward and backward.
#
#
#
# Example 1:
#
# Input: s = "a", t = "a"
#
# Output: 2
#
# Explanation:
#
# Concatenating "a" from s and "a" from t results in "aa", which is a palindrome of length 2.
#
# Example 2:
#
# Input: s = "abc", t = "def"
#
# Output: 1
#
# Explanation:
#
# Since all characters are different, the longest palindrome is any single character, so the answer is 1.
#
# Example 3:
#
# Input: s = "b", t = "aaaa"
#
# Output: 4
#
# Explanation:
#
# Selecting "aaaa" from t is the longest palindrome, so the answer is 4.
#
# Example 4:
#
# Input: s = "abcde", t = "ecdba"
#
# Output: 5
#
# Explanation:
#
# Concatenating "abc" from s and "ba" from t results in "abcba", which is a palindrome of length 5.
#
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 30
# s and t consist of lowercase English letters.
# Solution
# Python O(N**5) O(N + M) String
class Solution:
    def is_palindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            if s[left] != s[right]: return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s: str, t: str) -> int:
        output: int = 0
        for s_l in range(len(s)):
            for s_r in range(s_l, len(s) + 1):
                for t_l in range(len(t)):
                    for t_r in range(t_l, len(t) + 1):
                        if self.is_palindrome(s[s_l:s_r] + t[t_l:t_r]):
                            output = max(output, (s_r - s_l) + (t_r - t_l))
        return output

# C++ O(N**5) O(N + M) String
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            ++left;
            --right;
        }
        return true;
    }

    int longestPalindrome(string s, string t) {
        int n = s.size(), m = t.size();
        int output = 0;
        for (int sL = 0; sL < n; ++sL) {
            for (int sR = sL; sR <= n; ++sR) {
                for (int tL = 0; tL < m; ++tL) {
                    for (int tR = tL; tR <= m; ++tR) {
                        if (isPalindrome(s.substr(sL, sR - sL) + t.substr(tL, tR - tL))) {
                            output = max(output, (sR - sL) + (tR - tL));
                        }
                    }
                }
            }
        }
        return output;
    }
};