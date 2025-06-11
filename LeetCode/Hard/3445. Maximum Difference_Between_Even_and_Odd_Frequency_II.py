# You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:
#
# subs has a size of at least k.
# Character a has an odd frequency in subs.
# Character b has an even frequency in subs.
# Return the maximum difference.
#
# Note that subs can contain more than 2 distinct characters.
#
#
#
# Example 1:
#
# Input: s = "12233", k = 4
#
# Output: -1
#
# Explanation:
#
# For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.
#
# Example 2:
#
# Input: s = "1122211", k = 3
#
# Output: 1
#
# Explanation:
#
# For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.
#
# Example 3:
#
# Input: s = "110", k = 3
#
# Output: -1
#
#
#
# Constraints:
#
# 3 <= s.length <= 3 * 104
# s consists only of digits '0' to '4'.
# The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
# 1 <= k <= s.length
# Solution
# Python O(N) O(N) DynamicProgramming String
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n: int = len(s)
        output: int = float('-inf')
        for a in range(5):
            for b in range(5):
                if a == b: continue
                ps1: list[int] = [0] * (n + 1)
                ps2: list[int] = [0] * (n + 1)
                for i in range(1, n + 1):
                    ps1[i] = ps1[i - 1] + int(s[i - 1] == str(a))
                    ps2[i] = ps2[i - 1] + int(s[i - 1] == str(b))
                dp: list[list[int]] = [[float('-inf')] * 2 for _ in range(2)]
                left: int = 0
                for right in range(k, n + 1):
                    while right - left >= k and ps1[right] > ps1[left] and ps2[right] > ps2[left]:
                        pa: int = ps1[left] & 1
                        pb: int = ps2[left] & 1
                        dp[pa][pb] = max(dp[pa][pb], ps2[left] - ps1[left])
                        left += 1
                    pa: int = ps1[right] & 1
                    pb: int = ps2[right] & 1
                    need: int = dp[1 - pa][pb]
                    if need != float('-inf'): output = max(output, (ps1[right] - ps2[right]) + need)
        return -1 if output == float('-inf') else output

# C++ O(N) O(N) DynamicProgamming String
class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.size(), output = INT_MIN;
        for (int a = 0; a <= 4; ++a) {
            for (int b = 0; b <= 4; ++b) {
                if (a == b) continue;
                vector<int> ps1(n + 1);
                vector<int> ps2(n + 1);
                for (int i = 1; i <= n; ++i) {
                    ps1[i] = ps1[i - 1] + (s[i - 1] - '0' == a);
                    ps2[i] = ps2[i - 1] + (s[i - 1] - '0' == b);
                }
                vector<vector<int>> dp = {{INT_MIN, INT_MIN}, {INT_MIN, INT_MIN}};
                int left = 0;
                for (int right = k; right <= n; ++right) {
                    while (right - left >= k && ps1[right] > ps1[left] && ps2[right] > ps2[left]) {
                        int pa = ps1[left] % 2, pb = ps2[left] % 2;
                        dp[pa][pb] = max(dp[pa][pb], ps2[left] - ps1[left]);
                        ++left;
                    }
                    int pa = ps1[right] % 2, pb = ps2[right] % 2;
                    int need = dp[1 - pa][pb];
                    if (need != INT_MIN) output = max(output, (ps1[right] - ps2[right]) + need);
                }
            }
        }
        return (output != INT_MIN? output : -1);
    }
};