# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
# Solution O(N) O(N)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# Solution Two Pointers O(N) O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left = right = len(s) - 1
        while right > 0 and s[right] == ' ':
            right -= 1
        left = right
        while left >= 0 and s[left] != ' ':
            left -= 1
        return right - left