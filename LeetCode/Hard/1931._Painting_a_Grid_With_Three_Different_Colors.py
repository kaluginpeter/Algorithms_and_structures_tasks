# You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.
#
# Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
#
# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are shown in the image above.
# Example 2:
#
#
# Input: m = 1, n = 2
# Output: 6
# Explanation: The six possible colorings are shown in the image above.
# Example 3:
#
# Input: m = 5, n = 5
# Output: 580986
#
#
# Constraints:
#
# 1 <= m <= 5
# 1 <= n <= 1000
# Solution
# Python O(3^2M * N) O(3^2M) DynamicProgramming
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod: int = 10**9 + 7
        valid: dict[int, list[int]] = dict()
        for mask in range(3**m):
            color: list[int] = list()
            mm: int = mask
            for i in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)): continue
            valid[mask] = color
        adjacent: dict[int, list[int]] = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)): adjacent[mask1].append(mask2)
        f: list[int] = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            g: list[int] = [0] * (3**m)
            for mask2 in valid.keys():
                for mask1 in adjacent[mask2]:
                    g[mask2] += f[mask1]
                    if g[mask2] >= mod: g[mask2] -= mod
            f = g
        return sum(f) % mod

# C++ O(3^2M * N) O(3^2M) DynamicProgramming
class Solution {
    static constexpr int mod = 1000000007;
public:
    int colorTheGrid(int m, int n) {
        unordered_map<int, vector<int>> valid;
        int mask_end = pow(3, m);
        for (int mask = 0; mask < mask_end; ++mask) {
            vector<int> color;
            int mm = mask;
            for (int i = 0; i < m; ++i) {
                color.push_back(mm % 3);
                mm /= 3;
            }
            bool check = true;
            for (int i = 0; i < m - 1; ++i) {
                if (color[i] == color[i + 1]) {
                    check = false;
                    break;
                }
            }
            if (check) valid[mask] = move(color);
        }
        unordered_map<int, vector<int>> adjacent;
        for (const auto& [mask1, color1] : valid) {
            for (const auto& [mask2, color2] : valid) {
                bool check = true;
                for (int i = 0; i < m; ++i) {
                    if (color1[i] == color2[i]) {
                        check = false;
                        break;
                    }
                }
                if (check) adjacent[mask1].push_back(mask2);
            }
        }
        vector<int> f(mask_end);
        for (const auto& [mask, _] : valid) f[mask] = 1;
        for (int i = 1; i < n; ++i) {
            vector<int> g(mask_end);
            for (const auto& [mask2, _] : valid) {
                for (int mask1 : adjacent[mask2]) {
                    g[mask2] += f[mask1];
                    if (g[mask2] >= mod) g[mask2] -= mod;
                }
            }
            f = move(g);
        }
        int ans = 0;
        for (int num : f) {
            ans += num;
            if (ans >= mod) ans -= mod;
        }
        return ans;
    }
};