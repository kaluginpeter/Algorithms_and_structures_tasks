# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
#
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
#
#
#
# Example 1:
#
# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:
#
# Input: paragraph = "a.", banned = []
# Output: "a"
#
#
# Constraints:
#
# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.
# Solution
class Solution:
    def mostCommonWord(self, letters: str, ban: List[str]) -> str:
        d, word = {}, ''
        for i in letters.lower():
            if not i.isalpha():
                if word and word not in ban:
                    if word not in d:
                        d[word] = 0
                    d[word] += 1
                word = ''
            else:
                word += i
        if word and word not in ban:
            if word not in d:
                d[word] = 0
            d[word] += 1
        return sorted(d.items(), key=lambda x: -x[1])[0][0]