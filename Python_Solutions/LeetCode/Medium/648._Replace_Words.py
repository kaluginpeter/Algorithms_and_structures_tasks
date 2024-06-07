# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
#
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
#
# Return the sentence after the replacement.
#
#
#
# Example 1:
#
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 2:
#
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
#
#
# Constraints:
#
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 106
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.
# Solution HashSet O(OK) O(N)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        hs: set[str] = set()
        len_max_word: int = 0
        for word in dictionary:
            len_max_word = max(len_max_word, len(word))
            hs.add(word)
        output: list[str] = []
        for word in sentence.split():
            idx: int = 0
            matched: bool = False
            while idx < len_max_word:
                if word[:idx + 1] in hs:
                    matched = True
                    output.append(word[:idx + 1])
                    break
                idx += 1
            if not matched: output.append(word)
        return ' '.join(output)