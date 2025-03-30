# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
#
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
#
# Return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:
#
# Input: s = "eccbbbbdec"
# Output: [10]
#
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.
# Solution
# Python O(N) O(D) Two Pointers HashMap
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n: int = len(s)
        end: list[int] = [-1] * 26
        for i in range(n - 1, -1, -1):
            code: int = ord(s[i]) - 97
            if end[code] == -1: end[code] = i
        output: list[int] = []
        left: int = 0
        right: int = end[ord(s[left]) - 97]
        for middle in range(n):
            if end[ord(s[middle]) - 97] == middle and middle == right:
                output.append(right - left + 1)
                right += 1
                if right < n:
                    left = right
                    right = end[ord(s[right]) - 97]
            elif end[ord(s[middle]) - 97] > right: right = end[ord(s[middle]) - 97]
        return output

# C++ O(N) O(D) TwoPointers HashMap
class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        vector<int> end(26, -1);
        for (int i = n - 1; i >= 0; --i) {
            int code = s[i] - 'a';
            if (end[code] == -1) end[code] = i;
        }
        vector<int> output;
        int left = 0;
        int right = end[s[left] - 'a'];
        for (int middle = 0; middle < n; ++middle) {
            if (end[s[middle] - 'a'] == middle && middle == right) {
                output.push_back(right - left + 1);
                ++right;
                if (right < n) {
                    left = right;
                    right = end[s[left] - 'a'];
                }
            } else if (end[s[middle] - 'a'] > right) right = end[s[middle] - 'a'];
        }
        return output;
    }
};