# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
#
# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,
#
# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.
#
#
#
# Example 1:
#
#
# Input: s = "))()))", locked = "010100"
# Output: true
# Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
# We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
# Example 2:
#
# Input: s = "()()", locked = "0000"
# Output: true
# Explanation: We do not need to make any changes because s is already valid.
# Example 3:
#
# Input: s = ")", locked = "0"
# Output: false
# Explanation: locked permits us to change s[0].
# Changing s[0] to either '(' or ')' will not make s valid.
#
#
# Constraints:
#
# n == s.length == locked.length
# 1 <= n <= 105
# s[i] is either '(' or ')'.
# locked[i] is either '0' or '1'.
# Solution
# Python O(N) O(N) Stack Greedy
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1: return False
        close: list[int] = []
        extra: list[int] = []
        for i in range(len(s)):
            if s[i] == ')':
                if locked[i] == '1':
                    if close: close.pop()
                    elif extra: extra.pop()
                    else: return False
                else:
                    extra.append(i)
            else:
                if locked[i] == '1':
                    close.append(i)
                else:
                    extra.append(i)
        while close and extra:
            if close[-1] < extra[-1]:
                close.pop()
                extra.pop()
            else: break
        return len(close) == 0

# C++ O(N) O(N) Stack Greedy
class Solution {
public:
    bool canBeValid(string s, string locked) {
        if (s.size() % 2 != 0) {
            return false;
        }
        std::stack<int> open;
        std::stack<int> extra;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                if (locked[i] == '1') {
                    open.push(i);
                } else {
                    extra.push(i);
                }
            } else {
                if (locked[i] == '1') {
                    if (!open.empty()) {
                        open.pop();
                    } else if (!extra.empty()) {
                        extra.pop();
                    } else {
                        return false;
                    }
                } else {
                    extra.push(i);
                }
            }
        }
        while (!open.empty() && !extra.empty()) {
            if (open.top() < extra.top()) {
                open.pop();
                extra.pop();
            } else {
                break;
            }
        }
        return open.empty();
    }
};