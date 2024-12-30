# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:
#
# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.
#
# A good string is a string constructed by the above process having a length between low and high (inclusive).
#
# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: low = 3, high = 3, zero = 1, one = 1
# Output: 8
# Explanation:
# One possible valid good string is "011".
# It can be constructed as follows: "" -> "0" -> "01" -> "011".
# All binary strings from "000" to "111" are good strings in this example.
# Example 2:
#
# Input: low = 2, high = 3, zero = 1, one = 2
# Output: 5
# Explanation: The good strings are "00", "11", "000", "110", and "011".
#
#
# Constraints:
#
# 1 <= low <= high <= 105
# 1 <= zero, one <= low
# Solution
# Python O(N) O(N) Dynamic Programming
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp: list[int] = [0] * (high + 1)
        MOD: int = 10**9 + 7
        dp[0] = 1
        for L in range(high + 1):
            if L + one <= high:
                dp[L + one] = (dp[L + one] + dp[L]) % MOD
            if L + zero <= high:
                dp[L + zero] = (dp[L + zero] + dp[L]) % MOD
        score: int = 0
        for i in range(low, high + 1):
            score = (score + dp[i]) % MOD
        return score

# C++ O(N) O(N) Dynamic Programming
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        int bound = high + 1;
        std::vector<int> dp(bound);
        int MOD = 1000000007;
        dp[0] = 1;
        for (int L = 0; L <= high; ++L) {
            if (L + zero <= high) {
                dp[L + zero] = (dp[L + zero] + dp[L]) % MOD;
            }
            if (L + one <= high) {
                dp[L + one] = (dp[L + one] + dp[L]) % MOD;
            }
        }
        int score = 0;
        for (int i = low; i <= high; ++i) {
            score = (score + dp[i]) % MOD;
        }
        return score;
    }
};