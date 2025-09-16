# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
#
#
#
# Example 1:
#
# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
# Example 2:
#
# Input: s = "azxxzy"
# Output: "ay"
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# Solution
# Python O(N) O(N) Stack String
class Solution:
    def removeDuplicates(self, s: str) -> str:
        output: list[str] = []
        for ch in s:
            if output and output[-1] == ch: output.pop()
            else: output.append(ch)
        return ''.join(output)

# C++ O(N) O(N) String Stack
class Solution {
public:
    string removeDuplicates(string s) {
        std::string output = "";
        for (const char& ch : s) {
            if (!output.empty() && output.back() == ch) output.pop_back();
            else output.push_back(ch);
        }
        return output;
    }
};