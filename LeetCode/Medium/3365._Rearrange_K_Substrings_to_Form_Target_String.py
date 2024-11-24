# You are given two strings s and t, both of which are anagrams of each other, and an integer k.
#
# Your task is to determine whether it is possible to split the string s into k equal-sized substrings, rearrange the substrings, and concatenate them in any order to create a new string that matches the given string t.
#
# Return true if this is possible, otherwise, return false.
#
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
#
# A substring is a contiguous non-empty sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: s = "abcd", t = "cdab", k = 2
#
# Output: true
#
# Explanation:
#
# Split s into 2 substrings of length 2: ["ab", "cd"].
# Rearranging these substrings as ["cd", "ab"], and then concatenating them results in "cdab", which matches t.
# Example 2:
#
# Input: s = "aabbcc", t = "bbaacc", k = 3
#
# Output: true
#
# Explanation:
#
# Split s into 3 substrings of length 2: ["aa", "bb", "cc"].
# Rearranging these substrings as ["bb", "aa", "cc"], and then concatenating them results in "bbaacc", which matches t.
# Example 3:
#
# Input: s = "aabbcc", t = "bbaacc", k = 2
#
# Output: false
#
# Explanation:
#
# Split s into 2 substrings of length 3: ["aab", "bcc"].
# These substrings cannot be rearranged to form t = "bbaacc", so the output is false.
#
#
# Constraints:
#
# 1 <= s.length == t.length <= 2 * 105
# 1 <= k <= s.length
# s.length is divisible by k.
# s and t consist only of lowercase English letters.
# The input is generated such that s and t are anagrams of each other.
# Solution
# Python O(N) O(N) HashMap
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n: int = len(s)
        segment_length: int = n // k
        hashmap: dict[str, int] = dict()
        segment_s: list[str] = []
        segment_t: list[str] = []
        for idx in range(n):
            segment_s.append(s[idx])
            segment_t.append(t[idx])
            if len(segment_s) == segment_length:
                str_segment_s: str = ''.join(segment_s)
                str_segment_t: str = ''.join(segment_t)
                hashmap[str_segment_s] = hashmap.get(str_segment_s, 0) + 1
                hashmap[str_segment_t] = hashmap.get(str_segment_t, 0) - 1
                segment_s.clear()
                segment_t.clear()
        return all(freq >= 0 for segment, freq in hashmap.items())

# C++ O(N) O(N) HashMap
class Solution {
public:
    bool isPossibleToRearrange(string s, string t, int k) {
        std::unordered_map<std::string, int> hashmap;
        int n = s.size();
        int segmentLength = n / k;
        std::string segmentS = "";
        std::string segmentT = "";
        for (int index = 0; index < n; ++index) {
            segmentS += s[index];
            segmentT += t[index];
            if (segmentS.size() == segmentLength) {
                ++hashmap[segmentS];
                --hashmap[segmentT];
                segmentS = "";
                segmentT = "";
            }
        }
        for (auto& pair : hashmap) {
            if (pair.second < 0) {
                return false;
            }
        }
        return true;
    }
};