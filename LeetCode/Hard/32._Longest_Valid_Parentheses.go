/*
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
*/
// Solution
// Go O(N) O(N) Stack
func longestValidParentheses(s string) int {
    var prev []int = []int{}
    var cur, output int = 0, 0
    for _, ch := range s {
        if ch == '(' {
            prev = append(prev, cur)
            cur = 0
        } else {
            if len(prev) == 0 {
                cur = 0
            } else {
                cur += 2 + prev[len(prev) - 1]
                output = max(output, cur)
                prev = prev[:len(prev) - 1]
            }
        }
    }
    return output
}
// C++ O(N) O(N) Stack
class Solution {
public:
    int longestValidParentheses(string s) {
        std::vector<int> prev;
        int cur = 0, output = 0;
        for (char& ch : s) {
            if (ch == '(') {
                prev.push_back(cur);
                cur = 0;
            } else {
                if (prev.empty()) cur = 0;
                else {
                    cur += 2 + prev.back();
                    prev.pop_back();
                    output = std::max(output, cur);
                }
            }
        }
        return output;
    }
};