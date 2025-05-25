# You are given an array of strings words. Each element of words consists of two lowercase English letters.
#
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
#
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
#
# A palindrome is a string that reads the same forward and backward.
#
#
#
# Example 1:
#
# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.
# Example 2:
#
# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
# Example 3:
#
# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".
#
#
# Constraints:
#
# 1 <= words.length <= 105
# words[i].length == 2
# words[i] consists of lowercase English letters.
# Solution
# Python O(N) O(N) HashMap String Greedy
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap: dict[str, int] = dict()
        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 1
        output: int = 0
        is_median: bool = False
        seen: set[str] = set()
        for word, freq in hashmap.items():
            if word in seen: continue
            if word[0] == word[1]:
                if freq & 1: is_median = True
                output += freq // 2 * 2 * 2
            else:
                mirror: str = word[::-1]
                output += min(freq, hashmap.get(mirror, 0)) * 2 * 2
                seen.add(mirror)
        return output + (2 if is_median else 0)

# C++ O(N) O(N) HashMap String Greedy
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> hashmap;
        for (string &word : words) {
            ++hashmap[word];
        }
        int output = 0;
        unordered_set<string> seen;
        bool isMedian = false;
        for (const auto &p : hashmap) {
            if (seen.count(p.first)) continue;
            if (p.first[0] == p.first[1]) {
                if (p.second & 1) isMedian = true;
                output += p.second / 2 * 2 * 2;
            } else {
                string mirror = p.first;
                reverse(mirror.begin(), mirror.end());
                int mirrorCount = (hashmap.count(mirror)? hashmap[mirror] : 0);
                output += min(p.second, mirrorCount) * 2 * 2;
                seen.insert(mirror);
            }
        }
        return output + (isMedian? 2 : 0);
    }
};