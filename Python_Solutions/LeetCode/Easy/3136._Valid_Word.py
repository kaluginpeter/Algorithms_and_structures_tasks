# A word is considered valid if:
#
# It contains a minimum of 3 characters.
# It consists of the digits 0-9, and the uppercase and lowercase English letters. (Not necessary to have all of them.)
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.
#
# Return true if word is valid, otherwise, return false.
#
# Notes:
#
# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.
#
#
# Example 1:
#
# Input: word = "234Adas"
#
# Output: true
#
# Explanation:
#
# This word satisfies the conditions.
#
# Example 2:
#
# Input: word = "b3"
#
# Output: false
#
# Explanation:
#
# The length of this word is fewer than 3, and does not have a vowel.
#
# Example 3:
#
# Input: word = "a3$e"
#
# Output: false
#
# Explanation:
#
# This word contains a '$' character and does not have a consonant.
#
#
#
# Constraints:
#
# 1 <= word.length <= 20
# word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
# Solution O(N) O(1)
class Solution:
    def isValid(self, word: str) -> bool:
        al = 'abcdefghijklmnopqrstuvwxyz'
        ln = len(word)
        l, u = False, False
        c, v = False, False
        d = False
        for i in word:
            if i.isupper():
                if i.lower() in 'aeiou':
                    v = True
                elif i.lower() in al:
                    c = True
                u = True
            elif i.islower():
                if i in 'aeiou':
                    v = True
                elif i in al:
                    c = True
                l = True
            elif i.isdigit():
                d = True
            else:
                return False
        an = int(u) + int(l) + int(d)
        return len(word) >= 3 and an > 0 and c and v