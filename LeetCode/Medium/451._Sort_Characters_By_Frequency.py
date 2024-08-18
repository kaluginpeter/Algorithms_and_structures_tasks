# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
#
# Return the sorted string. If there are multiple answers, return any of them.
#
#
#
# Example 1:
#
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.
# Solution 1 HashTable in list comprehension O(NlogN) O(N)
class Solution:
    def frequencySort(self, s: str) -> str:
        ht: dict = {}
        for i in s:
            ht[i] = ht.get(i, 0) + 1
        return ''.join(i * ht[i] for i in sorted(ht, key=lambda x: ht[x], reverse=True))
# Solution 2 Bucket Sort O(N) O(N)
class Solution:
    def frequencySort(self, s: str) -> str:
        ht: dict = {}
        for i in s:
            ht[i] = ht.get(i, 0) + 1
        bucket: list = [[] for _ in range(max(ht.values()))]
        for i in ht:
            bucket[ht[i]-1] += [i * ht[i]]
        ans: list = []
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                ans.append(j)
        return ''.join(ans)