# You are given a string word and a non-negative integer k.
#
# Return the total number of
# substrings
#  of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
#
#
#
# Example 1:
#
# Input: word = "aeioqq", k = 1
#
# Output: 0
#
# Explanation:
#
# There is no substring with every vowel.
#
# Example 2:
#
# Input: word = "aeiou", k = 0
#
# Output: 1
#
# Explanation:
#
# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".
#
# Example 3:
#
# Input: word = "ieaouqqieaouqq", k = 1
#
# Output: 3
#
# Explanation:
#
# The substrings with every vowel and one consonant are:
#
# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
#
#
# Constraints:
#
# 5 <= word.length <= 250
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5
# Solution
# Python Brute Force O(N**2) O(1)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        count: int = 0
        for left in range(len(word)):
            vow: dict = dict()
            const: int = 0
            for right in range(left, len(word)):
                if word[right] in 'aeoiu':
                    vow[word[right]] = vow.get(word[right], 0) + 1
                else: const += 1
                if len(vow) == 5 and const == k: count += 1
        return count
# Python Sliding Window O(N) O(1)
from collections import defaultdict
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels: set[str] = set("aeiou")
        hashmap: dict[str, int] = defaultdict(int)
        consonants: int = 0
        left: int = 0
        answer: int = 0
        for right in range(len(word)):
            if word[right] in vowels:
                hashmap[word[right]] += 1
            else: consonants += 1
            while consonants > k:
                if word[left] in hashmap :
                    hashmap[word[left]] -= 1
                    if hashmap[word[left]] == 0:
                        del hashmap[word[left]]
                else: consonants -= 1
                left += 1
            if len(hashmap) == 5 and consonants == k:
                answer += 1
                second_left: int = left
                second_hashmap: dict[str, int] = hashmap.copy()
                second_consonants: int = consonants
                while len(second_hashmap) == 5:
                    if word[second_left] in second_hashmap:
                        second_hashmap[word[second_left]] -= 1
                        if second_hashmap[word[second_left]] == 0:
                            del second_hashmap[word[second_left]]
                    else:second_consonants -= 1
                    second_left += 1
                    if second_consonants == k and len(second_hashmap) == 5:
                        answer += 1
                    if consonants < k: break
        return answer