# You are given a binary string s.
#
# Return the number of substrings with dominant ones.
#
# A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.
#
#
#
# Example 1:
#
# Input: s = "00011"
#
# Output: 5
#
# Explanation:
#
# The substrings with dominant ones are shown in the table below.
#
# i	j	s[i..j]	Number of Zeros	Number of Ones
# 3	3	1	0	1
# 4	4	1	0	1
# 2	3	01	1	1
# 3	4	11	0	2
# 2	4	011	1	2
# Example 2:
#
# Input: s = "101101"
#
# Output: 16
#
# Explanation:
#
# The substrings with non-dominant ones are shown in the table below.
#
# Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.
#
# i	j	s[i..j]	Number of Zeros	Number of Ones
# 1	1	0	1	0
# 4	4	0	1	0
# 1	4	0110	2	2
# 0	4	10110	2	3
# 1	5	01101	2	3
#
#
# Constraints:
#
# 1 <= s.length <= 4 * 104
# s consists only of characters '0' and '1'.
# Solution
# Python O(Nsqrt(N)) O(N) Prefix SlidingWindow
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n: int = len(s)
        pre: list[int] = [0] * (n + 1)
        pre[0] = -1
        for i in range(n):
            if not i or s[i - 1] == '0': pre[i + 1] = i
            else: pre[i + 1] = pre[i]
        output: int = 0
        for i in range(1, n + 1):
            zeros: int = s[i - 1] == '0'
            j: int = i
            while j and zeros**2 <= n:
                ones: int = i - pre[j] - zeros
                if zeros**2 <= ones:
                    output += min(j - pre[j], ones - zeros**2 + 1)
                j = pre[j]
                zeros += 1
        return output

# C++ O(Nsqrt(N)) O(N) SlidingWindow
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        std::vector<int> pre(n + 1);
        pre[0] = -1;
        for (int i = 0; i < n; ++i) {
            if (i == 0 || (i > 0 && s[i - 1] == '0')) pre[i + 1] = i;
            else pre[i + 1] = pre[i];
        }
        int output = 0;
        for (int i = 1; i <= n; ++i) {
            int zeros = s[i - 1] == '0';
            int j = i;
            while (j > 0 && zeros * zeros <= n) {
                int ones = (i - pre[j]) - zeros;
                if (zeros * zeros <= ones) {
                    output += std::min(j - pre[j], ones - zeros * zeros + 1);
                }
                j = pre[j];
                ++zeros;
            }
        }
        return output;
    }
};