# There is a strange printer with the following two special properties:
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.
#
#
#
# Example 1:
#
# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:
#
# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# Solution Dynamic Programming O(N**3) O(N**2)
class Solution:
    def shorten_string(self, s: str) -> str:
        stack: list[str] = []
        for right in range(len(s)):
            if stack and stack[-1] == s[right]:
                continue
            else:
                stack.append(s[right])
        return ''.join(stack)

    def strangePrinter(self, s: str) -> int:
        s: str = self.shorten_string(s)
        n: int = len(s)
        # Max n constraint is 100, so initialize 100 + 1
        dp: list[list[int]] = [[0] * 101 for _ in range(101)]
        # Go from right to left
        for i in range(n - 1, -1, -1):
            # Initial state for current ceil
            dp[i][i] = 1
            # Go from current left to right
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                    continue
                x: int = dp[i][j - 1] + 1
                # Choose minimum possible x
                for k in range(i + 1, j - 1):
                    if s[k] == s[j]:
                        x = min(x, dp[i][k - 1] + dp[k][j - 1])
                dp[i][j] = x
        return dp[0][n-1]