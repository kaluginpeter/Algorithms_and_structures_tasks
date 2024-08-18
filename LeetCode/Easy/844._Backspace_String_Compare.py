# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
#
# Example 1:
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
#
#
# Follow up: Can you solve it in O(n) time and O(1) space?
# Solution
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x, y = len(s) - 1, len(t) - 1
        top_x, top_y = 0, 0
        while x >= 0 or y >= 0:
            while x >= 0:
                if s[x] == '#':
                    top_x += 1
                    x -= 1
                elif top_x > 0:
                    top_x -= 1
                    x -= 1
                else:
                    break
            while y >= 0:
                if t[y] == '#':
                    top_y += 1
                    y -= 1
                elif top_y > 0:
                    top_y -= 1
                    y -= 1
                else:
                    break
            if x >= 0 and y >= 0 and s[x] != t[y]:
                return False
            if (x >= 0) != (y >= 0):
                return False
            x -= 1
            y -= 1
        return True