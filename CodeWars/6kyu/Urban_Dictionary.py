# Design a data structure that supports the following two operations:
#
# addWord / add_word which adds a word,
# search which searches a literal word or a regular expression string containing lowercase letters "a-z" or "." where "." can represent any letter. Return true if the search term fully matches any word previously added; otherwise, return false.
# You may assume that all given words contain only lowercase letters.
#
# Examples
# wd = WordDictionary()
#
# wd.add_word("bad")
# wd.add_word("dad")
# wd.add_word("mad")
#
# wd.search("pad") == False
# wd.search("bad") == True
# wd.search(".ad") == True
# wd.search("b..") == True
# Note: the data structure will be initialized multiple times during the tests!
#
# AlgorithmsObject-oriented Programming
# Solution
class WordDictionary:
    def __init__(self):
        self.dataset: list[str] = []

    def add_word(self, word):
        self.dataset.append(word)

    def is_equal(self, word: str, data: str) -> bool:
        for i in range(len(word)):
            if word[i] != data[i]:
                if word[i] != '.': return False
        return True

    def search(self, word):
        for data in self.dataset:
            if len(word) != len(data):
                continue
            elif self.is_equal(word, data):
                return True
        return False