# Given two positive integers n and x.
#
# Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.
#
# Since the result can be very large, return it modulo 109 + 7.
#
# For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.
#
#
#
# Example 1:
#
# Input: n = 10, x = 2
# Output: 1
# Explanation: We can express n as the following: n = 32 + 12 = 10.
# It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
# Example 2:
#
# Input: n = 4, x = 1
# Output: 2
# Explanation: We can express n in the following ways:
# - n = 41 = 4.
# - n = 31 + 11 = 4.
#
#
# Constraints:
#
# 1 <= n <= 300
# 1 <= x <= 5
# Solution
# Python O(N^(1 + 1/x)) O(N) DynamicProgramming
class Solution:
    def get_bound(self, n: int, x: int) -> int:
        output: int = 1
        while pow(output, x) <= n: output += 1
        return output

    def numberOfWays(self, n: int, x: int) -> int:
        bound: int = self.get_bound(n, x)
        hashmap: list[int] = [0] * (n + 1)
        mod: int = int(1e9) + 7
        hashmap[0] = 1
        for i in range(1, bound):
            ix: int = pow(i, x)
            for j in range(n - ix, -1, -1):
                if not hashmap[j]: continue
                hashmap[ix + j] = (hashmap[ix + j] + hashmap[j]) % mod
        return hashmap[n]

# C++ O(N^(1 + 1/x)) O(N) DynamicProgramming
class Solution {
public:
    int getBound(int n, int x) {
        int bound = 0;
        while (std::pow(bound, x) <= n) ++bound;
        return bound;
    };

    int numberOfWays(int n, int x) {
        int bound = getBound(n, x), output = 0, mod = 1e9 + 7;
        std::array<int, 301> hashmap{};
        hashmap[0] = 1;
        for (int i = 1; i < bound; ++i) {
            int ix = std::pow(i, x);
            for (int j = n - ix; j >= 0; --j) {
                if (!hashmap[j]) continue;
                hashmap[ix + j] = (hashmap[ix + j] + hashmap[j]) % mod;
            }
        }
        return hashmap[n];
    }
};