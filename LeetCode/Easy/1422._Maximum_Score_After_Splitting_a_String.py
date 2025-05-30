# Given a string s of zeros and ones, return the maximum score after
# splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros
# in the left substring plus the number of ones in the right substring.
#
# Example 1:
#
# Input: s = "011101"
# Output: 5
# Explanation:
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5
# left = "01" and right = "1101", score = 1 + 3 = 4
# left = "011" and right = "101", score = 1 + 2 = 3
# left = "0111" and right = "01", score = 1 + 1 = 2
# left = "01110" and right = "1", score = 2 + 1 = 3
# Example 2:
#
# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
# Example 3:
#
# Input: s = "1111"
# Output: 3
#
# Constraints:
# 2 <= s.length <= 500
# The string s consists of characters '0' and '1' only.
# Solution
class Solution:
    def maxScore(self, s: str) -> int:
        return max(s[:i].count('0') + s[i:].count('1') for i in range(1, len(s)))
    

# Solution O(N) O(1)
class Solution:
    def maxScore(self, s: str) -> int:
        count_s = s.count('1', 1)
        if s[0] == '0':
            count_s += 1
        total = count_s
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                count_s += 1
            else:
                count_s -= 1
            total = max(total, count_s)
        return total

# Python O(N) O(N) Prefix Sum
class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum: list[tuple[int, int]] = []
        zeros = ones = 0
        n: int = len(s)
        for idx in range(n):
            if s[idx] == '0':
                zeros += 1
            else:
                ones += 1
            prefix_sum.append((zeros, ones))
        max_score: int = 0
        for left in range(n - 1):
            cur_score: int = prefix_sum[left][0] + prefix_sum[n - 1][1] - prefix_sum[left][1]
            if cur_score > max_score:
                max_score = cur_score
        return max_score

# C++ O(N) O(N) Prefix Sum
class Solution {
public:
    int maxScore(string s) {
        int n = s.size();
        std::vector<std::pair<int, int>> prefixSum;
        int zeros = 0, ones = 0;
        for (int idx = 0; idx < n; ++idx) {
            if (s[idx] == '0') {
                ++zeros;
            } else {
                ++ones;
            }
            prefixSum.push_back({zeros, ones});
        }
        int maxScore = 0;
        for (int left = 0; left < n - 1; ++left) {
            int curScore = prefixSum[left].first + prefixSum[n - 1].second - prefixSum[left].second;
            if (curScore > maxScore) {
                maxScore = curScore;
            }
        }
        return maxScore;
    }
};