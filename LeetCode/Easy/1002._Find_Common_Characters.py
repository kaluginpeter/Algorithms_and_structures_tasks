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

# Solution Array HashTable O(N) O(N)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letter_storage: list[list[int]] = [[] for _ in range(27)] # total storage
        n: int = 0 # length of words
        for word in words:
            n += 1
            # local storage to each word
            local_letter_storage: list[int] = [0 for _ in range(27)]
            for letter in word: # count all frequences of each charackter in one word
                local_letter_storage[ord(letter) - 96] += 1
            for char in range(27): # Adding result of local storage to total storage
                letter_storage[char] += [local_letter_storage[char]]
        common_characters: list[int] = [] # Answer array
        for char in range(27):
            if len(letter_storage[char]) == n: # if character contained in all words
                common_characters.extend([chr(char + 96)] * min(letter_storage[char])) # addind minimum frequence
        return common_characters