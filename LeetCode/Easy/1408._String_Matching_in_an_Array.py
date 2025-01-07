# Given an array of string words, return all strings in words
# that is a substring of another word. You can return the answer in any order.
# A substring is a contiguous sequence of characters within a string
#
# Example 1:
#
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:
#
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:
#
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
#
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.
# Solution
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = []
        w = ' '.join(i for i in words)
        for i in words:
            if w.count(i) > 1: l.append(i)
        return l

# Solution
# Python O(N**2 + M) O(NM) Knuth-Morris-Pratt
class Solution:
    def build_lps(self, sub: str) -> list[int]:
        n: int = len(sub)
        lps: list[int] = [0] * n
        left: int = 0
        right: int = left + 1
        while right < n:
            if sub[right] == sub[left]:
                left += 1
                lps[right] = left
                right += 1
            elif left > 0:
                left = lps[left - 1]
            else:
                right += 1
        return lps

    def string_matching(self, main: str, pattern: str, lps: list[int]) -> bool:
        pattern_idx: int = 0
        main_idx: int = 0
        n: int = len(pattern)
        m: int = len(main)
        while pattern_idx < n and main_idx < m:
            if main[main_idx] == pattern[pattern_idx]:
                pattern_idx += 1
                main_idx += 1
            elif pattern_idx > 0:
                pattern_idx = lps[pattern_idx - 1]
            else:
                main_idx += 1
        return pattern_idx == n

    def stringMatching(self, words: List[str]) -> List[str]:
        output: list[str] = []
        n: int = len(words)

        for pattern_idx in range(n):
            lps: list[int] = self.build_lps(words[pattern_idx])
            for main_idx in range(n):
                if main_idx == pattern_idx: continue
                if self.string_matching(words[main_idx], words[pattern_idx], lps):
                    output.append(words[pattern_idx])
                    break
        return output

# C++ O(N**2 + M) O(NM) Knuth-Morris-Pratt
class Solution {
public:
    std::vector<int> buildLps(std::string& sub) {
        int n = sub.size();
        std::vector<int> lps (n, 0);
        int left = 0;
        int right = 1;
        while (right < n) {
            if (sub[left] == sub[right]) {
                ++left;
                lps[right] = left;
                ++right;
            } else if (left > 0) {
                left = lps[left - 1];
            } else {
                ++right;
            }
        }
        return lps;
    }

    bool stringMatching(std::string& main, std::string& pattern, std::vector<int>& lps) {
        int n = pattern.size();
        int m = main.size();
        int patternIdx = 0;
        int mainIdx = 0;
        while (patternIdx < n && mainIdx < m) {
            if (main[mainIdx] == pattern[patternIdx]) {
                ++patternIdx;
                ++mainIdx;
            } else if (patternIdx > 0) {
                patternIdx = lps[patternIdx - 1];
            } else {
                ++mainIdx;
            }
        }
        return patternIdx == pattern.size();
    }

    vector<string> stringMatching(vector<string>& words) {
        std::vector<std::string> output;
        int n = words.size();
        for (int patternIdx = 0; patternIdx < n; ++patternIdx) {
            std::vector<int> lps = buildLps(words[patternIdx]);
            for (int mainIdx = 0; mainIdx < n; ++mainIdx) {
                if (patternIdx == mainIdx) {
                    continue;
                }
                if (stringMatching(words[mainIdx], words[patternIdx], lps)) {
                    output.push_back(words[patternIdx]);
                    break;
                }
            }
        }
        return output;
    }
};