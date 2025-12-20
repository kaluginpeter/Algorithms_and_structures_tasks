# You are given an array of n strings strs, all of the same length.
#
# The strings can be arranged such that there is one on each line, making a grid.
#
# For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
#
# Return the number of columns that you will delete.
#
#
#
# Example 1:
#
# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
# Example 2:
#
# Input: strs = ["a","b"]
# Output: 0
# Explanation: The grid looks as follows:
#   a
#   b
# Column 0 is the only column and is sorted, so you will not delete any columns.
# Example 3:
#
# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# Explanation: The grid looks as follows:
#   zyx
#   wvu
#   tsr
# All 3 columns are not sorted, so you will delete all 3.
#
#
# Constraints:
#
# n == strs.length
# 1 <= n <= 100
# 1 <= strs[i].length <= 1000
# strs[i] consists of lowercase English letters.
# Solution
class Solution(object):
    def minDeletionSize(self, strs):
        top = 0
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j+1][i]:
                    top += 1
                    break
        return top


# Python O(NM) O(1) Matrix
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        output: int = 0
        n: int = len(strs)
        m: int = len(strs[0])
        for j in range(m):
            prev: str = 'a'
            is_valid: bool = True
            for i in range(n):
                if strs[i][j] < prev:
                    is_valid = False
                    break
                prev = strs[i][j]
            if not is_valid: output += 1
        return output

# C++ O(NM) O(1) Matrix
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int output = 0;
        size_t n = strs.size(), m = strs[0].size();
        for (size_t j = 0; j < m; ++j) {
            bool isValid = true;
            char prev = 'a';
            for (size_t i = 0; i < n; ++i) {
                if (strs[i][j] < prev) {
                    isValid = false;
                    break;
                }
                prev = strs[i][j];
            }
            if (!isValid) ++output;
        }
        return output;
    }
};