# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
#
# Return any possible rearrangement of s or return "" if not possible.
#
#
#
# Example 1:
#
# Input: s = "aab"
# Output: "aba"
# Example 2:
#
# Input: s = "aaab"
# Output: ""
#
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.
# Accepted
# 325.3K
# Submissions
# 600.3K
# Acceptance Rate
# 54.2%
# Solution
class Solution(object):
    def reorganizeString(self, s):
        n, c = len(s), Counter(s)
        arr = sorted([ch for ch in c], key = lambda x: -c[x])
        if c[arr[0]] > (len(s)+1)//2: return ''
        chars = list(chain(*[[ch]*c[ch] for ch in arr]))
        return ''.join([chars[(n+i)//2] if i%2 else chars[i//2] for i in range(n)])