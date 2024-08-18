# Given a hash of letters and the number of times they occur, recreate all of the
# possible anagram combinations that could be created using all of the letters, sorted alphabetically.
#
# The inputs will never include numbers, spaces or any special characters, only lowercase letters a-z.
#
# E.g. get_words({2=>["a"], 1=>["b", "c"]}) => ["aabc", "aacb", "abac", "abca", "acab",
# "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"]
#
# PUZZLES
# Solution
import itertools
def get_words(hash):
    s = ''.join(k * v for k, v in hash.items() for v in v)
    return sorted({''.join(i) for i in itertools.permutations(s)})