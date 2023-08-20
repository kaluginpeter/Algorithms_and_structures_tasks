# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
#
#
# Example 1:
#
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:
#
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
#
#
# Constraints:
#
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# Solution
class Solution(object):
    def longestPalindrome(self, s):
        d, count = {}, 0
        for i in s:
            if i in d:
                d[i] += 1
                if d[i] % 2 == 0:
                    count += 2
            else:
                d[i] = 1
        return count + 1 if len(s) - count != 0 else count