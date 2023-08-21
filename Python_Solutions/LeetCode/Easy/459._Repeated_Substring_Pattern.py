# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
#
#
#
# Example 1:
#
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:
#
# Input: s = "aba"
# Output: false
# Example 3:
#
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of lowercase English letters.
# Solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Solution 1
        return s in s[1:] + s[:-1]
        # Solution 2
        l = len(s)
        j = l
        for i in range(l // 2):
            while len(s[:i+1] * j) >= l:
                j -= 1
            if s[:i+1] * (j+1) == s:
                return True
        return False
        # Solution 3
        def kmp_table(W):
            n = len(W)
            T = [0 for _ in range(n)]
            T[0] = -1
            pos = 0
            for i in range(1, n):
                if W[i] == W[pos]:
                    T[i] = T[pos]
                else:
                    T[i] = pos
                    pos = T[pos]
                    while pos >= 0 and W[i] != W[pos]:
                        pos = T[pos]
                pos += 1
            return T
        string, substring = s[1:] + s[:-1], s
        m = len(substring)
        n = len(string)
        T = kmp_table(substring)
        pos = 0
        i = 0
        while i < n:
            if string[i] != substring[pos]:
                pos = T[pos]
                if pos < 0:
                    pos += 1
                    i += 1
            else:
                i += 1
                pos += 1
                if pos == m:
                    return True
        return False

# Solution 3
class Solution(object):
    def repeatedSubstringPattern(self, s):
        if len(s) == 1:
            return False
        for i in range(len(s) // 2):
            count = s[:i+1]
            cop = ''
            while len(cop) < len(s):
                cop += count
            if cop == s:
                return True
        return False