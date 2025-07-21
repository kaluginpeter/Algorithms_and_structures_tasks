# A fancy string is a string where no three consecutive characters are equal.
#
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
#
# Return the final string after the deletion. It can be shown that the answer will always be unique.
#
#
#
# Example 1:
#
# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
# Example 2:
#
# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".
# Example 3:
#
# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists only of lowercase English letters.
# Solution
# Python O(N) O(N) Two Pointers
class Solution:
    def makeFancyString(self, s: str) -> str:
        output: list[str] = []
        left: int = 0
        for right in range(len(s)):
            if s[left] != s[right]:
                output.append(s[right])
                left = right
            elif right - left + 1 <= 2:
                output.append(s[right])
        return ''.join(output)

# C++ O(N) O(N) Two Pointers
class Solution {
public:
    string makeFancyString(string s) {
        std::string output = "";
        int left = 0;
        for (int right = 0; right < s.size(); ++right) {
            if (s[left] != s[right]) {
                output += s[right];
                left = right;
            } else if (right - left + 1 <= 2) {
                output += s[right];
            }
        }
        return output;
    }
};


# Python O(N) O(N) String TwoPointers
class Solution:
    def makeFancyString(self, s: str) -> str:
        output: list[str] = []
        left: int = 0
        for right in range(len(s)):
            if s[left] == s[right]:
                if right - left + 1 == 3:
                    left += 1
                    continue
            else: left = right
            output.append(s[right])
        return ''.join(output)

# C++ O(N) O(N) TwoPointers String
class Solution {
public:
    string makeFancyString(string s) {
        std::string output = "";
        int left = 0;
        for (int right = 0; right < s.size(); ++right) {
            if (s[left] == s[right]) {
                if (right - left + 1 == 3) {
                    ++left;
                    continue;
                }
            } else left = right;
            output.push_back(s[right]);
        }
        return output;
    }
};