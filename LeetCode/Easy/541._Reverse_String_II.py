# Given a string s and an integer k, reverse the first k characters for every 2k
# characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and leave the other as original.
#
# Example 1:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
#
# Input: s = "abcd", k = 2
# Output: "bacd"
#
# Constraints:
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104
# Solution
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        size = len(s)
        output_str = ""
        i = 0
        while size - i*2*k >= 2*k:
            output_str += s[i*2*k : i*2*k+k][::-1] + s[i*2*k+k : (i+1)*2*k]
            i += 1
        if size - i*2*k < k:
            output_str += s[i*2*k:][::-1]
        else:
            output_str += s[i*2*k:i*2*k+k][::-1] + s[i*2*k+k:]
        return output_str