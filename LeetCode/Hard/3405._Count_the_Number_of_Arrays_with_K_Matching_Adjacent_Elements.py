# You are given three integers n, m, k. A good array arr of size n is defined as follows:
#
# Each element in arr is in the inclusive range [1, m].
# Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
# Return the number of good arrays that can be formed.
#
# Since the answer may be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: n = 3, m = 2, k = 1
#
# Output: 4
#
# Explanation:
#
# There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
# Hence, the answer is 4.
# Example 2:
#
# Input: n = 4, m = 2, k = 2
#
# Output: 6
#
# Explanation:
#
# The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
# Hence, the answer is 6.
# Example 3:
#
# Input: n = 5, m = 2, k = 0
#
# Output: 2
#
# Explanation:
#
# The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
#
#
# Constraints:
#
# 1 <= n <= 105
# 1 <= m <= 105
# 0 <= k <= n - 1
# Solution
# Python O(log(N - k)) O(1) Math Combinatorics
class Solution:
    MOD: int = 1000000007
    bound: int = 100000
    fact: list[int] = [0] * bound
    inv_fact: list[int] = [0] * bound

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        self.preprocessing()
        return self.binom_coef(n - 1, k) * m % self.MOD * self.binary_pow(m - 1, n - k - 1) % self.MOD

    def binary_pow(self, x: int, n: int) -> int:
        output: int = 1
        while n:
            if n & 1: output = output * x % self.MOD
            x = x * x % self.MOD
            n >>= 1
        return output

    def binom_coef(self, n: int, m: int) -> int:
        return self.fact[n] * self.inv_fact[m] % self.MOD * self.inv_fact[n - m] % self.MOD

    def preprocessing(self) -> None:
        if self.fact[0]: return
        self.fact[0] = 1
        for i in range(1, self.bound):
            self.fact[i] = self.fact[i - 1] * i % self.MOD
        self.inv_fact[self.bound - 1] = self.binary_pow(self.fact[self.bound - 1], self.MOD - 2)
        for i in range(self.bound - 1, 0, -1):
            self.inv_fact[i - 1] = self.inv_fact[i] * i % self.MOD

# C++ O(log(N - k)) O(1) Math Combinatorics
class Solution {
public:
    int MOD = 1e9 + 7;
    const static int bound = 1e5;
    long long fact[bound];
    long long inv_fact[bound];

    int countGoodArrays(int n, int m, int k) {
        preprocessing();
        return binomCoef(n - 1, k) * m % MOD * binaryPow(m - 1, n - k - 1) % MOD;
    }

    long long binaryPow(long long x, int n) {
        long long output = 1;
        while (n) {
            if (n & 1) output = output * x % MOD;
            x = x * x % MOD;
            n >>= 1;
        }
        return output;
    }

    long long binomCoef(int n, int m) {
        return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD;
    }

    void preprocessing() {
        if (fact[0]) return;
        fact[0] = 1;
        for (int i = 1; i < bound; ++i) fact[i] = fact[i - 1] * i % MOD;
        inv_fact[bound - 1] = binaryPow(fact[bound - 1], MOD - 2);
        for (int i = bound - 1; i; --i) inv_fact[i - 1] = inv_fact[i] * i % MOD;
    }
};