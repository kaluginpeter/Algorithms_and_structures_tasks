# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
# Example 1:
#
# Input: s = "hello"
# Output: "holle"
# Example 2:
#
# Input: s = "leetcode"
# Output: "leotcede"
#
# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.
# Solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        string = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if string[i].lower() not in vowels:
                i += 1
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        return "".join(string)