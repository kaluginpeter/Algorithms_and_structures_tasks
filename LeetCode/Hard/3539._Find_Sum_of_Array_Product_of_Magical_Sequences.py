# You are given two integers, m and k, and an integer array nums.
#
# A sequence of integers seq is called magical if:
# seq has a size of m.
# 0 <= seq[i] < nums.length
# The binary representation of 2seq[0] + 2seq[1] + ... + 2seq[m - 1] has k set bits.
# The array product of this sequence is defined as prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]]).
#
# Return the sum of the array products for all valid magical sequences.
#
# Since the answer may be large, return it modulo 109 + 7.
#
# A set bit refers to a bit in the binary representation of a number that has a value of 1.
#
#
#
# Example 1:
#
# Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]
#
# Output: 991600007
#
# Explanation:
#
# All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.
#
# Example 2:
#
# Input: m = 2, k = 2, nums = [5,4,3,2,1]
#
# Output: 170
#
# Explanation:
#
# The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].
#
# Example 3:
#
# Input: m = 1, k = 1, nums = [28]
#
# Output: 28
#
# Explanation:
#
# The only magical sequence is [0].
#
#
#
# Constraints:
#
# 1 <= k <= m <= 30
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 108
# Solution
# C++ O(N * M^3 * K) O(N * M^2) DynamicProgramming
using namespace std;
using ll = long long;
const int MOD = 1e9 + 7;
class Solution {
public:
    int magicalSum(int m, int k, vector<int>& nums) {
        int n = nums.size();
        vector<vector<ll>> powNum(n, vector<ll>(m + 1, 1));
        for (int i = 0; i < n; i++)
            for (int j = 1; j <= m; j++)
                powNum[i][j] = (powNum[i][j - 1] * nums[i]) % MOD;
        vector<vector<ll>> C(m + 1, vector<ll>(m + 1, 0));
        for (int i = 0; i <= m; i++) {
            C[i][0] = C[i][i] = 1;
            for (int j = 1; j < i; j++)
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
        static ll dp[55][35][35][35];
        static bool vis[55][35][35][35];
        memset(vis, 0, sizeof(vis));
        function<ll(int,int,int,int)> dfs = [&](int pos, int carry, int used, int ones) -> ll {
            if (pos == n) {
                int extra = 0;
                int c = carry;
                while (c) {
                    if (c & 1) extra++;
                    c >>= 1;
                }
                return (used == m && ones + extra == k) ? 1 : 0;
            }
            if (vis[pos][carry][used][ones]) return dp[pos][carry][used][ones];
            vis[pos][carry][used][ones] = 1;
            ll ans = 0;
            for (int cnt = 0; cnt + used <= m; cnt++) {
                int total = carry + cnt;
                int bit = total & 1;
                int ncarry = total >> 1;
                int nones = ones + bit;
                ll sub = dfs(pos + 1, ncarry, used + cnt, nones);
                if (!sub) continue;
                ll ways = C[m - used][cnt];
                ll prod = powNum[pos][cnt];
                ans = (ans + sub * ways % MOD * prod) % MOD;
            }
            return dp[pos][carry][used][ones] = ans;
        };
        return (int)dfs(0, 0, 0, 0);
    }
};

# Python O(N * M^3 * K) O(N * M^2) DynamicProgramming
from functools import lru_cache
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n: int = len(nums)
        mod: int = 10**9 + 7
        pow_num: list[list[int]] = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                pow_num[i][j] = (pow_num[i][j - 1] * nums[i]) % mod
        c: list[list[int]] = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            c[i][0] = c[i][i] = 1
            for j in range(1, i):
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod
        @lru_cache(None)
        def dfs(pos: int, carry: int, used: int, ones: int) -> int:
            if pos == n:
                extra: int = bin(carry).count('1')
                return int(used == m and ones + extra == k)
            output: int = 0
            for cnt in range(m - used + 1):
                total: int = carry + cnt
                bit: int = total & 1
                ncarry: int = total >> 1
                nones: int = ones + bit
                sub: int = dfs(pos + 1, ncarry, used + cnt, nones)
                if not sub: continue
                ways: int = c[m - used][cnt]
                prod: int = pow_num[pos][cnt]
                output = (output + sub * ways % mod * prod) % mod
            return output
        return dfs(0, 0, 0, 0)