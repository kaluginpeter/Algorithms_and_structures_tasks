# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
#
# Return the number of special letters in word.
#
#
#
# Example 1:
#
# Input: word = "aaAbcBC"
#
# Output: 3
#
# Explanation:
#
# The special characters are 'a', 'b', and 'c'.
#
# Example 2:
#
# Input: word = "abc"
#
# Output: 0
#
# Explanation:
#
# There are no special characters in word.
#
# Example 3:
#
# Input: word = "AbBCab"
#
# Output: 0
#
# Explanation:
#
# There are no special characters in word.
#
#
#
# Constraints:
#
# 1 <= word.length <= 2 * 105
# word consists of only lowercase and uppercase English letters.
# Solution Greedy HashTable O(N) O(N)
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ht: dict[str, int] = dict()
        for i in range(len(word)):
            if word[i] not in ht:
                ht[word[i]] = i
            elif word[i].islower():
                ht[word[i]] = i
        ans: int = 0
        for i in ht:
            if (i.lower() in ht and i.upper() in ht) and ht[i.lower()] < ht[i.upper()]:
                ans += 1
        return ans // 2


# Python O(N) O(D) HashMap
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower: list[int] = [-1] * 26
        upper: list[int] = [-1] * 26
        for i in range(len(word)):
            if word[i].islower(): lower[ord(word[i]) - 97] = i
            elif upper[ord(word[i]) - 65] == -1: upper[ord(word[i]) - 65] = i
        output: int = 0
        for i in range(26):
            if lower[i] != -1 and upper[i] != -1 and lower[i] < upper[i]:
                output += 1
        return output

# C++ O(N) O(D) HashMap
class Solution {
public:
    int numberOfSpecialChars(string word) {
        std::array<int, 26> lower{}, upper{};
        for (size_t i = 0; i < 26; ++i) {
            lower[i] = -1; upper[i] = -1;
        }
        for (size_t i = 0; i < word.size(); ++i) {
            if (std::islower(word[i])) lower[word[i] - 'a'] = i;
            else if (upper[word[i] - 'A'] == -1) upper[word[i] - 'A'] = i;
        }
        int output = 0;
        for (size_t i = 0; i < 26; ++i) {
            if (lower[i] != -1 && upper[i] != -1 && lower[i] < upper[i]) ++output;
        }
        return output;
    }
};