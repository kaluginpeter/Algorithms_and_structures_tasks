# A parentheses string is valid if and only if:
#
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
#
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.
#
#
#
# Example 1:
#
# Input: s = "())"
# Output: 1
# Example 2:
#
# Input: s = "((("
# Output: 3
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.
# Solution
# C++ O(N) O(1) Stack Greedy Counting
class Solution {
public:
    int minAddToMakeValid(string s) {
        int open_br = 0, close_br = 0;
        int count = 0;
        for (size_t index = 0; index < s.size(); ++index) {
            if (s[index] == '(') {
                open_br += 1;
            } else {
                close_br += 1;
                if (close_br > open_br) {
                    close_br -= 1;
                    count += 1;
                }
            }
        }
        return count + std::max(open_br - close_br, 0);
    }
};

# Python O(N) O(1) Counting Greedy Stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_br: int = 0
        close_br: int = 0
        count: int = 0
        for brace in s:
            if brace == '(':
                open_br += 1
            else: close_br += 1
            if close_br > open_br:
                count += 1
                close_br -= 1
        return count + max(open_br - close_br, 0)