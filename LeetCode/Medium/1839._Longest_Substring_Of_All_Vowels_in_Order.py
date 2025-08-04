# A string is considered beautiful if it satisfies the following conditions:
#
# Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
# The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
# For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.
#
# Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.
#
# A substring is a contiguous sequence of characters in a string.
#
#
#
# Example 1:
#
# Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
# Output: 13
# Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
# Example 2:
#
# Input: word = "aeeeiiiioooauuuaeiou"
# Output: 5
# Explanation: The longest beautiful substring in word is "aeiou" of length 5.
# Example 3:
#
# Input: word = "a"
# Output: 0
# Explanation: There is no beautiful substring, so return 0.
#
#
# Constraints:
#
# 1 <= word.length <= 5 * 105
# word consists of characters 'a', 'e', 'i', 'o', and 'u'.
# Solution
# Python O(N) O(1) SlidingWindow BitMask
class Solution:
    def get_bit(self, ch: str) -> int:
        match ch:
            case 'a': return 0
            case 'e': return 1
            case 'i': return 2
            case 'o': return 3
            case 'u': return 4
        return 0

    def longestBeautifulSubstring(self, word: str) -> int:
        output: int = 0
        left: int = 0
        cur_char: str = word[left]
        mask: int = 0
        for right in range(len(word)):
            if (cur_char != word[right]) and (
                (cur_char == 'a' and word[right] != 'e')
                or (cur_char == 'e' and word[right] != 'i')
                or (cur_char == 'i' and word[right] != 'o')
                or (cur_char == 'o' and word[right] != 'u')
                or (cur_char == 'u')
            ):
                left = right
                mask = 0
            cur_char = word[right]
            mask |= (1 << self.get_bit(cur_char))
            if mask == 31: output = max(output, right - left + 1)
        return output

# C++ O(N) O(1) SlidingWindow BitMask
class Solution {
public:
    int getBit(const char &x) {
        switch (x) {
            case 'a': return 0;
            case 'e': return 1;
            case 'i': return 2;
            case 'o': return 3;
            case 'u': return 4;
        }
        return 0;
    }
    int longestBeautifulSubstring(string word) {
        int output = 0, mask = 0, left = 0;
        char curChar = word[left];
        for (int right = 0; right < word.size(); ++right) {
            if (
                (curChar != word[right]) && (
                    (curChar == 'a' && word[right] != 'e')
                    || (curChar == 'e' && word[right] != 'i')
                    || (curChar == 'i' && word[right] != 'o')
                    || (curChar == 'o' && word[right] != 'u')
                    || (curChar == 'u')
                )
            ) {
                left = right;
                mask = 0;
            }
            curChar = word[right];
            mask |= (1 << getBit(curChar));
            if (mask == 31) output = std::max(output, right - left + 1);
        }
        return output;
    }
};