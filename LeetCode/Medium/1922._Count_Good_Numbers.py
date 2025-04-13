# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
#
# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
#
# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
# Example 2:
#
# Input: n = 4
# Output: 400
# Example 3:
#
# Input: n = 50
# Output: 564908303
#
#
# Constraints:
#
# 1 <= n <= 1015
# Solution
# Python O(logN) O(logN) Math Recursion
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD: int = 1000000007
        odd: int = pow(4, n // 2, MOD)
        if n & 1: return pow(5, n // 2 + 1, MOD) * odd % MOD
        return pow(5, n // 2, MOD) * odd % MOD

# C++ O(logN) O(logN) Math Recursion
class Solution {
public:
    long long powByModule(int x, long long n, int m) {
        if (!n) return 1LL;
        else if (n & 1) return x * powByModule(x, n - 1, m) % m;
        long long even = powByModule(x, n / 2, m) % m;
        return even * even % m;
    }
    int countGoodNumbers(long long n) {
        int MOD = 1000000007;
        long long odd = powByModule(4, n / 2, MOD);
        if (n & 1) return powByModule(5, n / 2 + 1, MOD) * odd % MOD;
        return powByModule(5, n / 2, MOD) * odd % MOD;
    }
};