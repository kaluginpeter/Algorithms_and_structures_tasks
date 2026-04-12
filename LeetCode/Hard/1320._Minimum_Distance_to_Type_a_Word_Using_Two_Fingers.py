# You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.
#
# For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
# Given the string word, return the minimum total distance to type such string using only two fingers.
#
# The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.
#
# Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.
#
#
#
# Example 1:
#
# Input: word = "CAKE"
# Output: 3
# Explanation: Using two fingers, one optimal way to type "CAKE" is:
# Finger 1 on letter 'C' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2
# Finger 2 on letter 'K' -> cost = 0
# Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1
# Total distance = 3
# Example 2:
#
# Input: word = "HAPPY"
# Output: 6
# Explanation: Using two fingers, one optimal way to type "HAPPY" is:
# Finger 1 on letter 'H' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
# Finger 2 on letter 'P' -> cost = 0
# Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
# Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
# Total distance = 6
#
#
# Constraints:
#
# 2 <= word.length <= 300
# word consists of uppercase English letters.
# Solution
# Python O(N26*26) O(N26*26) DynamicProgramming
class Solution:
    def f(self, p: int, q: int) -> int:
        x1: int = p // 6
        y1: int = p % 6
        x2: int = q // 6
        y2: int = q % 6
        return abs(x1 - x2) + abs(y1 - y2)

    def minimumDistance(self, word: str) -> int:
        n: int = len(word)
        dp: list[list[int]] = [[float('inf')] * 26 for _ in range(n)]
        for i in range(26): dp[0][i] = 0
        for i in range(1, n):
            cur: int = ord(word[i]) - 65
            prev: int = ord(word[i - 1]) - 65
            d: int = self.f(prev, cur)
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + d)
                if prev == j:
                    for k in range(26):
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + self.f(k, cur))
        return min(dp[n - 1])

# C++ O(N26*26) O(N26*26) DynamicProgramming
class Solution {
public:
    int f(int& p, int& q) {
        int x1 = p / 6, y1 = p % 6;
        int x2 = q / 6, y2 = q % 6;
        return std::abs(x1 - x2) + std::abs(y1 - y2);
    }
    int minimumDistance(string word) {
        size_t n = word.size();
        std::vector<std::vector<int>> dp(n, std::vector<int>(26, INT_MAX >> 1));
        std::fill(dp[0].begin(), dp[0].end(), 0);
        for (int i = 1; i < n; ++i) {
            int cur = word[i] - 'A', prev = word[i - 1] - 'A';
            int d = f(prev, cur);
            for (int j = 0; j < 26; ++j) {
                dp[i][j] = std::min(dp[i][j], dp[i - 1][j] + d);
                if (prev == j) {
                    for (int k = 0; k < 26; ++k) {
                        dp[i][j] = std::min(dp[i][j], dp[i - 1][k] + f(k, cur));
                    }
                }
            }
        }
        return *std::min_element(dp[n - 1].begin(), dp[n - 1].end());
    }
};