# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# Solution O(NlogN) O(N)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht: dict = {}
        for i in range(len(strs)):
            x: str = ''.join(sorted(strs[i]))
            if x in ht:
                ht[x] += [i]
            else:
                ht[x] = [i]
        ans: list = []
        for i in ht:
            top: list = []
            for j in ht[i]:
                top.append(strs[j])
            ans.append(top)
        return ans

# Solution HashTable O(NlogN) O(N)
class Solution:
    def get_index(self, word: str) -> str:
        return ''.join(sorted(word))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage: dict[str, list[str]] = dict()
        for word in strs:
            idx: str = self.get_index(word)
            storage[idx] = storage.get(idx, []) + [word]
        return storage.values()