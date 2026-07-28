# You are given a palindromic string s.
#
# Return the lexicographically smallest palindromic permutation of s.
#
# A string is palindromic if it reads the same forward and backward.
#
# A permutation is a rearrangement of all the characters of a string.
#
# A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
# If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.
#
#
# Example 1:
#
# Input: s = "z"
#
# Output: "z"
#
# Explanation:
#
# A string of only one character is already the lexicographically smallest palindrome.
#
# Example 2:
#
# Input: s = "babab"
#
# Output: "abbba"
#
# Explanation:
#
# Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.
#
# Example 3:
#
# Input: s = "daccad"
#
# Output: "acddca"
#
# Explanation:
#
# Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.
# Solution
# Python O(N) O(N) HashMap Greedy
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        hashmap: list[int] = [0] * 26
        for letter in s: hashmap[ord(letter) - 97] += 1
        median: int = -1
        left_part: list[str] = []
        for code in range(26):
            if hashmap[code] & 1 and median == -1: median = code + 97
            for _ in range(hashmap[code] // 2):
                left_part.append(chr(code + 97))
        output: list[str] = left_part[::]
        if median != -1: output.append(chr(median))
        return ''.join(output) + ''.join(reversed(left_part))

# C++ O(N) O(N) HashMap Greedy
class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> hashmap(26, 0);
        for (char &letter : s) ++hashmap[letter - 'a'];
        int median = -1;
        string leftPart = "";
        for (int code = 0; code < 26; ++code) {
            if (hashmap[code] & 1 && median == -1) median = code + 97;
            for (int i = 0; i < hashmap[code] / 2; ++i) {
                leftPart.push_back(static_cast<char>(code + 97));
            }
        }
        string palindrom = leftPart;
        if (median != -1) palindrom.push_back(static_cast<char>(median));
        for (string::const_reverse_iterator letter = leftPart.crbegin(); letter != leftPart.crend(); ++letter) {
            palindrom.push_back(*letter);
        }
        return palindrom;
    }
};


# Python O(N) O(26) HashMap Greedy
from array import array
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        hashmap: list[int] = array('I', [0]) * 26
        for ch in s: hashmap[ord(ch) - 97] += 1
        tie: int = 26
        output: list[int] = []
        for i in range(26):
            if hashmap[i] & 1: tie = i # only once possible
            for _ in range(hashmap[i] >> 1): output.append(i)
        if tie < 26: output.append(tie)
        for i in range(26):
            for _ in range(hashmap[26 - i - 1] >> 1): output.append(26 - i - 1)
        return ''.join(chr(ch + 97) for ch in output)

# C++ O(N) O(26) Greedy HashMap
class Solution {
public:
    string smallestPalindrome(string s) {
        std::array<int, 26> hashmap{};
        for (char& ch : s) ++hashmap[ch - 'a'];
        std::string output = "";
        size_t tie = 26;
        for (size_t i = 0; i < 26; ++i) {
            if (hashmap[i] & 1) tie = i; // only once possible
            for (size_t j = 0; j < hashmap[i] >> 1; ++j) output.push_back(i + 'a');
        }
        if (tie < 26) output.push_back(tie + 'a');
        for (size_t i = 26; i > 0; --i) {
            for (size_t j = 0; j < hashmap[i - 1] >> 1; ++j) output.push_back((i - 1) + 'a');
        }
        return output;
    }
};