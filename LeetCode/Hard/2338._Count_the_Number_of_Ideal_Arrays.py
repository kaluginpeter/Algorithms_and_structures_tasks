# You are given two integers n and maxValue, which are used to describe an ideal array.
#
# A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:
#
# Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
# Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
# Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: n = 2, maxValue = 5
# Output: 10
# Explanation: The following are the possible ideal arrays:
# - Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
# - Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
# - Arrays starting with the value 3 (1 array): [3,3]
# - Arrays starting with the value 4 (1 array): [4,4]
# - Arrays starting with the value 5 (1 array): [5,5]
# There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
# Example 2:
#
# Input: n = 5, maxValue = 3
# Output: 11
# Explanation: The following are the possible ideal arrays:
# - Arrays starting with the value 1 (9 arrays):
#    - With no other distinct values (1 array): [1,1,1,1,1]
#    - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
#    - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
# - Arrays starting with the value 2 (1 array): [2,2,2,2,2]
# - Arrays starting with the value 3 (1 array): [3,3,3,3,3]
# There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
#
#
# Constraints:
#
# 2 <= n <= 104
# 1 <= maxValue <= 104
# Solution
# Python O(maxVallog(maxVal) * min(n, 14)) O(maxVal)
class Solution:
    MOD: int = 1000000007
    fact_memo: list[int] = [0] * 100000
    dp: list[list[int]] = [[0] * 15 for _ in range(100000)]
    def fast_power(self, x: int, base: int, m: int) -> int:
        output: int = 1
        while base:
            if base & 1: output = (output * x) % m
            x = (x * x) % m
            base >>= 1
        return output

    def fact(self, n: int) -> int:
        if not n: return 1
        if self.fact_memo[n]: return self.fact_memo[n]
        self.fact_memo[n] = (n * self.fact(n - 1)) % self.MOD
        return self.fact_memo[n]

    def mod_inv(self, x: int, y: int) -> int:
        return (((self.fact(x) * self.fast_power(self.fact(y), self.MOD - 2, self.MOD)) % self.MOD) * self.fast_power(self.fact(x - y), self.MOD - 2, self.MOD)) % self.MOD

    def idealArrays(self, n: int, maxValue: int) -> int:
        for num in range(1, maxValue + 1):
            for d in range(1, min(n, 14) + 1):
                self.dp[num][d] = 0
        for num in range(1, maxValue + 1):
            self.dp[num][1] = 1
            div: int = 2
            while div * num <= maxValue:
                for k in range(1, min(n, 14)):
                    self.dp[num * div][k + 1] += self.dp[num][k]
                div += 1
        output: int = 0
        for num in range(1, maxValue + 1):
            for d in range(1, min(n, 14) + 1):
                output = (output + self.mod_inv(n - 1, n - d) * self.dp[num][d]) % self.MOD
        return output

# C++ O(maxVallog(maxVal) * min(n, 14) O(maxVal)
class Solution {
private:
    int MOD = 1e9 + 7;
    int factMemo[100000];
    int dp[100000][15];
public:
    long long fastPower(long long x, long long base, long long m) {
        long long output = 1;
        while (base > 0) {
            if (base & 1) output = (output * x) % m;
            x = (x * x) % m;
            base >>= 1;
        }
        return output;
    }
    long long fact(long long n) {
        if (n == 0) return 1;
        if (factMemo[n]) return factMemo[n];
        factMemo[n] = (n * fact(n - 1)) % MOD;
        return factMemo[n];
    }
    long long modInv(long long x, long long y) {
        return (((fact(x) * fastPower(fact(y), MOD - 2, MOD)) % MOD) * fastPower(fact(x - y), MOD - 2, MOD)) % MOD;
    }

    int idealArrays(int n, int maxVal) {
        for (int num = 1; num <= maxVal; ++num)
            for (int d = 1; d <= min(n, 14); ++d) dp[num][d] = 0;
        for (int num = 1; num <= maxVal; ++num) {
            dp[num][1] = 1;
            for (int div = 2; div * num <= maxVal; ++div)
                for (int k = 1; k < min(n, 14); ++k)
                    dp[num * div][k + 1] += dp[num][k];
        }
        long long output = 0;
        for (int num = 1; num <= maxVal; ++num)
            for (int div = 1; div <= min(n, 14); ++div)
                output = (output + modInv(n - 1, n - div) * dp[num][div]) % MOD;
        return output;
    }
};