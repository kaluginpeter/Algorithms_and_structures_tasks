# Given an array of strings words, return the first palindromic string in the array.
# If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.
#
# Example 1:
#
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
# Example 2:
#
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
# Example 3:
#
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.
#
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists only of lowercase English letters.
# Solution
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                return words[i]
        return ''


# Solution Two Pointers O(N) O(1)
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            left, right = 0, len(i) - 1
            flag: bool = True
            while left <= right:
                if i[left] != i[right]:
                    flag = not flag
                    break
                left += 1
                right -= 1
            if flag:
                return i
        return ''
# Solution Two Pointers One Liner O(N) O(1)
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((i for i in words if all(i[j] == i[-(j+1)] for j in range(len(i)))), '')