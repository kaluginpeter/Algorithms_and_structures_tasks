# You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.
#
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
#
# A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.
#
# For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
# Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.
#
#
#
# Example 1:
#
# example 1
# Input: s = "letsleetcode", k = 2
# Output: "let"
# Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
# "let" is the lexicographically largest one.
# Example 2:
#
# Input: s = "bb", k = 2
# Output: "b"
# Explanation: The longest subsequence repeated 2 times is "b".
# Example 3:
#
# Input: s = "ab", k = 2
# Output: ""
# Explanation: There is no subsequence repeated 2 times. Empty string is returned.
#
#
# Constraints:
#
# n == s.length
# 2 <= n, k <= 2000
# 2 <= n < k * 8
# s consists of lowercase English letters.
# Solution
# Python O(N * (N / K)!) O((N / K)!) String Greedy Counting
class Solution:
    def has_match(self, s: str, next_: list[str], k: int) -> bool:
        idx: int = 0
        count: int = 0
        n: int = len(s)
        length: int = len(next_)
        for letter in s:
            if letter == next_[idx]:
                idx += 1
                if idx == length:
                    idx = 0
                    count += 1
                    if count == k: return True
        return False

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq: list[int] = [0] * 26
        for letter in s:
            freq[ord(letter) - 97] += 1
        candidate: list[str] = []
        for i in range(25, -1, -1):
            if freq[i] >= k: candidate.append(chr(i + 97))
        line: list[list[str]] = deque()
        for letter in candidate:
            line.append([letter])
        output: list[str] = []
        while line:
            curr: list[str] = line.popleft()
            if len(curr) > len(output): output = curr[::]
            for letter in candidate:
                next_: list[str] = curr[::]
                next_.append(letter)
                if self.has_match(s, next_, k): line.append(next_)
        return ''.join(output)

# C++ O(N * (N / K)!) O((N / K)!) Greedy String Counting
class Solution {
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        std::vector<int> freq(26);
        for (char &ch : s) ++freq[ch - 'a'];
        std::vector<char> candidate;
        for (int i = 25; i >= 0; --i) {
            if (freq[i] >= k) candidate.push_back(i + 'a');
        }
        std::queue<std::string> q;
        for (char &ch : candidate) q.push(std::string(1, ch));
        std::string output = "";
        while (!q.empty()) {
            std::string curr = q.front();
            q.pop();
            if (curr.size() > output.size()) output = curr;
            for (char &ch : candidate) {
                std::string next = curr + ch;
                if (hasMatch(s, next, k)) q.push(next);
            }
        }
        return output;
    }

    bool hasMatch(const std::string& s, const std::string& next, int k) {
        int idx = 0, count = 0;
        int n = s.size(), length = next.size();
        for (char ch : s) {
            if (ch == next[idx]) {
                ++idx;
                if (idx == length) {
                    idx = 0;
                    ++count;
                    if (count == k) return true;
                }
            }
        }
        return false;
    }
};