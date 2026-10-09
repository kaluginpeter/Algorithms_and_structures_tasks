/*
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

 

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.
Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
 

Constraints:

1 <= s.length <= 105
s consists of '(' and ')' only.
*/
// Solution
// C++ O(N) O(1) Math
class Solution {
public:
    int minInsertions(string s) {
        size_t output = 0, cur = 0;
        for (char& ch : s) {
            if (ch == '(') {
                if (cur & 1) {
                    --cur; ++output;
                }
                cur += 2;
            } else {
                if (!cur) {
                    cur += 2; ++output;
                }
                --cur;
            }
        }
        return output + cur;
    }
};

// Go O(N) O(1) Math
func minInsertions(s string) int {
    var output, cur int = 0, 0
    for _, ch := range s {
        if ch == '(' {
            if cur & 1 == 1 {
                output++
                cur--
            }
            cur += 2
        } else {
            if cur == 0 {
                output++
                cur += 2
            }
            cur--
        }
    }
    return output + cur
}