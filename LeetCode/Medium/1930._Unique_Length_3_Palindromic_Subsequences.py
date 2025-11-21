# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
#
#
# Example 1:
#
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
# Example 2:
#
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
# Example 3:
#
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
#
#
# Constraints:
#
# 3 <= s.length <= 105
# s consists of only lowercase English letters.
# Solution
# Note
# We can simplify memory usage by avoidind creation of prefixSum vector.
# For doing that, we need to find leftmost and rightmost indexes of each
# character(of 26 max possibles) and that iterate through all 26 letters and for
# each check size of distinct elements in range (leftmostIndex, rightmostIndex]
# Python O(N) O(N) Prefix Sum HashMap
class Solution:
    def get_palindroms(self, x: list[int], y: list[int], bound: str) -> int:
        count: int = 0
        for hash_code in range(26):
            if hash_code == ord(bound) - ord('a'):
                count += x[hash_code] >= 3
            elif x[hash_code] > y[hash_code]:
                count += 1
        return count

    def countPalindromicSubsequence(self, s: str) -> int:
        prefix_sum: list[list[int]] = []
        chunk: list[int] = [0] * 26
        first_pos: list[int] = [0] * 26
        for i in range(len(s)):
            hash_code: int = ord(s[i]) - ord('a')
            chunk[hash_code] += 1
            if chunk[hash_code] == 1:
                first_pos[hash_code] = i
            prefix_sum.append(chunk.copy())
        seen: list[bool] = [False] * 26
        output: int = 0
        for i in range(len(s) - 1, -1, -1):
            hash_code: int = ord(s[i]) - ord('a')
            if not seen[hash_code] and first_pos[hash_code] != i:
                output += self.get_palindroms(
                    prefix_sum[i], prefix_sum[first_pos[hash_code]], s[i]
                )
                seen[hash_code] = True
        return output

# C++ O(N) O(N) Prefix Sum HashMap
class Solution {
public:
    int getPalindroms(std::vector<int>& x, std::vector<int>& y, char& bound) {
        int count = 0;
        for (int i = 0; i < 26; ++i) {
            if (i == bound - 'a') {
                count += (x[i] >= 3? 1 : 0);
            } else if (x[i] > y[i]) {
                ++count;
            }
        }
        return count;
    }
    int countPalindromicSubsequence(string s) {
        std::vector<std::vector<int>> prefixSum;
        std::vector<int> chunk (26, 0);
        std::vector<int> firstPos (26, 0);
        for (int i = 0; i < s.size(); ++i) {
            ++chunk[s[i] - 'a'];
            if (chunk[s[i] - 'a'] == 1) {
                firstPos[s[i] - 'a'] = i;
            }
            prefixSum.push_back(chunk);
        }
        int output = 0;
        std::vector<bool> seen (26, false);
        for (int i = s.size() - 1; i >= 0; --i) {
            if (!seen[s[i] - 'a'] && firstPos[s[i] - 'a'] != i) {
                output += getPalindroms(prefixSum[i], prefixSum[firstPos[s[i] - 'a']], s[i]);
                seen[s[i] - 'a'] = true;
            }
        }
        return output;
    }
};


# Python O(N26) O(26*26) BitManipulation HashMap
import array
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first: array.array[int] = array.array('i', (-1 for _ in range(26)))
        last: array.array[int] = array.array('i', (-1 for _ in range(26)))
        n: int = len(s)
        for i in range(n):
            j: int = ord(s[i]) - 97
            if first[j] == -1: first[j] = i
            last[j] = i
        output: int = 0
        seen: list[array.array[int]] = [array.array('i', (0 for _ in range(26))) for _ in range(26)]
        for i in range(1, n - 1):
            k: int = ord(s[i]) - 97
            for j in range(26):
                if (first[j] < i < last[j]) and not seen[j][k]:
                    seen[j][k] = 1
                    output += 1
        return output

# C++ O(N26) O(26*26) HashMap
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        std::array<int, 26> first{}, last{};
        for (int i = 0; i < 26; ++i) {
            first[i] = -1;
            last[i] = -1;
        }
        for (int i = 0; i < s.size(); ++i) {
            int j = s[i] - 'a';
            if (first[j] == -1) first[j] = i;
            last[j] = i;
        }
        std::array<std::bitset<26>, 26> seen{};
        int output = 0;
        for (size_t i = 1; i < s.size() - 1; ++i) {
            int k = s[i] - 'a';
            for (int j = 0; j < 26; ++j) {
                if ((first[j] < i) && (i < last[j]) && !seen[j][k]) {
                    seen[j][k] = 1;
                    ++output;
                }
            }
        }
        return output;
    }
};