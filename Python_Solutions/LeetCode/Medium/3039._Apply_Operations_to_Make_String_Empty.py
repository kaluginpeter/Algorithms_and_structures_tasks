# You are given a string s.
#
# Consider performing the following operation until s becomes empty:
#
# For every alphabet character from 'a' to 'z', remove the first occurrence of that character in s (if it exists).
# For example, let initially s = "aabcbbca". We do the following operations:
#
# Remove the underlined characters s = "aabcbbca". The resulting string is s = "abbca".
# Remove the underlined characters s = "abbca". The resulting string is s = "ba".
# Remove the underlined characters s = "ba". The resulting string is s = "".
# Return the value of the string s right before applying the last operation. In the example above, answer is "ba".
#
#
#
# Example 1:
#
# Input: s = "aabcbbca"
# Output: "ba"
# Explanation: Explained in the statement.
# Example 2:
#
# Input: s = "abcd"
# Output: "abcd"
# Explanation: We do the following operation:
# - Remove the underlined characters s = "abcd". The resulting string is s = "".
# The string just before the last operation is "abcd".
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 105
# s consists only of lowercase English letters.
# Initial solution O(NlogN) O(N)
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        eng_al: str = 'abcdefghijklmnopqrstuvwxyz'
        ht: dict = dict()
        for i in range(len(s)):
            if s[i] in ht:
                ht[s[i]] = [ht[s[i]][0] + 1, i]
            else:
                ht[s[i]] = [1, i]
        mx = max(ht, key=lambda x: ht[x][0])
        score = ht[mx][0]
        ans: list = [[mx, ht[mx][0], ht[mx][1]]]
        del ht[mx]
        for i in ht:
            if ht[i][0] == score:
                ans.append([i, ht[i][0], ht[i][1]])
        ans.sort(key=lambda x: x[2])
        return ''.join(i[0] for i in ans)
# Solution HashTable O(N) O(N)
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        ht: dict = dict()
        for i in s:
            ht[i] = ht.get(i, 0) + 1
        mx: int = max(ht.values())
        ans: list = list()
        for i in range(len(s) - 1, -1, -1):
            if ht[s[i]] == mx:
                ans.append(s[i])
                ht[s[i]] = -1
        return ''.join(ans[::-1])