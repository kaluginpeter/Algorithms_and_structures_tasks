# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
# Solution
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(':')', '{':'}', '[':']'}
        stack = []
        for b in s:
            if b in parentheses:
                stack.append(parentheses[b])
            elif not stack or stack.pop() != b:
                return False
        return not stack


# Solution Stack String O(N) O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets: dict[str, str] = {')': '(', ']': '[', '}': '{'}
        stack: list[str] = []
        for bracket in s:
            if bracket not in closed_brackets:
                stack.append(bracket)
            elif not stack or stack[-1] != closed_brackets[bracket]:
                return False
            else: stack.pop()
        return not stack


# Go O(N) O(D) Stack
func isValid(s string) bool {
    var prev []rune = []rune{}
    var reciprocal map[rune]rune = map[rune]rune{')': '(', ']': '[', '}': '{'}
    for _, ch := range s {
        if ch == '(' || ch == '[' || ch == '{' {
            prev = append(prev, ch)
        } else {
            if len(prev) == 0 || prev[len(prev) - 1] != reciprocal[ch] {
                return false
            }
            prev = prev[:len(prev) - 1]
        }
    }
    return len(prev) == 0
}

# C++ O(N) O(D) Stack
class Solution {
public:
    bool isValid(string s) {
        std::stack<int> prev;
        std::unordered_map<int, int> reciprocal = {
            {'}' - '0', '{' - '0'},
            {']' - '0', '[' - '0'},
            {')' - '0', '(' - '0'}
        };
        for (char& ch : s) {
            if (!reciprocal.count(ch - '0')) prev.push(ch - '0');
            else {
                if (prev.empty() || reciprocal[ch - '0'] != prev.top()) {
                    return false;
                }
                prev.pop();
            }
        }
        return prev.empty();
    }
};