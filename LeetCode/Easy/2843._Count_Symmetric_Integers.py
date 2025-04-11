# You are given two positive integers low and high.
#
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
#
# Return the number of symmetric integers in the range [low, high].
#
#
#
# Example 1:
#
# Input: low = 1, high = 100
# Output: 9
# Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
# Example 2:
#
# Input: low = 1200, high = 1230
# Output: 4
# Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
#
#
# Constraints:
#
# 1 <= low <= high <= 104
# Solution
# Python O(log(N)^4) O(log(N)^4) DynamicProgramming
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def dfs(pos: int, s: str, tight: bool, left: int, right: int, zeros: int) -> int:
            if pos >= len(s):
                return left == right and not ((pos - zeros) & 1) and zeros != pos
            bound: int = 9 if tight else int(s[pos])
            score: int = 0
            for digit in range(bound + 1):
                new_tight: bool = tight or (digit < bound)
                if not digit and zeros == pos:
                    score += dfs(pos + 1, s, new_tight, left, right, zeros + 1)
                else:
                    len_left: int = len(s) - zeros
                    if pos - zeros < len_left // 2:
                        score += dfs(pos + 1, s, new_tight, left + digit, right, zeros)
                    else:
                        score += dfs(pos + 1, s, new_tight, left, right + digit, zeros)
            return score

        right: int = dfs(0, str(high), False, 0, 0, 0)
        left: int = dfs(0, str(low - 1), False, 0, 0, 0)
        return right - left

# C++ O(log(N)^4) O(log(N)^4) DynamicProgramming
class Solution {
private:
    int dp[5][2][45][45][5];
public:
    int dfs(int pos, string s, bool tight, int left, int right, int zeros) {
        if (pos >= s.size()) {
            return (left == right) && !((pos - zeros) & 1) && zeros != pos;
        }
        if (dp[pos][tight][left][right][zeros] != -1) {
            return dp[pos][tight][left][right][zeros];
        }
        int bound = (tight? 9 : s[pos] - '0');
        int score = 0;
        for (int digit = 0; digit <= bound; ++digit) {
            bool newTight = tight || (digit < bound);
            if (!digit && zeros == pos) {
                score += dfs(pos + 1, s, newTight, left, right, zeros + 1);
            } else {
                int lenLeft = s.size() - zeros;
                if (pos - zeros < lenLeft / 2) {
                    score += dfs(pos + 1, s, newTight, left + digit, right, zeros);
                } else {
                    score += dfs(pos + 1, s, newTight, left, right + digit, zeros);
                }
            }
        }
        dp[pos][tight][left][right][zeros] = score;
        return score;
    }
    int countSymmetricIntegers(int low, int high) {
        memset(dp, -1, sizeof(dp));
        int right = dfs(0, to_string(high), false, 0, 0, 0);
        memset(dp, -1, sizeof(dp));
        int left = dfs(0, to_string(low - 1), false, 0, 0, 0);
        return right - left;
    }
};