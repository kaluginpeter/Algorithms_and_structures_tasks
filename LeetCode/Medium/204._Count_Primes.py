# Given an integer n, return the number of prime numbers that are strictly less than n.
#
#
#
# Example 1:
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:
#
# Input: n = 0
# Output: 0
# Example 3:
#
# Input: n = 1
# Output: 0
#
#
# Constraints:
#
# 0 <= n <= 5 * 106
# Solution
# Python O(NlogN) O(N) DynamicProgramming
class Solution:
    def countPrimes(self, n: int) -> int:
        output: int = int(n > 2)
        dp: list[bool] = [True] * n
        for i in range(3, n, 2):
            if not dp[i]: continue
            elif i % 2 == 0: continue
            output += 1
            for j in range(i + i, n, i): dp[j] = False
        return output

# C++ O(NlogN) O(N) DynamicProgramming
class Solution {
public:
    int countPrimes(int n) {
        int output = (n > 2 ? 1 : 0);
        std::vector<bool> dp(n, true);
        for (size_t i = 3; i < n; i += 2) {
            if (!dp[i]) continue;
            else if (i % 2 == 0) continue;
            ++output;
            for (size_t j = i + i; j < n; j += i) dp[j] = false;
        }
        return output;
    }
};