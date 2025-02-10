# You are given a string s.
#
# Your task is to remove all digits by doing this operation repeatedly:
#
# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.
#
#
#
# Example 1:
#
# Input: s = "abc"
#
# Output: "abc"
#
# Explanation:
#
# There is no digit in the string.
#
# Example 2:
#
# Input: s = "cb34"
#
# Output: ""
#
# Explanation:
#
# First, we apply the operation on s[2], and s becomes "c4".
#
# Then we apply the operation on s[1], and s becomes "".
#
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# The input is generated such that it is possible to delete all digits.
# Solution One Pass O(N) O(N)
class Solution:
    def clearDigits(self, s: str) -> str:
        stack: list[str] = []
        for i in s:
            if i.isdigit():
                stack.pop()
            else:
                stack += i
        return ''.join(stack)


# Python O(N) O(N) Stack Simulation
class Solution:
    def clearDigits(self, s: str) -> str:
        stack: list[str] = []
        for ch in s:
            if ch.isdigit():
                if stack: stack.pop()
            else: stack.append(ch)
        return ''.join(stack)

# C++ O(N) O(N) Stack Simulation
class Solution {
public:
    string clearDigits(string s) {
        std::string output = "";
        for (char& ch : s) {
            if (std::isdigit(ch)) {
                if (output.size()) output.pop_back();
            } else output.push_back(ch);
        }
        return output;
    }
};