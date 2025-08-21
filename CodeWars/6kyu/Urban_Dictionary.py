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