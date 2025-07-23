# You are given a string s and two integers x and y. You can perform two types of operations any number of times.
#
# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.
#
#
#
# Example 1:
#
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:
#
# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
#
#
# Constraints:
#
# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.
# Solution Stack
# General idea:
# Choose substring that gives max points and count
# how many it contains in string using stack for counting and processing.
# After, you should iterate from entire first stack and count how many second substring contains in first stack,
# uses second stack for counting. In the end return total sum of points.
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        first_substring: str = ['a', 'b'] if x >= y else ['b', 'a']
        first_points: int = max(x, y)
        second_substring: str = ['a', 'b'] if x < y else ['b', 'a']
        second_points: int = min(x, y)
        total_points: int = 0

        first_stack: list[str] = []
        for char in s:
            first_stack.append(char)
            while first_stack and first_stack[-2:] == first_substring:
                total_points += first_points
                first_stack.pop()
                first_stack.pop()

        second_stack: list[str] = []
        for char in first_stack:
            second_stack.append(char)
            while second_stack and second_stack[-2:] == second_substring:
                total_points += second_points
                second_stack.pop()
                second_stack.pop()

        return total_points


# Python O(N) O(N) Greedy
class Solution:
    def simulate(self, s: str, major: str, minor: str, major_p: int, minor_p: int) -> int:
        stack: list[str] = []
        output: int = 0
        for i in range(len(s)):
            if stack and stack[-1] == major[0] and s[i] == major[1]:
                stack.pop()
                output += major_p
            else: stack.append(s[i])
        remaining: str = ''.join(stack)
        stack.clear()
        for i in range(len(remaining)):
            if stack and stack[-1] == minor[0] and remaining[i] == minor[1]:
                stack.pop()
                output += minor_p
            else: stack.append(remaining[i])
        return output

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y: return self.simulate(s, 'ab', 'ba', x, y)
        return self.simulate(s, 'ba', 'ab', y, x)

# C++ O(N) O(N) Greedy
class Solution {
public:
    int simulate(std::string &s, std::string &major, std::string &minor, int majorP, int minorP) {
        std::stack<char> st;
        int output = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (!st.empty() && st.top() == major[0] && s[i] == major[1]) {
                st.pop();
                output += majorP;
            } else st.push(s[i]);
        }
        std::string remaining = "";
        while (!st.empty()) {
            remaining.push_back(st.top());
            st.pop();
        }
        std::reverse(remaining.begin(), remaining.end());
        for (int i = 0; i < remaining.size(); ++i) {
            if (!st.empty() && st.top() == minor[0] && remaining[i] == minor[1]) {
                output += minorP;
                st.pop();
            } else st.push(remaining[i]);
        }
        return output;
    }
    int maximumGain(string s, int x, int y) {
        std::string first = "ab", second = "ba";
        if (x >= y) return simulate(s, first, second, x, y);
        return simulate(s, second, first, y, x);
    }
};