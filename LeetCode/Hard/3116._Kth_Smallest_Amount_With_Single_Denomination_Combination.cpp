/*
You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.



Example 1:

Input: coins = [3,6,9], k = 3

Output: 9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:

Input: coins = [5,2], k = 7

Output: 12

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.



Constraints:

1 <= coins.length <= 15
1 <= coins[i] <= 25
1 <= k <= 2 * 109
coins contains pairwise distinct integers.


*/
// Solution
// C++ O(2^N) O(2^N) Math BinarySearch
class Solution {
public:
    using ll = long long;
    long long findKthSmallest(vector<int>& coins, int k) {
        int n = coins.size();
        int m = (1 << n);
        std::sort(coins.begin(), coins.end());
        std::vector<int> bit_count(m);
        std::vector<ll> lcm(m);
        ll l = k, r = 1ll * coins[0] * k + 1;
        for (int mask = 1; mask < m; mask++) {
            ll cur_lcm = 1;
            for (int i = 0; i < n; i++) {
                if (mask >> i & 1) {
                    ll tmp = cur_lcm / gcd(cur_lcm, coins[i]);
                    if (tmp <= r / coins[i]) {
                        cur_lcm = tmp * coins[i];
                    } else {
                        cur_lcm = r + 1;
                        break;
                    }
                    bit_count[mask]++;
                }
            }
            lcm[mask] = cur_lcm;
        }

        auto get = [&](ll x) -> ll {
            ll count = 0;
            for (int mask = 1; mask < m; mask++) {
                if (lcm[mask] > x) {
                    continue;
                }
                if (bit_count[mask] & 1) {
                    count += x / lcm[mask];
                } else {
                    count -= x / lcm[mask];
                }
            }
            return count;
        };

        while (l < r) {
            ll x = (l + r) >> 1;
            if (get(x) >= k) {
                r = x;
            } else {
                l = x + 1;
            }
        }
        return l;
    }
};