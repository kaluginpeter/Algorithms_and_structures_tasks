# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.
#
# Example 1:
#
# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
# Example 2:
#
# Input: words = ["leetcode","win","loops","success"], pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.
#
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length, pref.length <= 100
# words[i] and pref consist of lowercase English letters.
# Solution
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in range(len(words)):
            if words[i].startswith(pref):
                count += 1
        return count

# Python O(NM) O(1) String Matching
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)

# C++ O(NM) O(1) String Matching
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int count = 0;
        for (std::string& word : words) {
            if (word.find(pref) == 0) {
                ++count;
            }
        }
        return count;
    }
};