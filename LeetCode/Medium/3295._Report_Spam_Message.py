# You are given an array of strings message and an array of strings bannedWords.
#
# An array of words is considered spam if there are at least two words in it that exactly match any word in bannedWords.
#
# Return true if the array message is spam, and false otherwise.
#
#
#
# Example 1:
#
# Input: message = ["hello","world","leetcode"], bannedWords = ["world","hello"]
#
# Output: true
#
# Explanation:
#
# The words "hello" and "world" from the message array both appear in the bannedWords array.
#
# Example 2:
#
# Input: message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]
#
# Output: false
#
# Explanation:
#
# Only one word from the message array ("programming") appears in the bannedWords array.
#
#
#
# Constraints:
#
# 1 <= message.length, bannedWords.length <= 105
# 1 <= message[i].length, bannedWords[i].length <= 15
# message[i] and bannedWords[i] consist only of lowercase English letters.
# Solution
# Python O(N) O(K), where K is length of distinct words in bannedWords
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        deprecated: set[str] = set(bannedWords)
        count: int = 0
        for m in message:
            count += m in deprecated
            if count > 1: return True
        return False

# C++ O(N) O(K), where K is length of distinct words in bannedWords
class Solution {
public:
    bool reportSpam(vector<string>& message, vector<string>& bannedWords) {
        std::unordered_set<std::string> deprecated;
        for (std::string word : bannedWords) {
            deprecated.insert(word);
        }
        int count = 0;
        for (std::string word : message) {
            count += deprecated.count(word);
            if (count > 1) {
                return true;
            }
        }
        return false;
    }
};