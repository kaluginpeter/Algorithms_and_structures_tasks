# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.
#
#
#
# Example 1:
#
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
# Example 2:
#
# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.
# Example 3:
#
# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
#
#
# Constraints:
#
# 1 <= words.length <= 104
# 1 <= allowed.length <= 26
# 1 <= words[i].length <= 10
# The characters in allowed are distinct.
# words[i] and allowed contain only lowercase English letters.
# Solution 1
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        for i in words:
            for j in i:
                if j not in allowed:
                    count -= 1
                    break
        return count
# Runtime 237 ms - Beats 99.23%, Memory 18.3 MB - Beats 68.86%
# Solution 2 using set
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count, allowed = len(words), set(allowed)
        for i in words:
            for j in i:
                if j not in allowed:
                    count -= 1
                    break
        return count
# Runtime 248 ms - Beats 91.64%, Memory 18.3 MB - Beats 95.47%

# Solution, both for Python and C++
# Time complexity: O(NM), where N is length of words and M is length of lenghtmost word in words
# Space complexity: O(K), where K is length of allowed characters
# Python
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashset_allowed: set[str] = set(allowed)
        consistent_words: int = 0
        for word in words:
            is_valid: bool = True
            for char in word:
                if char not in hashset_allowed:
                    is_valid = False
                    break
            if is_valid:
                consistent_words += 1
        return consistent_words
# C++
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_set<char> hashset_allowed;
        for (char allowed_char : allowed) {
            hashset_allowed.insert(allowed_char);
        }
        int consistent_words = 0;
        for (string word : words) {
            bool is_valid = true;
            for (char letter : word) {
                if (!hashset_allowed.count(letter)) {
                    is_valid = false;
                    break;
                }
            }
            if (is_valid) {
                consistent_words += 1;
            }
        }
        return consistent_words;
    }
};