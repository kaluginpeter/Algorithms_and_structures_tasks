/*
You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).



Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]​​​​​​​
Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
All arrays meet the ZigZag conditions.



Constraints:

3 <= n <= 2000
1 <= l < r <= 2000
*/
// Solution
// C++ O(NM) O(M) DynamicProgramming
constexpr int MOD = 1'000'000'007;

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        std::vector<int> dp0(m, 0), dp1(m, 0), sum0(m + 1, 0), sum1(m + 1, 0);
        for (int i = 0; i < m; ++i) dp0[i] = dp1[i] = 1;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                sum0[j + 1] = (sum0[j] + dp0[j]) % MOD;
                sum1[j + 1] = (sum1[j] + dp1[j]) % MOD;
            }
            for (int j = 0; j < m; ++j) {
                dp0[j] = (sum1[m] - sum1[j + 1] + MOD) % MOD;
                dp1[j] = sum0[j];
            }
        }
        auto op = [](int acc, int x) { return (acc + x) % MOD; };
        auto ans0 = std::reduce(dp0.begin(), dp0.end(), 0, op);
        auto ans1 = std::reduce(dp1.begin(), dp1.end(), 0, op);
        return (ans0 + ans1) % MOD;
    }
};

// Python O(NM) O(M) DynamicProgramming
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        segment: int = r - l + 1
        dp_up: list[int] = [0] * segment
        dp_down: list[int] = [0] * segment
        for i in range(segment):
            dp_up[i] = i
            dp_down[i] = segment - i - 1
        mod: int = 10**9 + 7
        if n == 2: return (sum(dp_up) + sum(dp_down)) % mod
        for n in range(3, n + 1):
            new_up: list[int] = [0] * segment
            new_down: list[int] = [0] * segment
            pref_up: int = 0
            pref_down: int = 0
            prefix_up: list[int] = [0] * segment
            prefix_down: list[int] = [0] * segment
            for v in range(segment):
                pref_up += dp_up[v]
                pref_up %= mod
                prefix_up[v] = pref_up
                pref_down += dp_down[v]
                pref_down %= mod
                prefix_down[v] = pref_down
            total_up: int = prefix_up[-1]
            for v in range(segment):
                if not v:
                    new_up[v] = 0
                else:
                    new_up[v] = prefix_down[v - 1]
                up: int = total_up - prefix_up[v]
                if up < 0: up += mod
                new_down[v] = up
            dp_up, dp_down = new_up, new_down
        return (sum(dp_up) + sum(dp_down)) % mod