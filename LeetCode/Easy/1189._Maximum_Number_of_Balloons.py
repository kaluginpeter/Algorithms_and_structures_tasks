# Given a string text, you want to use the characters of text
# to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
#
# Example 1:
#
#
# Input: text = "nlaebolko"
# Output: 1
# Example 2:
#
# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:
#
# Input: text = "leetcode"
# Output: 0
#
# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.
# Solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word, l, count, flag = '', ['b', 'a', 'l', 'l', 'o', 'o', 'n'], 0, False
        for i in text:
            if i in 'balloon':
                word += i
        while word:
            for i in l:
                if i in word:
                    count +=1
                    word = word[:word.index(i)] + word[word.index(i)+1:]
                    continue
                if i not in word:
                    flag = True
                    break
            if flag:
                break
        return count // 7