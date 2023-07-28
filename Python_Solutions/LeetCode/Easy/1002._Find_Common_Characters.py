# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
# Solution
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = []
        for i in set(words[0]):
            if all(i in j for j in words):
                c = min(j.count(i) for j in words)
                l += [i] * c
        return l