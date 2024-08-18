# You are given a string s, which is known to be a concatenation of anagrams of some string t.
#
# Return the minimum possible length of the string t.
#
# An anagram is a word or phrase formed by rearranging the letters of a word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "abba"
#
# Output: 2
#
# Explanation:
#
# One possible string t could be "ba".
#
# Example 2:
#
# Input: s = "cdef"
#
# Output: 4
#
# Explanation:
#
# One possible string t could be "cdef", notice that t can be equal to s.
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consist only of lowercase English letters.
# Solution HashTable O(N) O(N)
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n: int = len(s)
        ht = dict()
        for i in s:
            ht[i] = ht.get(i, 0) + 1
        if len(ht) == 1:
            return 1
        for i in range(n, 0, -1):
            if n % i == 0:
                if all(v % i == 0 for v in ht.values()):
                    return sum(v // i for v in ht.values())
