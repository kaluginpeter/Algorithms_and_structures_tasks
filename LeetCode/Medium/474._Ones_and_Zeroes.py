# You are given an array of binary strings strs and two integers m and n.
#
# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
#
# A set x is a subset of a set y if all elements of x are also elements of y.
#
#
#
# Example 1:
#
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
# Example 2:
#
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.
#
#
# Constraints:
#
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
# Solution
# Python O(LNM) O(NM) DynamicProgramming
class Solution:
    def get_score(self, row: str) -> tuple[int, int]:
        zeros: int = 0
        ones: int = 0
        for ch in row:
            if int(ch): ones += 1
            else: zeros += 1
        return (zeros, ones)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
        for cell in strs:
            zeros, ones = self.get_score(cell)
            for i in range(n, ones - 1, -1):
                for j in range(m, zeros - 1, -1):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i - ones][j - zeros] + 1
                    )
        return dp[n][m]

# C++ O(LNM) O(NM) DynamicProgramming
class Solution {
public:
    std::pair<int, int> getFreq(std::string& cell) {
        int zeros = 0, ones = 0;
        for (char& ch : cell) {
            zeros += ch == '0';
            ones += ch == '1';
        }
        return std::pair<int, int>(zeros, ones);
    }
    int findMaxForm(vector<string>& strs, int m, int n) {
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));
        for (std::string& cell : strs) {
            std::pair<int, int> freq = getFreq(cell); // <zeros, ones>
            for (int i = n; i >= freq.second; --i) {
                for (int j = m; j >= freq.first; --j) {
                    dp[i][j] = std::max({
                        dp[i][j],
                        dp[i - freq.second][j - freq.first] + 1,
                    });
                }
            }
        }
        return dp[n][m];
    }
};