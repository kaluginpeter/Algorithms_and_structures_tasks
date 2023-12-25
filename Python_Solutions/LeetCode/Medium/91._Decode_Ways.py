# A message containing letters from A-Z can be encoded into numbers using the following mapping:
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
#
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
#
# The test cases are generated so that the answer fits in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:
#
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).
# Solution 1 - DP O(N) O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        count1, count2 = 1 if s[0] > '0' else 0, 0
        top = s[0]
        for i in s[1:]:
            prev = count1
            top += i
            if i > '0':
                count1 = count1 + count2
            else:
                count1 = 0
            if len(top) == 2:
                if '09' < top <= '26':
                    count2 = prev
                else:
                    count2 = 0
                top = top[-1]
        return count1 + count2
# Solution 2 DP O(N) O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]