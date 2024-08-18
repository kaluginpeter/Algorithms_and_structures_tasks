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


# Solution HashTable Greedy O(N) O(N)
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ht: dict[str, int] = defaultdict(int)
        for i in s: ht[i] += 1
        answer: int = 0
        mx_odd: str = None
        for i in ht:
            if ht[i] % 2 == 0: answer += ht[i]
            elif not mx_odd or ht[i] > ht[mx_odd]:
                answer += (ht[mx_odd] - 1) if mx_odd else 0
                mx_odd = i
            else: answer += ht[i] - 1
        return answer + ht[mx_odd]