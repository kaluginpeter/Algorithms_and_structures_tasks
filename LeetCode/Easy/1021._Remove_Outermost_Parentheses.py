# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
#
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
#
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
#
#
#
# Example 1:
#
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:
#
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:
#
# Input: s = "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '(' or ')'.
# s is a valid parentheses string.
# Solution O(N) O(N)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans: list = []
        count: int = 0
        for i in s:
            if i == '(' and count > 0:
                ans.append(i)
            elif i == ')' and count > 1:
                ans.append(i)
            count += 1 if i == '(' else -1
        return ''.join(ans)
# Solution O(N) O(N)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack: list = []
        ans: str = ''
        part: list = []
        for i in s:
            if i == '(':
                stack.append(i)
                part.append(i)
            else:
                stack.pop()
                part.append(i)
                if not stack:
                    ans += ''.join(part[1:-1])
                    part = []
        return ans


# C++ O(N) O(N) Stack
class Solution {
public:
    string removeOuterParentheses(string s) {
        std::string output = "", cur = "";
        int acc = 0;
        for (char& ch : s) {
            if (ch == '(') {
                ++acc; cur.push_back(ch);
            } else {
                --acc; cur.push_back(ch);
                if (!acc) {
                    output += cur.substr(1, cur.size() - 2);
                    cur.clear();
                }
            }
        }
        return output;
    }
};

# Go O(N) O(N) Stack String
func removeOuterParentheses(s string) string {
    var output, cur []byte = []byte{}, []byte{}
    var acc int = 0
    for _, ch := range s {
        if ch == '(' {
            acc++
            cur = append(cur, byte(ch))
        } else {
            acc--
            cur = append(cur, byte(ch))
            if acc == 0 {
                output = append(output, cur[1:len(cur) - 1]...)
                cur = []byte{}
            }
        }
    }
    return string(output)
}