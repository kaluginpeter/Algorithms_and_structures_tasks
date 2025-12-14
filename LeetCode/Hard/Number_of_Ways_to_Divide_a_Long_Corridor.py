# Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.
#
# One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.
#
# Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.
#
# Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.
#
#
#
# Example 1:
#
#
# Input: corridor = "SSPPSPS"
# Output: 3
# Explanation: There are 3 different ways to divide the corridor.
# The black bars in the above image indicate the two room dividers already installed.
# Note that in each of the ways, each section has exactly two seats.
# Example 2:
#
#
# Input: corridor = "PPSPSP"
# Output: 1
# Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
# Installing any would create some section that does not have exactly two seats.
# Example 3:
#
#
# Input: corridor = "S"
# Output: 0
# Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
#
#
# Constraints:
#
# n == corridor.length
# 1 <= n <= 105
# corridor[i] is either 'S' or 'P'.
# Solution
# Python O(N) O(1) Combinatorics
mod: int = 10**9 + 7
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        output: int = 0
        n: int = len(corridor)
        left: int = 0
        right: int = 0
        p_left: int = -1
        p_right: int = -1
        while right < n:
            cur: int = 0
            while cur < 2 and right < n:
                if corridor[right] == 'S':
                    cur += 1
                    if cur == 1: left = right
                right += 1
            if cur and cur < 2: return 0
            if p_left == -1: output += int(bool(cur))
            else: output = output * (left - p_right) % mod
            p_left = left
            p_right = right - 1
            left = right
        return output

# C++ O(N) O(1) Combinatorics
constexpr int mod = 1000000007;
class Solution {
public:
    int numberOfWays(string corridor) {
        int output = 0;
        int n = corridor.size(), left = 0, right = 0, pLeft = -1, pRight = -1;
        while (right < n) {
            int cur = 0;
            while (cur < 2 && right < n) {
                if (corridor[right] == 'S') {
                    ++cur;
                    if (cur == 1) left = right;
                }
                ++right;
            }
            if (cur && cur < 2) return 0;
            if (pLeft == -1) (cur ? ++output : output);
            else output = (1LL * output * (left - pRight)) % mod;
            pLeft = left;
            pRight = right - 1;
            left = right;
        }
        return output;
    }
};