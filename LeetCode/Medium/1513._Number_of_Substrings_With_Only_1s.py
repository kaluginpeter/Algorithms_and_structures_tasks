# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.
# Example 2:
#
# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.
# Example 3:
#
# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
# Solution
# Python O(N) O(1) Combinatorics TwoPointers
class Solution:
    def numSub(self, s: str) -> int:
        mod: int = 1_000_000_007
        output: int = 0
        left: int = 0
        right: int = 0
        n: int = len(s)
        while right < n:
            while right < n and s[right] == '1': right += 1
            length: int = right - left
            output = (output + length * (length + 1) // 2) % mod
            right += 1
            left = right
        return output

# C++ O(N) O(1) Combinatorics TwoPointers
class Solution:
    def numSub(self, s: str) -> int:
        mod: int = 1_000_000_007
        output: int = 0
        left: int = 0
        right: int = 0
        n: int = len(s)
        while right < n:
            while right < n and s[right] == '1': right += 1
            length: int = right - left
            output = (output + length * (length + 1) // 2) % mod
            right += 1
            left = right
        return output