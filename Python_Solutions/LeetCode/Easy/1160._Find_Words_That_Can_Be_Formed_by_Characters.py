# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.
# Solution
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count, mi_char = 0, chars
        for i in words:
            cop = i
            for j in i:
                if j in mi_char:
                    i = i[:i.index(j)] + i[i.index(j)+1:]
                    mi_char = mi_char[:mi_char.index(j)] + mi_char[mi_char.index(j)+1:]
            if i == '':
                count += len(cop)
            mi_char = chars
        return count

# Solution 2 Speed O(N) Memory O(N)
class Solution(object):
    def countCharacters(self, words, chars):
        d, count = {}, 0
        for i in chars:
            d[i] = d.get(i, 0) + 1
        for i in words:
            top, flag = {}, True
            for j in i:
                top[j] = top.get(j, 0) + 1
                if j not in d or top[j] > d[j]:
                    flag = False
                    break
            if flag:
                count += len(i)
        return count