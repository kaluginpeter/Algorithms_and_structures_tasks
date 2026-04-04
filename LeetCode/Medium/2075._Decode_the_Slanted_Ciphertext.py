# A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a matrix having a fixed number of rows rows.
#
# originalText is placed first in a top-left to bottom-right manner.
#
#
# The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of originalText. The arrow indicates the order in which the cells are filled. All empty cells are filled with ' '. The number of columns is chosen such that the rightmost column will not be empty after filling in originalText.
#
# encodedText is then formed by appending all characters of the matrix in a row-wise fashion.
#
#
# The characters in the blue cells are appended first to encodedText, then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed.
#
# For example, if originalText = "cipher" and rows = 3, then we encode it in the following manner:
#
#
# The blue arrows depict how originalText is placed in the matrix, and the red arrows denote the order in which encodedText is formed. In the above example, encodedText = "ch ie pr".
#
# Given the encoded string encodedText and number of rows rows, return the original string originalText.
#
# Note: originalText does not have any trailing spaces ' '. The test cases are generated such that there is only one possible originalText.
#
#
#
# Example 1:
#
# Input: encodedText = "ch   ie   pr", rows = 3
# Output: "cipher"
# Explanation: This is the same example described in the problem description.
# Example 2:
#
#
# Input: encodedText = "iveo    eed   l te   olc", rows = 4
# Output: "i love leetcode"
# Explanation: The figure above denotes the matrix that was used to encode originalText.
# The blue arrows show how we can find originalText from encodedText.
# Example 3:
#
#
# Input: encodedText = "coding", rows = 1
# Output: "coding"
# Explanation: Since there is only 1 row, both originalText and encodedText are the same.
#
#
# Constraints:
#
# 0 <= encodedText.length <= 106
# encodedText consists of lowercase English letters and ' ' only.
# encodedText is a valid encoding of some originalText that does not have trailing spaces.
# 1 <= rows <= 1000
# The testcases are generated such that there is only one possible originalText.
# Solution
# Python O(NM) O(NM) Matrix
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n: int = len(encodedText)
        cols: int = n // rows
        output: list[str] = []
        for j in range(cols):
            for i in range(rows):
                pos: int = j + cols * i + i
                if pos >= n: continue
                output.append(encodedText[pos])
        while output and output[-1] == ' ': output.pop()
        return ''.join(output)

# C++ O(NM) O(NM) Matrix
class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        int n = encodedText.size();
        int cols = n / rows;
        std::string output = "";
        int j = 0;
        for (int j = 0; j < cols; ++j) {
            for (int i = 0; i < rows; ++i) {
                int pos = j + cols * i + i;
                if (pos >= n) continue;
                output.push_back(encodedText[pos]);
            }
        }
        while (!output.empty() && output.back() == ' ') output.pop_back();
        return output;
    }
};


# Python O(|K|) O(K) where K is the length of output string String Matrix Math
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n: int = rows
        bound: int = len(encodedText)
        m: int = bound // n
        output: list[str] = []
        for start in range(m):
            for shift in range(n):
                ptr: int = start + shift * m + shift
                if ptr >= bound: break
                output.append(encodedText[ptr])
        while output and output[-1] == ' ': output.pop()
        return ''.join(output)

# C++ O(|K|) O(K) where the K is the length of output string String Math Matrix
class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        size_t n = rows, m = encodedText.size() / n;
        std::string output = "";
        for (size_t start = 0; start < m; ++start) {
            for (size_t shift = 0; shift < n && start + m * shift + shift < encodedText.size(); ++shift) {
                output.push_back(encodedText[start + m * shift + shift]);
            }
        }
        while (!output.empty() && std::isspace(output.back())) output.pop_back();
        return output;
    }
};