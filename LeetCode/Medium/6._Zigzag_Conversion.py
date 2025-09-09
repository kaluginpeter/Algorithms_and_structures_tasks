# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
# Solution
# Python O(N) O(N) TwoPointers String
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        start: int = 0
        end: int = max(1, numRows * 2 - 2)
        step: int = max(1, numRows * 2 - 2)
        segment: int = 0
        n: int = len(s)
        output: list[str] = []
        while start <= end:
            i: int = start
            while i < n:
                output.append(s[i])
                i += step
                if step and segment and i < n: output.append(s[i])
                i += segment
            segment += 2
            step -= 2
            start += 1
            end -= 1
        return ''.join(output)

# C++ O(N) O(N) String TwoPointers
class Solution {
public:
    string convert(string s, int numRows) {
        std::string output = "";
        size_t start = 0, end = std::max(1, numRows * 2 - 2), segment = 0, n = s.size(), step = std::max(1, numRows * 2 - 2);
        while (start <= end) {
            int i = start;
            while (i < n) {
                output.push_back(s[i]);
                i += step;
                if (segment && step && i < n) output.push_back(s[i]);
                i += segment;
            }
            step -= 2;
            segment += 2;
            ++start;
            --end;
        }
        return output;
    }
};