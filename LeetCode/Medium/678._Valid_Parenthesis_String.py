# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
#
# The following rules define a valid string:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "(*)"
# Output: true
# Example 3:
#
# Input: s = "(*))"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.
# Solution Stack Greedy O(N) O(N)
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack: list[int] = list()
        zeros: list[int] = list()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                elif zeros:
                    zeros.pop()
                else:
                    return False
            else:
                zeros.append(i)
        while stack and zeros:
            if stack[0] <= zeros[0]:
                stack.pop(0)
                zeros.pop(0)
            else:
                zeros.pop(0)
        return not stack

# Solution One Pass O(N) O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        mn, mx = 0, 0
        for i in s:
            if i == '(':
                mn, mx = mn + 1, mx + 1
            elif i == ')':
                mn, mx = max(mn - 1, 0), mx - 1
            else:
                mn, mx = max(mn - 1, 0), mx + 1
            if mx < 0:
                return False
        return mn == 0


# C++ O(N) O(N) String
class Solution {
public:
    bool check(std::string& s) {
        size_t open = 0, closed = 0, extra = 0;
        for (char& ch : s) {
            if (ch == '(') ++open;
            else if (ch == '*') ++extra;
            else {
                ++closed;
                if (closed > open) {
                    if (!extra) return false;
                    ++open;
                    --extra;
                }
            }
        }
        return true;
    }
    bool checkValidString(string s) {
        bool first = check(s);
        std::string tmp = "";
        for (auto it = s.rbegin(); it != s.rend(); ++it) {
            if (*it == '(') tmp.push_back(')');
            else if (*it == ')') tmp.push_back('(');
            else tmp.push_back('*');
        }
        return first && check(tmp);
    }
};