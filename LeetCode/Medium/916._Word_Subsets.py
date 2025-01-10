# You are given two string arrays words1 and words2.
#
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
#
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
#
# Return an array of all the universal strings in words1. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]
# Example 2:
#
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
# Output: ["apple","google","leetcode"]
#
#
# Constraints:
#
# 1 <= words1.length, words2.length <= 104
# 1 <= words1[i].length, words2[i].length <= 10
# words1[i] and words2[i] consist only of lowercase English letters.
# All the strings of words1 are unique.
# Solution
# Python O(N + M) O(N) String HashMap
class Solution:
    def make_histogram(self, word: str) -> list[int]:
        histogram: list[int] = [0] * 26
        for letter in word:
            histogram[ord(letter) - 97] += 1
        return histogram

    def is_universal(self, x: list[int], y: list[int]) -> bool:
        return all(x[i] >= y[i] for i in range(26))

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_histogram: list[int] = [0] * 26
        for word in words2:
            word_histogram: list[int] = self.make_histogram(word)
            for i in range(26):
                if words2_histogram[i] < word_histogram[i]:
                    words2_histogram[i] = word_histogram[i]
        output: list[str] = []
        for word in words1:
            word_histogram: list[int] = self.make_histogram(word)
            if self.is_universal(word_histogram, words2_histogram):
                output.append(word)
        return output

# C++ O(N + M) O(N) String HashMap
class Solution {
public:
    std::vector<int> makeHistogram(std::string& word) {
        std::vector<int> histogram (26, 0);
        for (char& letter : word) {
            ++histogram[letter - 97];
        }
        return histogram;
    }
    bool isUniversal(std::vector<int>& x, std::vector<int>& y) {
        for (int i = 0; i < 26; ++i) {
            if (x[i] < y[i]) {
                return false;
            }
        }
        return true;
    }
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        std::vector<int> words2Histogram (26, 0);
        for (std::string& word : words2) {
            std::vector<int> wordHistogram = makeHistogram(word);
            for (int i = 0; i < 26; ++i) {
                if (words2Histogram[i] < wordHistogram[i]) {
                    words2Histogram[i] = wordHistogram[i];
                }
            }
        }
        std::vector<std::string> output;
        for (std::string& word : words1) {
            std::vector<int> wordHistogram = makeHistogram(word);
            if (isUniversal(wordHistogram, words2Histogram)) {
                output.push_back(word);
            }
        }
        return output;
    }
};