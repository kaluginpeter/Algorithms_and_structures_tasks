# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
#
# Return the number of special letters in word.
#
#
#
# Example 1:
#
# Input: word = "aaAbcBC"
#
# Output: 3
#
# Explanation:
#
# The special characters in word are 'a', 'b', and 'c'.
#
# Example 2:
#
# Input: word = "abc"
#
# Output: 0
#
# Explanation:
#
# No character in word appears in uppercase.
#
# Example 3:
#
# Input: word = "abBCab"
#
# Output: 1
#
# Explanation:
#
# The only special character in word is 'b'.
#
#
#
# Constraints:
#
# 1 <= word.length <= 50
# word consists of only lowercase and uppercase English letters.
# Solution HashTable O(N) O(N)
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ht: dict[str, int] = dict()
        for i in word:
            ht[i] = ht.get(i, 0) + 1
        ans: int = 0
        for i in ht:
            if i.lower() in ht and i.upper() in ht:
                ans += 1
        return ans // 2