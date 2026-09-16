/*
Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

 

Example 1:


Input: n = 4, k = 2
Output: 5
Explanation: The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.
 

Constraints:

2 <= n <= 1000
1 <= k <= n-1
*/
// Solution
// Go O(N) O(N) Math
var mod int64 = 1_000_000_007
func modpow(base int64, exp int64) int64 {
    var output int64 = 1
    base %= mod
    for exp > 0 {
        if exp & 1 == 1 {output = output * base % mod }
        base = base * base % mod
        exp >>= 1
    }
    return output
}
func numberOfSets(n int, k int) int {
    var m, r int = n + k - 1, k << 1
    var fact, invFact []int64 = make([]int64, m + 1), make([]int64, m + 1)
    fact[0] = 1
    for i := 1; i <= m; i++ { fact[i] = fact[i - 1] * int64(i) % mod }
    invFact[m] = modpow(fact[m], mod - 2)
    for i := m; i >= 1; i-- { invFact[i - 1] = invFact[i] * int64(i) % mod }
    return int(fact[m] * invFact[r] % mod * invFact[m - r] % mod)
}

// C++ O(N) O(N) Math
constexpr int MOD = 1'000'000'007;

class Solution {
private:
    long long modpow(long long base, long long exp) {
        long long result = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp & 1) result = result * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return result;
    }
public:
    int numberOfSets(int n, int k) {
        int m = n + k - 1, r = k << 1;
        vector<long long> fact(m + 1), invFact(m + 1);
        fact[0] = 1;
        for (int i = 1; i <= m; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[m] = modpow(fact[m], MOD - 2);
        for (int i = m; i >= 1; --i) invFact[i - 1] = invFact[i] * i % MOD;
        long long output = fact[m] * invFact[r] % MOD * invFact[m - r] % MOD;
        return output;
    }
};