# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:
#
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
#
#
# Constraints:
#
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
# Solution
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = {}
        for i in s1.split():
            d[i] = d.get(i, 0) + 1
        for i in s2.split():
            d[i] = d.get(i, 0) + 1
        return [i for i in d if d[i] == 1]

# Solution O(N) O(N) HashMap Counting
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        storage_s1: dict[str, int] = dict()
        storage_s2: dict[str, int] = dict()
        for word in s1.split():
            storage_s1[word] = storage_s1.get(word, 0) + 1
        for word in s2.split():
            storage_s2[word] = storage_s2.get(word, 0) + 1
        output: list[str] = []
        for word in storage_s1:
            if storage_s1[word] == 1 and word not in storage_s2:
                output.append(word)
        for word in storage_s2:
            if storage_s2[word] == 1 and word not in storage_s1:
                output.append(word)
        return output
