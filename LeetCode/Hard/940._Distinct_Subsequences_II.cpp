/*
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
 

Example 1:

Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:

Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".
Example 3:

Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters.
*/
// Solution
// C++ O(N) O(N) DynamicProgramming
constexpr const int32_t MOD = 1e9 + 7;
class Solution {
public:
    int distinctSubseqII(string s) {
        const size_t n = s.length();
        std::vector<int> dp(n + 1);
        dp[0] = 1;
        std::array<int, 26> last;
        last.fill(-1);
        for(size_t i = 0; i < n; ++i) {
            uint8_t x = s[i] - 'a';
            dp[i + 1] = (dp[i] << 1) % MOD;
            if (last[x] >= 0) dp[i + 1] -= dp[last[x]];
            dp[i + 1] %= MOD;
            last[x] = i;
        }
        --dp[n];
        if(dp[n] < 0) dp[n] += MOD;
        return dp[n];
    }
};