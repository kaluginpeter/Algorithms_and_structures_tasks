# You are given a string s consisting of lowercase English letters.
#
# You must repeatedly perform the following operation while the string s has at least two consecutive characters:
#
# Remove the leftmost pair of adjacent characters in the string that are consecutive in the alphabet, in either order (e.g., 'a' and 'b', or 'b' and 'a').
# Shift the remaining characters to the left to fill the gap.
# Return the resulting string after no more operations can be performed.
#
# Note: Consider the alphabet as circular, thus 'a' and 'z' are consecutive.
#
#
#
# Example 1:
#
# Input: s = "abc"
#
# Output: "c"
#
# Explanation:
#
# Remove "ab" from the string, leaving "c" as the remaining string.
# No further operations are possible. Thus, the resulting string after all possible removals is "c".
# Example 2:
#
# Input: s = "adcb"
#
# Output: ""
#
# Explanation:
#
# Remove "dc" from the string, leaving "ab" as the remaining string.
# Remove "ab" from the string, leaving "" as the remaining string.
# No further operations are possible. Thus, the resulting string after all possible removals is "".
# Example 3:
#
# Input: s = "zadb"
#
# Output: "db"
#
# Explanation:
#
# Remove "za" from the string, leaving "db" as the remaining string.
# No further operations are possible. Thus, the resulting string after all possible removals is "db".
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists only of lowercase English letters.
# Solution
# Python O(N) O(N) Stack String Greedy
class Solution:
    def resultingString(self, s: str) -> str:
        n: int = len(s)
        stack: list[str] = []
        for char in s:
            if not stack or abs((ord(stack[-1]) - 97) - (ord(char) - 97)) not in [1, 25]:
                stack.append(char)
            else: stack.pop()
        return ''.join(stack)

# C++ O(N) O(N) Stack String Greedy
class Solution {
public:
    string resultingString(string s) {
        string output = "";
        for (string::size_type i = 0; i < s.size(); ++i) {
            char &letter = s[i];
            if (!output.size()) output.push_back(letter);
            else {
                int diff = abs((output[output.size() - 1] - 'a' + 1) - (letter - 'a' + 1));
                if (diff == 1 || diff == 25) output.pop_back();
                else output.push_back(letter);
            }
        }
        return output;
    }
};