# You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.
#
# Build a new string result by processing s according to the following rules from left to right:
#
# If the letter is a lowercase English letter append it to result.
# A '*' removes the last character from result, if it exists.
# A '#' duplicates the current result and appends it to itself.
# A '%' reverses the current result.
# Return the final string result after processing all characters in s.
#
#
#
# Example 1:
#
# Input: s = "a#b%*"
#
# Output: "ba"
#
# Explanation:
#
# i	s[i]	Operation	Current result
# 0	'a'	Append 'a'	"a"
# 1	'#'	Duplicate result	"aa"
# 2	'b'	Append 'b'	"aab"
# 3	'%'	Reverse result	"baa"
# 4	'*'	Remove the last character	"ba"
# Thus, the final result is "ba".
#
# Example 2:
#
# Input: s = "z*#"
#
# Output: ""
#
# Explanation:
#
# i	s[i]	Operation	Current result
# 0	'z'	Append 'z'	"z"
# 1	'*'	Remove the last character	""
# 2	'#'	Duplicate the string	""
# Thus, the final result is "".
#
#
#
# Constraints:
#
# 1 <= s.length <= 20
# s consists of only lowercase English letters and special characters *, #, and %.
# Solution
# Python O(N^2) O(N) Simulation String
class Solution:
    def processStr(self, s: str) -> str:
        output: list[str] = []
        for ch in s:
            if ch == '*' and output: output.pop()
            elif ch == '#': output.extend(output)
            elif ch == '%': output.reverse()
            elif ch.islower(): output.append(ch)
        return ''.join(output)

# C++ O(N^2) O(N) String Simulation
class Solution {
public:
    string processStr(string s) {
        std::string output = "";
        for (char& ch : s) {
            if (ch == '*' && output.size()) output.pop_back();
            else if (ch == '#') output += output;
            else if (ch == '%') std::reverse(output.begin(), output.end());
            else if (std::islower(ch)) output.push_back(ch);
        }
        return output;
    }
};